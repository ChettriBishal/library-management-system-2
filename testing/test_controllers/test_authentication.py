import pytest
from unittest.mock import patch, Mock
from src.controllers import authentication
from src.controllers.authentication import Authentication, checkpw, generate_uuid


class TestAuthentication:

    @pytest.fixture
    def mock_get_item(self, mocker):
        return mocker.patch('src.controllers.authentication.get_item')

    @pytest.fixture
    def mock_logger(self, mocker):
        return mocker.patch('src.controllers.authentication.Authentication.log_obj')

    def test_sign_up_invalid(self, capsys, mock_get_item):
        mock_get_item.return_value = True  # already exists with that name

        test_auth = Authentication("test_user", "123", "user")
        test_auth.signup()

        captured = capsys.readouterr()

        assert captured.out.strip() == "Choose a different username!"

    @patch('src.controllers.authentication.insert_item')
    def test_sign_up_valid(self, mock_insert_item, monkeypatch, mocker, mock_get_item, mock_logger):
        mock_get_item.return_value = None  # no one with that username exists

        test_auth = Authentication("test_user", "123", "user")
        test_auth.signup()
        mocker.patch.object(test_auth, '_hash_password', return_value='12312312')

        mock_insert_item.return_value = True

        mock_insert_item.assert_called_once()

    def test_login_no_user(self, capsys, mock_get_item):
        mock_get_item.return_value = None

        test_auth = Authentication("test_user", "123", "user")
        test_auth.login()

        captured = capsys.readouterr()

        assert captured.out.strip() == "User with username `test_user` does not exist!"

    def test_login_valid_user(self, capsys, mocker, mock_get_item):
        check_user = ["test_user", "user", "!##!@@!"]
        mock_get_item.return_value = check_user

        test_auth = Authentication("test_user", "123", "user")
        mocker.patch.object(test_auth, '_check_password', return_value=True)

        res = test_auth.login()
        capsys.readouterr()

        assert res == check_user

    def test_login_wrong_password(self, capsys, mocker, mock_get_item):
        check_user = ["test_user", "user", "!##!@@!"]
        mock_get_item.return_value = check_user

        test_auth = Authentication("test_user", "123", "user")
        mocker.patch.object(test_auth, '_check_password', return_value=False)

        res = test_auth.login()
        capsys.readouterr()

        assert res is None

    @pytest.mark.parametrize("res", [True, False])
    def test_check_password(self, res, monkeypatch):
        test_auth = Authentication("test_user", "123", "user")

        with patch('src.controllers.authentication.checkpw', return_value=res):
            res = test_auth._check_password('1231322@@')
            assert res is res
