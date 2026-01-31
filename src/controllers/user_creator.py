from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface

class UserCreator:
    def __init__(self, users_repository: UsersRepositoryInterface): # Inverção da dependência - D SOLID
        self._users_repo = users_repository