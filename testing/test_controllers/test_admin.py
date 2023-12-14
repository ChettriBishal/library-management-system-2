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
