from fastapi.testclient import TestClient
from src.fastapp import app

client = TestClient(app)


def test_server():
    response = client.get(url="/")
    assert response.status_code == 200
    assert response.json() == {"message": "Server is running"}
