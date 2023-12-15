import pytest
from unittest.mock import patch
from src.helpers import initialisation


class TestInitialisation:
    @pytest.fixture
    def mock_execute_query(self, mocker):
        return mocker.patch('src.helpers.initialisation.execute_query')

    def test_create(self, mock_execute_query):
        mock_execute_query.return_value = True

        initialisation.create_book_table()
        initialisation.create_user_table()
        initialisation.create_book_issue_table()

        mock_execute_query.assert_called()

    @patch('src.helpers.initialisation.create_book_table',return_value=True)
    @patch('src.helpers.initialisation.create_user_table',return_value=True)
    @patch('src.helpers.initialisation.create_book_issue_table',return_value=True)
    def test_init(self, mock_issue_table, mock_user_table, mock_book_table):
        initialisation.init_all()

        mock_issue_table.assert_called()
        mock_user_table.assert_called()
        mock_book_table.assert_called()
