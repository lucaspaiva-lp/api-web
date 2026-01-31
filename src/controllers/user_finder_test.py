import pytest
from src.models.entities.users import Users
from .user_finder import UserFinder

class UserRepositoryMock:
    def __init__(self):
        self.select_user_att = {}

    def select_user(self, name: str) -> list:
        self.select_user_att["name"] = name
        return [
            Users(
                id=123,
                name="tatu",
                age=42,
                height=3.20   
            )
        ]

class UserRepositoryMockWithError:
    def __init__(self):
        self.select_user_att = {}
    
    def select_user(self, name: str) -> list:
        self.select_user_att["name"] = name
        return[]

def test_find_by_name():
    name = "my_papa_name"
    user_repo = UserRepositoryMock()
    user_finder = UserFinder(user_repo)
    
    response = user_finder.find_by_name(name)
    print(response)
    print(user_repo.select_user_att)
    
    assert user_repo.select_user_att["name"] == name
    assert isinstance(response, dict)
    assert response["type"] == "Users"
    assert "attributes" in response
    assert isinstance(response["attributes"], list)
    
def test_find_by_name_with_error():
    user_repo = UserRepositoryMockWithError()
    user_finder = UserFinder(user_repo)
    
    with pytest.raises(Exception) as exc_info:
        user_finder.find_by_name("something")
        
    assert str(exc_info.value) == "User is not registered!"
    