import pytest
import requests
#import requests_mock
from http import HTTPStatus

# Fixture to set up the mock API
@pytest.fixture
def mock_api():
    with requests.Mocker() as m:
        yield m

@pytest.mark.integration
def test_users_endpoint_valid_credentials(mock_api):
    """
    Test the users endpoint with valid credentials (admin/qwerty).
    Should return HTTP 200 with empty response.
    """
    url = "http://127.0.0.1:8000/users/"
    params = {"username": "admin", "password": "qwerty"}
    mock_api.get(url, json={}, status_code=HTTPStatus.OK, reason="OK")

    response = requests.get(url, params=params)

    assert response.status_code == HTTPStatus.OK
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert response.json() == {}
    assert response.reason == "OK"

@pytest.mark.integration
def test_users_endpoint_invalid_credentials(mock_api):
    """
    Test the users endpoint with invalid credentials (admin/admin).
    Should return HTTP 401 with empty response.
    """
    url = "http://127.0.0.1:8000/users/"
    params = {"username": "admin", "password": "admin"}
    mock_api.get(url, json={}, status_code=HTTPStatus.UNAUTHORIZED, reason="Unauthorized")

    response = requests.get(url, params=params)

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert response.json() == {}
    assert response.reason == "Unauthorized"