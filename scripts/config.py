import logging

ENV = "dev"
CRYPTO_TOPIC = "crypto"
LOGGING_FORMAT_STRING = (
    "%(asctime)s %(levelname)-1s [%(name)s] [%(filename)s:%(lineno)d] "
    f"[env={ENV} dd.trace_id=%(process)d dd.span_id=%(thread)d] - %(message)s"
)

# Root level basic logging configuration
logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT_STRING)

# kafka specific logging configuration
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(LOGGING_FORMAT_STRING))
producer_logger = logging.getLogger(__name__)
producer_logger.addHandler(console_handler)
kafka_logger = logging.getLogger("kafka.KafkaProducer")
kafka_logger.propagate = False
kafka_logger.addHandler(console_handler)
