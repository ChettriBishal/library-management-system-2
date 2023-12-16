from src.helpers import validation


class TestValidation:
    def test_validate_username_invalid(self):
        username = '#@!@#@'  # which is invalid
        res = validation.validate_username(username)

        assert not res

    def test_validate_username_valid(self):
        username = 'test_123'
        res = validation.validate_username(username)

        assert res

    def test_validate_password_invalid(self):
        password = '12312'
        res = validation.validate_password(password)

        assert not res

    def test_validate_password_valid(self):
        password = 'StrongPassword@1231*'
        res = validation.validate_password(password)

        assert res

