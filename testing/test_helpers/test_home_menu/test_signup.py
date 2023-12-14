from unittest.mock import Mock
from src.helpers import home_menu, take_input


class TestSignUp:
    def test_signup(self, mocker, capsys):
        mocker.patch.object(take_input, 'get_visitor_details', return_value=('test_name', 'test_email'))
        mock_user = Mock()
        mock_user.signup.return_value = True

        mocker.patch('src.helpers.home_menu.Authentication', return_value=mock_user)

        home_menu.signup()
        capsys.readouterr()

        mock_user.signup.assert_called_once()
