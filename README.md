# Using Datadog to Monitor Redpanda

Use this demo to learn how to monitor Redpanda with DataDog.

Follow along with [this tutorial on the Redpanda blog](https://redpanda.com/blog/) to put this demo into action. 

----------------------

## How to setup the project?

1. Have a Datadog account to setup:
    - Your Datadog API Key (`DD_API_KEY`)
    - The name of your Datadog site (`DD_SITE`)
2. Have Docker and [docker-compose](https://docs.docker.com/compose/install/) installed on your computer.
3. Have a Coin Ranking API account [with an API Token.](https://developers.coinranking.com/create-account)
4. Create a `.env` file next to this `README.md`. Include the following:
    ```
    TOKEN=<COINRANKING_API_TOKEN>
    DATADOG_API_KEY=<DD_API_KEY>
    ```
5. Run `docker-compose`:
    ```
    docker-compose up -d
    ```
-----------------------

## About Redpanda 

Redpanda is Apache Kafka® API-compatible. Any client that works with Kafka will work with Redpanda, but we have tested the ones listed [here](https://docs.redpanda.com/docs/reference/faq/#what-clients-do-you-recommend-to-use-with-redpanda).

* You can find our main project repo here: [Redpanda](https://github.com/redpanda-data/redpanda)
* Join the [Redpanda Community on Slack](https://redpanda.com/slack)
* [Sign up for Redpanda University](https://university.redpanda.com/) for free courses on data streaming and working with Redpanda
