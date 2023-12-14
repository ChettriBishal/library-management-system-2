import pytest
from unittest.mock import Mock

from src.helpers.home_menu import librarian_menu


class TestLibrarianMenu:

    @pytest.fixture
    def mock_librarian(self):
        mock_class = Mock()
        _instance = mock_class.return_value
        _instance.add_book.return_value = True
        _instance.sort_books_by_rating.return_value = lambda _: True
        _instance.remove_book.return_value = True
        return _instance

    @pytest.mark.parametrize("choices", [('1', '2', '4')])
    def test_choice_1(self, choices, mock_librarian, monkeypatch):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        librarian_menu(mock_librarian)
        mock_librarian.add_book.assert_called_once()

    @pytest.mark.parametrize("choices", [('2', '4')])
    def test_choice_2(self, choices, mock_librarian, monkeypatch):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        librarian_menu(mock_librarian)
        mock_librarian.sort_books_by_rating.assert_called_once()

    @pytest.mark.parametrize("choices", [('3', 'test_book', '4')])
    def test_choice_3(self, choices, mock_librarian, monkeypatch):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        librarian_menu(mock_librarian)
        mock_librarian.remove_book.assert_called_once()

    @pytest.mark.parametrize("choices", [('7', '4')])
    def test_choice_invalid(self, capsys, choices, mock_librarian, monkeypatch):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        librarian_menu(mock_librarian)
        captured = capsys.readouterr()

        assert captured.out.strip() == "Invalid Choice!"
