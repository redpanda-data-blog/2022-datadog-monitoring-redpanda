#!/usr/bin/env python3

import logging
import os
import time
import uuid
from datetime import datetime
from json import dumps

import requests
import schedule
from kafka import KafkaProducer

from config import CRYPTO_TOPIC

COIN_PAGE = "https://api.coinranking.com/v2/coins"
TOKEN = os.getenv(
    "TOKEN",
    ".",
)
HEADERS = {"Authorization": f"access_token {TOKEN}"}
FREQUENCY = int(os.getenv("PRODUCE_FREQUENCY", "30"))


def produce_list_of_coin_dict_into_queue(list_of_dict: list) -> None:
    producer = KafkaProducer(bootstrap_servers="redpanda:9092")
    for coin_with_model in list_of_dict:
        try:
            producer.send(
                topic=CRYPTO_TOPIC,
                value=dumps(coin_with_model).encode("utf-8"),
                key=uuid.uuid4().hex.encode("utf-8"),
            )
        except Exception as e:
            logging.error(
                f"There is a problem with the {coin_with_model}\nThe problem is: {e}!"  # noqa
            )
    producer.flush()
    logging.info(producer.metrics())
    producer.close()


def get_json_api(page: str) -> tuple:
    get_request = requests.get(page, headers=HEADERS)
    assert get_request.status_code == 200, "Request not successful"
    return get_request.json(), get_request.status_code


def get_coin_model(coin: dict) -> dict:
    try:
        return {
            "uuid": coin.get("uuid"),
            "name": coin.get("name"),
            "symbol": coin.get("symbol"),
            "btc_price": coin.get("btcPrice"),
            "last_24h_volume": coin.get("24hVolume"),
            "marketcap": coin.get("marketCap"),
            "price": coin.get("price"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        # In the API milliseconds are used.
    except Exception as e:
        logging.error(f"Exception: {e}")
        return {}


def get_all_coins_with_model(all_coins: dict) -> list:
    return [get_coin_model(coin) for coin in all_coins["data"]["coins"]]


def coins_producer() -> None:
    all_coins, _ = get_json_api(COIN_PAGE)
    coins_with_model = get_all_coins_with_model(all_coins)
    produce_list_of_coin_dict_into_queue(coins_with_model)


if __name__ == "__main__":

    schedule.every(FREQUENCY).seconds.do(coins_producer)
    while True:
        schedule.run_pending()
        time.sleep(1)
