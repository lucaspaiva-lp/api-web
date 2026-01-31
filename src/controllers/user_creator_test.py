import pytest
from src.controllers.user_creator import UserCreator

class UserRepositoryMock:
    def __init__(self):
        self.select_user_att = {}
        self.insert_user_att = {}

    def select_user(self, name: str) -> list:
        self.select_user_att["name"] = name
        return []

    def insert_user(self, name: str, age: int, height: float) -> None:
        self.insert_user_att["name"] = name
        self.insert_user_att["age"] = age
        self.insert_user_att["height"] = height


class UserRepositoryMockWithError:
    def __init__(self):
        self.select_user_att = {}
    
    def select_user(self, name: str) -> list:
        self.select_user_att["name"] = name
        return [1, 2, 3]
    
def test_insert_new_user():
    user_repository = UserRepositoryMock()
    user_creator = UserCreator(user_repository)

    name = "My name"
    age = 42
    height = 1.80

    response = user_creator.insert_new_user(name, age, height)

    assert isinstance(response, dict)
    assert "type" in response
    assert response["count"] == 1
    assert response["message"] == "User is not registered!"

def test_insert_new_user_with_error():
    user_repository = UserRepositoryMockWithError()
    user_creator = UserCreator(user_repository)
    
    with pytest.raises(Exception) as exc_info:
        user_creator.insert_new_user("something", 42, 1.11)
    assert str(exc_info.value) == "User is not registered!"
        