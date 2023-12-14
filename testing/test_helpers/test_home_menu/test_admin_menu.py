import pytest
from unittest.mock import Mock

from src.helpers.home_menu import admin_menu, maskpass


class TestAdminMenu:
    @pytest.fixture
    def mock_admin(self):
        mock_class = Mock()
        _instance = mock_class.return_value
        _instance.register_librarian.return_value = True
        _instance.list_users.return_value = True
        _instance.remove_user.return_value = True

        return _instance

    @pytest.mark.parametrize('choices', [('1', 'test_user', '2', '4')])
    def test_choice_1(self, choices, mock_admin, monkeypatch):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        monkeypatch.setattr(maskpass, 'advpass', lambda _: 'test_password')

        admin_menu(mock_admin)

        mock_admin.register_librarian.assert_called_once()

    @pytest.mark.parametrize('choices', [('3', 'test_user', '4')])
    def test_choice_3(self, choices, mock_admin, monkeypatch):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        monkeypatch.setattr(maskpass, 'advpass', lambda _: 'test_password')

        admin_menu(mock_admin)

        mock_admin.remove_user.assert_called_once()

    @pytest.mark.parametrize('choices', [('5', '4')])
    def test_choice_invalid(self, choices, capsys, mock_admin, monkeypatch):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        admin_menu(mock_admin)
        captured = capsys.readouterr()
        assert captured.out.strip() == "Invalid choice!"



