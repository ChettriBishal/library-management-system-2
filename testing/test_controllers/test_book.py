import pytest
from unittest.mock import patch, Mock
from src.controllers.book import Book


class TestBook:

    @pytest.fixture
    def book_obj(self):
        obj = Book(300, 'test_name', 'test_author', 9, 500, 'fiction')
        return obj

    @patch('src.controllers.book.insert_item')
    def test_add_book(self, mock_insert_item, book_obj, capsys):
        mock_insert_item.return_value = True

        book_obj.add_book()
        capsys.readouterr()

        mock_insert_item.assert_called_once()

    @patch('src.controllers.book.remove_item')
    def test_remove_book(self, mock_remove_item, book_obj, capsys):
        mock_remove_item.return_value = True

        book_obj.remove_book()
        capsys.readouterr()

        mock_remove_item.assert_called_once()

    def test_show_book_details(self, monkeypatch, book_obj):
        monkeypatch.setattr('builtins.print', lambda _: True)
        res = book_obj.show_book_details()
        assert res is None

    def test_get_book_details(self, book_obj):
        res = book_obj.get_book_details
        assert res is not None
