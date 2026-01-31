from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface

class UserCreator:
    def __init__(self, users_repository: UsersRepositoryInterface): # Inverção da dependência - D SOLID
        self.__users_repo = users_repository

    def insert_new_user(self, name: str, age: int, height: float) -> dict:
        self.__check_if_user_exists(name)
        self.__create_new_user(name, age, height)
        return self.__format_response()
    
    def __check_if_user_exists(self, name: str) -> None:
        select_users = self.__users_repo.select_user(name)
        if (not select_users or len(select_users) == 0):
            return
        
        raise Exception("Signed User!")
    
    def __create_new_user(self, name: str, age: int, height: float) -> None:
        #Others Activates necessary (optional)
        self.__users_repo.insert_user(name, age, height)
        
    def __format_response(self) -> dict:
        return {
            "type": "Users",
            "count": 1,
            "message": "Signed user!"
        }