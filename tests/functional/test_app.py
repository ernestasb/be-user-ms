"""
Test application general functionality.
"""

import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session
from src.database import db_session


def test_app_ok(client):
    # test app
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "user_data",
    [
        {
            "email": "test_user1@gmail.com",
            "password": "test_user_pw_1",
            "name": "test_user_1",
            "surname": "test_user_1",
        },
        {
            "email": "test_user2@gmail.com",
            "password": "test_user_pw_2",
            "name": "test_user_2",
            "surname": "test_user_2",
        },
        {
            "email": "test_user3@gmail.com",
            "password": "test_user_pw_3",
            "name": "test_user_3",
            "surname": "test_user_3",
        },
    ],
)
def test_database_error_offline(client_offline_db, user_data):
    # test postgress service down with user endpoint
    response = client_offline_db.post("/user", json=user_data)
    print(response.json())
    assert response.status_code == 503
