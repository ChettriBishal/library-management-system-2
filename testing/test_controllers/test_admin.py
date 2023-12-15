import pytest
from unittest.mock import patch, Mock
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
    def test_list_users(self, mock_user, mock_get_many_items, admin_obj, capsys):
        mock_get_many_items.return_value = [('t_1', 't_1_2'), ('t_2', 't_2_1')]
        _obj = mock_user()
        _obj.user_details.return_value = True

        admin_obj.list_users()
        capsys.readouterr()

        _obj.user_details.assert_called()

    @patch('src.controllers.user.get_item', return_value=True)
    @patch('src.controllers.user.remove_item')
    def test_remove_user_valid(self, mock_remove_item, mock_get_item, admin_obj, capsys):
        admin_obj.remove_user('test_user')
        capsys.readouterr()
        mock_remove_item.assert_called_once()

    @patch('src.controllers.user.get_item', return_value=None)
    @patch('src.controllers.user.remove_item')
    def test_remove_user_invalid(self, mock_remove_item, mock_get_item, admin_obj, capsys):
        admin_obj.remove_user('test_user')
        captured = capsys.readouterr()

        assert captured.out.strip() == "User with username `test_user` doesn't exist!!"
        mock_remove_item.assert_not_called()
