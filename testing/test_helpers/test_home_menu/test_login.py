import pytest
from unittest.mock import Mock
from src.helpers import home_menu
from src.helpers.home_menu import maskpass, Authentication


class TestLogin:
    @pytest.mark.parametrize("inputs", [('test_user', '3')])
    def test_login_no_account(self, inputs, monkeypatch, mocker, capsys):
        user_input = iter(inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input))
        monkeypatch.setattr('builtins.print', lambda _: True)
        monkeypatch.setattr(maskpass, 'advpass', lambda _: 'test_password')

        mocker.patch('src.helpers.home_menu.get_item', return_value=None)

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            home_menu.login()
            capsys.readouterr()

        assert pytest_wrapped_e.type == SystemExit

    def test_login_wrong_password(self, monkeypatch, mocker, capsys):
        monkeypatch.setattr('builtins.input', lambda _: 'test_user')
        monkeypatch.setattr(maskpass, 'advpass', lambda _: 'test_password')
        mocker.patch('src.helpers.home_menu.get_item', return_value=['user'])

        mock_auth = Mock(spec=Authentication)
        _instance = mock_auth.return_value
        monkeypatch.setattr(_instance, 'login', lambda: None)

        mocker.patch('src.helpers.home_menu.Authentication', return_value=_instance)
        home_menu.login()
        captured = capsys.readouterr()
        lines = captured.out.split('\n')
        assert lines[1].strip() == "Wrong password! Please try again"

    def test_login_valid_login_admin(self, monkeypatch, mocker, capsys):
        monkeypatch.setattr('builtins.input', lambda _: 'test_user')
        monkeypatch.setattr(maskpass, 'advpass', lambda _: 'test_password')
        mocker.patch('src.helpers.home_menu.get_item', return_value=['admin'])

        mock_auth = Mock(spec=Authentication)
        _instance = mock_auth.return_value
        monkeypatch.setattr(_instance, 'login', lambda: True)

        mocker.patch('src.helpers.home_menu.Authentication', return_value=_instance)

        mock_admin_menu = mocker.patch('src.helpers.home_menu.admin_menu', return_value=True)

        home_menu.login()
        capsys.readouterr()

        mock_admin_menu.assert_called_once()

    def test_login_valid_login_visitor(self, monkeypatch, mocker, capsys):
        monkeypatch.setattr('builtins.input', lambda _: 'test_user')
        monkeypatch.setattr(maskpass, 'advpass', lambda _: 'test_password')
        mocker.patch('src.helpers.home_menu.get_item', return_value=['visitor'])

        mock_auth = Mock(spec=Authentication)
        _instance = mock_auth.return_value
        monkeypatch.setattr(_instance, 'login', lambda: True)

        mocker.patch('src.helpers.home_menu.Authentication', return_value=_instance)

        mock_visitor_menu = mocker.patch('src.helpers.home_menu.visitor_menu', return_value=True)

        home_menu.login()
        capsys.readouterr()

        mock_visitor_menu.assert_called_once()

    def test_login_valid_login_librarian(self, monkeypatch, mocker, capsys):
        monkeypatch.setattr('builtins.input', lambda _: 'test_user')
        monkeypatch.setattr(maskpass, 'advpass', lambda _: 'test_password')
        mocker.patch('src.helpers.home_menu.get_item', return_value=['librarian'])

        mock_auth = Mock(spec=Authentication)
        _instance = mock_auth.return_value
        monkeypatch.setattr(_instance, 'login', lambda: True)

        mocker.patch('src.helpers.home_menu.Authentication', return_value=_instance)

        mock_librarian_menu = mocker.patch('src.helpers.home_menu.librarian_menu', return_value=True)

        home_menu.login()
        capsys.readouterr()

        mock_librarian_menu.assert_called_once()
