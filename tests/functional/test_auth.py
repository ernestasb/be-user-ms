import pytest

router_prefix = "/auth"


@pytest.mark.parametrize(
    "user_data",
    [
        {
            "email": "test_user1@gmail.com",
            "password": "test_user_pw_1",
        },
        {
            "email": "test_user2@gmail.com",
            "password": "test_user_pw_2",
        },
        {
            "email": "test_user3@gmail.com",
            "password": "test_user_pw_3",
        },
    ],
)
def test_login_ok(client, user_data, create_users):
    # test login
    response = client.post(router_prefix + "/login", json=user_data)
    assert response.status_code == 200
    assert response.json()["access_token"]


@pytest.mark.parametrize(
    "user_data",
    [
        {
            "email": "test_user1@gmail.com",
            "password": "test_user_pw_2",
        },
        {
            "email": "test_user2@gmail.com",
            "password": "test_user_pw_3",
        },
        {
            "email": "test_user3@gmail.com",
            "password": "test_user_pw_4",
        },
    ],
)
def test_login_bad_data(client, user_data, create_users):
    # test login with bad data
    response = client.post(router_prefix + "/login", json=user_data)
    assert response.status_code == 401
    print(response.json())
    assert response.json()["message"] == "Invalid credentials"


def test_auth_ok(client, valid_token):
    # test auth
    response = client.post(router_prefix, json={"access_token": valid_token})
    assert response.status_code == 200
    assert response.json()["message"] == "Authenticated"


def test_auth_expired_token(client, expired_token):
    # test expired token
    response = client.post(router_prefix, json={"access_token": expired_token})
    assert response.status_code == 401
    assert response.json()["message"] == "Token expired"


def test_auth_invalid_token(client):
    response = client.post(router_prefix, json={"access_token": "some_token"})
    assert response.status_code == 401
    assert response.json()["message"] == "Invalid token"
