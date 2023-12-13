import pytest
from unittest.mock import Mock, patch
from src.helpers import home_menu, take_input
from src.helpers.home_menu import maskpass


class TestHomeMenu:

    @pytest.mark.parametrize("choices", [('1', '2', '3')])
    def test_home(self, choices, monkeypatch, mocker):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))
        mock_login = mocker.patch('src.helpers.home_menu.login', return_value=True)
        mock_signup = mocker.patch('src.helpers.home_menu.signup', return_value=True)
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            home_menu.home()

        mock_login.assert_called()
        mock_signup.assert_called()
        assert pytest_wrapped_e.type == SystemExit

    @pytest.mark.parametrize("choices", [('5', '3')])
    def test_home_invalid(self, choices, monkeypatch, capsys):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))
        monkeypatch.setattr('builtins.print', lambda _: True)

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            res = home_menu.home()
            assert res is None

    def test_signup(self, mocker, capsys):
        mocker.patch.object(take_input, 'get_visitor_details', return_value=('test_name', 'test_email'))
        mock_user = Mock()
        mock_user.signup.return_value = True

        mocker.patch('src.helpers.home_menu.Authentication', return_value=mock_user)

        home_menu.signup()
        capsys.readouterr()

        mock_user.signup.assert_called_once()

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



