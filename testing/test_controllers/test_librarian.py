import pytest
from unittest.mock import patch, Mock
from src.controllers.user import Librarian


class TestLibrarian:
    @pytest.fixture
    def lib_obj(self):
        obj = Librarian('test_user', 'test_password', 'librarian')
        return obj

    @pytest.fixture
    def mock_book(self, mocker):
        _instance = Mock()
        return mocker.patch('src.controllers.user.Book', return_value=_instance)

    @patch('src.controllers.user.get_book_details')
    def test_add_book(self, mock_get_book, lib_obj):
        book_instance = Mock()
        mock_get_book.return_value = book_instance
        book_instance.add_book.return_value = True

        lib_obj.add_book()

        book_instance.add_book.assert_called_once()

    @patch('src.controllers.user.get_item', return_value=('name', 'author'))
    def test_remove_book(self, mock_get_item, mock_book, lib_obj):
        _obj = mock_book()
        _obj.remove_book.return_value = True

        res = lib_obj.remove_book('test_name')

        assert res is True

    @patch('src.controllers.user.get_item', return_value=None)
    def test_remove_book_invalid(self, mock_get_item, mock_book, lib_obj):
        _obj = mock_book()

        res = lib_obj.remove_book('test_name')

        assert res is False


