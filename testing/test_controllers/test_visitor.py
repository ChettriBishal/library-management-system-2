import pytest
from unittest.mock import patch
from src.controllers.user import Visitor


class TestVisitor:
    @pytest.fixture
    def vis_obj(self):
        obj = Visitor('test_user', 'test_password', 'librarian')
        return obj

    @pytest.fixture
    def mock_get_many_items(self, mocker):
        return mocker.patch('src.controllers.user.get_many_items')

    def test_issue_book_none(self, mock_get_many_items, vis_obj):
        mock_get_many_items.return_value = None
        res = vis_obj.issue_book('test_book')
        assert res is None

    def test_issue_book(self, mocker, mock_get_many_items, vis_obj):
        books = [[111], [111]]
        mock_get_many_items.return_value = books

        book_issue_class = mocker.patch('src.controllers.user.BookIssue')
        _instance = book_issue_class.return_value
        _instance.add_book.return_value = True

        vis_obj.issue_book('test_name')

        _instance.add_book.assert_called_once()

    def test_books_issued(self, mock_get_many_items, vis_obj):
        mock_get_many_items.return_value = ['one', 'two']

        res = vis_obj.books_issued()
        assert res

    @patch('src.controllers.user.get_item')
    def test_return_book_none(self, mock_get_item, vis_obj):
        mock_get_item.return_value = None

        res = vis_obj.return_book(123)
        assert res is False

    @patch('src.controllers.user.get_item')
    @patch('src.controllers.user.remove_item')
    def test_return_book(self, mock_remove_item, mock_get_item, vis_obj):
        mock_get_item.return_value = [[123]]

        res = vis_obj.return_book(123)
        assert res is True
