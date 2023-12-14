import pytest
from src.helpers import home_menu


class TestHome:
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

        with pytest.raises(SystemExit):
            res = home_menu.home()
            assert res is None
