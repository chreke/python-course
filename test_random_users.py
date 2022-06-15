from unittest.mock import Mock

from random_users import random_users


def test_random_users(monkeypatch):
    mock = Mock()
    mock.return_value = [
        {"email": "tristan.hana@example.com",
         "dob": {"age": 43},
         "name": {"first": "Tristan", "last": "Hana"}}
    ]
    monkeypatch.setattr("random_users.get_random_users", mock)
    user = next(random_users())
    assert user.email == "tristan.hana@example.com"
