#!/usr/bin/env python3

import json
import logging
from time import sleep

from kafka import KafkaConsumer

from config import CRYPTO_TOPIC

if __name__ == "__main__":
    consumer = KafkaConsumer(
        CRYPTO_TOPIC,
        bootstrap_servers=["redpanda:9092"],
        group_id="consumer_1",
        auto_offset_reset="earliest",
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    while True:
        messages = consumer.poll(timeout_ms=1000, max_records=25)
        logging.info(messages)
        sleep(10)
