from datetime import datetime
import logging
import json

# Логування подій та помилок

class Logger:
    def __init__(self, log_file, log_level):
        self.logger = logging.getLogger("ApplicationLogger")
        self.logger.setLevel(getattr(logging, log_level.upper()))
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(JsonFormatter())
        self.logger.addHandler(file_handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message, exc_info=True)

    def log_fatal(self, message):
        self.logger.critical(message, exc_info=True)

# Форматер для структурованих логів у JSON для зручної читабельності

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_message = {
            "timestamp": datetime.now().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "line_number": record.lineno,
        }

        # Форматування винятків у багаторядковий вигляд
        if record.exc_info:
            exception_details = self.formatException(record.exc_info)
            # Розділення кожного рядка для кращої читабельності
            log_message["exception"] = exception_details.splitlines()

        return json.dumps(log_message, indent=4)
