import pytest
from unittest.mock import patch, Mock, MagicMock
from src.controllers.user import Admin


class TestAdmin:
    @pytest.fixture
    def admin_obj(self):
        obj = Admin('test_user', 'test_password', 'admin')
        return obj

    @patch('src.controllers.user.Authentication')
    def test_register_librarian(self, mock_auth, admin_obj, capsys):
        lib_obj = mock_auth.return_value
        lib_obj.signup.return_value = True

        admin_obj.register_librarian('test_user', 't_pass')
        capsys.readouterr()

        lib_obj.signup.assert_called()

    @patch('src.controllers.user.get_many_items')
    @patch('src.controllers.user.User', return_value=Mock())
    def test_list_users(self, mock_user, mock_get_many_items, admin_obj):
        mock_get_many_items.return_value = [('t_1', 't_1_2'), ('t_2', 't_2_1')]
        _obj = mock_user()
        _obj.user_details.return_value = True

        admin_obj.list_users()

        _obj.user_details.assert_called()
