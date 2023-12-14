import pytest
from unittest.mock import Mock
from src.controllers.user import User


class TestUser:
    @pytest.fixture
    def user_obj(self):
        obj = User('test_user', 'test_password', 'test_role')
        return obj

    @pytest.fixture
    def mock_book(self, mocker):
        _instance = Mock()
        return mocker.patch('src.controllers.user.Book', return_value=_instance)

    @pytest.fixture
    def mock_get_many_items(self, mocker):
        return mocker.patch('src.controllers.user.get_many_items')

    def test_user_details(self, capsys, user_obj):
        res = user_obj.user_details()
        assert res is not None

    def test_query_book(self, mock_get_many_items, user_obj):
        mock_get_many_items.return_value = ['item_1', 'item_2', 'item_3']
        user_obj.query_book('test_name')

        mock_get_many_items.assert_called_once()

    def test_sort_books_by_rating(self, mock_get_many_items, mock_book, user_obj):
        mock_get_many_items.return_value = [('t_1', 't_1_2'), ('t_2', 't_2_1')]
        user_obj.sort_books_by_rating()

        _obj = mock_book()
        _obj.show_book_details.assert_called()

    def test_sort_books_by_price(self, mock_get_many_items, mock_book, user_obj):
        mock_get_many_items.return_value = [('t_1', 't_1_2'), ('t_2', 't_2_1')]
        user_obj.sort_books_by_price()

        _obj = mock_book()
        _obj.show_book_details.assert_called()

    def test_sort_books_by_genre_valid(self, mock_get_many_items, mock_book, user_obj):
        mock_get_many_items.return_value = [('t_1', 't_1_2'), ('t_2', 't_2_1')]
        user_obj.group_books_by_genre('test')

        _obj = mock_book()
        _obj.show_book_details.assert_called()

    def test_sort_books_by_rating_none(self, capsys, mock_get_many_items, user_obj):
        mock_get_many_items.return_value = None

        user_obj.group_books_by_genre('test')
        captured = capsys.readouterr()

        assert captured.out.strip() == 'Null entries for genre `test`'


