import pytest
from src.models.connection.db_connection_handler import DbConnectionHandler
from .users_repository import UsersRepository

@pytest.mark.skip(reason="Insert in DB")
def test_users_repository():
    db_conn = DbConnectionHandler()
    users_repo = UsersRepository(db_conn)
    
    name = "Test name"
    age = 100
    height = 1.85
    
    users_repo.insert_user(name, age, height)
    users = users_repo.select_user(name)

    assert isinstance(users, list)
    assert len(users) >= 1
    assert users[0].name == name
    assert users[0].age == age
    assert users[0].height == height
