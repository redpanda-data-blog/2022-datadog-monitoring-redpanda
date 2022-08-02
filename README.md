# Using Datadog to Monitor Redpanda

This README informs the users about the setup of the demo project.

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
