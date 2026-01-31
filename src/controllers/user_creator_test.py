from src.controllers.user_creator import UserCreator

class UserRepositoryMock:
    def __init__(self):
        self.select_user_att = {}
        self.insert_user_att = {}

    def select_user(self, name: str) -> list:
        return [self.insert_user_att] if self.insert_user_att else []

    def insert_user(self, name: str, age: int, height: float) -> None:
        self.insert_user_att["name"] = name
        self.insert_user_att["age"] = age
        self.insert_user_att["height"] = height
        return

def test_insert_new_user():
    user_repository = UserRepositoryMock()
    user_creator = UserCreator(user_repository)

    name = "My name"
    age = 42
    height = 1.80

    response = user_creator.insert_new_user(name, age, height)

    users = user_repository.select_user(name)
    assert users[0]["name"] == name

    assert isinstance(response, dict)
    assert "type" in response
    assert response["count"] == 1
    assert response["message"] == "Signed user!"
