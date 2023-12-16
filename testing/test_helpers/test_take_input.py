import pytest
from unittest.mock import Mock, patch
from src.helpers import take_input


class TestTakeInput:

    @pytest.mark.parametrize("user_inputs", [('test_book', 'test_author', 1345, 7, 'genre')])
    def test_get_book_details(self, user_inputs, mocker, monkeypatch):
        user_input = iter(user_inputs)

        monkeypatch.setattr('builtins.input', lambda _: next(user_input))

        mocker.patch('src.helpers.take_input.generate_uuid', return_value=123)
        _instance = Mock()
        mocker.patch('src.helpers.take_input.Book', return_value=_instance)

        res = take_input.get_book_details()

        assert res is _instance

    def test_get_visitor_details_valid(self, capsys, mocker, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'test_name')
        mocker.patch('src.helpers.take_input.validate_username', return_value=True)
        mocker.patch('src.helpers.take_input.validate_password', return_value=True)

        mocker.patch('maskpass.advpass', return_value='test_password')

        res = take_input.get_visitor_details()

        capsys.readouterr()
        assert res is not None

    def test_get_book_query(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'test_name')

        res = take_input.get_book_query()
        assert res in 'test_name'
