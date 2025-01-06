import pytest
from logger import Logger

def test_log_info():
    logger = Logger()
    assert logger.log_info("Test message") == None


class Logger:
    """Клас для логування подій у системі."""

    def log_info(self, message: str) -> None:
        """Логує інформаційне повідомлення."""
        print(f"[INFO]: {message}")

    def log_error(self, message: str) -> None:
        """Логує повідомлення про помилку."""
        print(f"[ERROR]: {message}")


