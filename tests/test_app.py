import pytest
from app import app

client = app.test_client()

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_empty_url():
    response = client.post(
        "/analyze",
        json={"url": ""}
    )

    assert response.status_code == 400

def test_invalid_url():
    response = client.post(
        "/analyze",
        json={"url": "abcd.invalid"}
    )

    assert response.status_code in [400, 408]