from fastapi.testclient import TestClient
from fastapi import HTTPException
import pytest
from src.fast_routes.user_router import user_route

client = TestClient(user_route)

from fastapi import HTTPException
from fastapi.testclient import TestClient
from unittest.mock import patch

#
# def test_login_user():
#     # Mocking the database function
#     with patch('src.models.database.get_item') as mock_get_item:
#         # Set up the mock return value for the database function
#         mock_get_item.return_value = {'username': 'test_user', 'password': 'test_password', 'role': 'user'}
#
#         # Create a test client
#         client = TestClient(user_route)
#
#         # Define test input data
#         test_data = {
#             'username': 'test_user',
#             'password': 'test_password',
#             'role': 'user'
#         }
#
#         # Send a request to the login endpoint
#         response = client.post('/login', json=test_data)
#
#         # Assert the response status code is 200 OK
#         assert response.status_code == 200
#
#         # Assert the response JSON contains the expected keys
#         assert 'access_token' in response.json()
#         assert 'token_type' in response.json()
#
#         # You can further assert the content of the response based on your requirements
#
#         # Reset the mock state
#         mock_get_item.reset_mock()


# Run the tests

def test_login_user_postive():
    user_data = {
        "username": "greater",
        "password": "Dummy@123#",
        "role": "visitor"
    }

    response = client.post("/login", json=user_data)

    assert response.status_code == 200

    assert "access_token" in response.json()
    assert "token_type" in response.json()


def test_login_user_negative():
    invalid_user_data = {
        "username": "unknown",
        "password": "Dummy@123#",
        "role": "visitor"
    }

    with pytest.raises(HTTPException) as exc:
        client.post("/login", json=invalid_user_data)

    assert exc.value.status_code == 404
