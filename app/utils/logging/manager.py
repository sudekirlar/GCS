import logging
import logging.config
import json
from datetime import datetime

class JsonFormatter(logging.Formatter):
    """
    Log kaydını JSON formatında oluşturur.
    """
    def format(self, record):
        # Temel log bilgilerini bir sözlükte topluyoruz.
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "logger": record.name,
            "level": record.levelname,
            "message": record.getMessage()
        }
        # Eğer exception bilgisi varsa onu da ekleyelim.
        if record.exc_info:
            log_record["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(log_record)

class LogManager:
    """
    Uygulamanın loglama yapılandırmasını, logging.conf dosyası üzerinden yükler.
    """
    @staticmethod
    def setup_logging(config_file='logging.conf'):
        logging.config.fileConfig(config_file, disable_existing_loggers=False)