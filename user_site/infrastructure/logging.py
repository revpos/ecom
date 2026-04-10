import logging, logging.config
import sys
from contextvars import ContextVar

def setup_logging():
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s %(levelname)s [%(name)s] [ReqID: %(request_id)s] %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "filters": {
            "request_id": {"()": "app.infrastructure.logging.RequestIdFilter"},
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "stream": sys.stdout,
                "filters": ["request_id"],
            },
        },
        "root": {"level": "INFO", "handlers": ["console"]},
        "loggers": {
            "uvicorn.error": {"level": "INFO"},
            "uvicorn.access": {"level": "INFO", "propagate": False},
        },
    }
    logging.config.dictConfig(logging_config)


# A global 'context' that holds the ID for the current thread/task
request_id_ctx_var: ContextVar[str] = ContextVar("request_id", default="n/a")

class RequestIdFilter(logging.Filter):
    def filter(self, record):
        # Injects the current Request ID into the log record
        record.request_id = request_id_ctx_var.get()
        return True