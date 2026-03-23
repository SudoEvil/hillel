import unittest
from unittest.mock import patch
import logging

# Імпортуємо функцію (припустимо вона в файлі login.py)
from homework14 import log_event


class TestLogEvent(unittest.TestCase):

    """
    Цей тестовий клас перевіряє,
    чи функція log_event правильно викликає
    методи логера залежно від статусу входу.
    """

    @patch("logging.getLogger")
    def test_log_event_success(self, mock_get_logger):
        """
        Перевіряємо, що при статусі 'success'
        викликається logger.info()
        """

        mock_logger = mock_get_logger.return_value

        log_event("alex", "success")

        mock_logger.info.assert_called_once_with(
            "Login event - Username: alex, Status: success"
        )


    @patch("logging.getLogger")
    def test_log_event_expired(self, mock_get_logger):
        """
        Перевіряємо, що при статусі 'expired'
        викликається logger.warning()
        """

        mock_logger = mock_get_logger.return_value

        log_event("alex", "expired")

        mock_logger.warning.assert_called_once_with(
            "Login event - Username: alex, Status: expired"
        )


    @patch("logging.getLogger")
    def test_log_event_failed(self, mock_get_logger):
        """
        Перевіряємо, що при статусі 'failed'
        викликається logger.error()
        """

        mock_logger = mock_get_logger.return_value

        log_event("alex", "failed")

        mock_logger.error.assert_called_once_with(
            "Login event - Username: alex, Status: failed"
        )


    @patch("logging.getLogger")
    def test_log_event_unknown_status(self, mock_get_logger):
        """
        Перевіряємо, що будь-який інший статус
        теж викликає logger.error()
        """

        mock_logger = mock_get_logger.return_value

        log_event("alex", "unknown_status")

        mock_logger.error.assert_called_once_with(
            "Login event - Username: alex, Status: unknown_status"
        )


if __name__ == "__main__":
    unittest.main()