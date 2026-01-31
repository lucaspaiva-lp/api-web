from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface

class UserFinder:
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repo = users_repository
        
    def find_by_name(self, name:str) -> dict:
        select_users = self.__select_and_validate_user(name)
        return self.__format_response(select_users)
    def __select_and_validate_user(self, name: str) -> list:
        select_users = self.__users_repo.select_user(name)
        if (not select_users or len(select_users) == 0):
            raise Exception("User is not registered!")
        
        return select_users
    
    def __format_response(self, select_users: list) -> dict:
        formatted_users = []
        for user in select_users:
            formatted_users.append({
                "id": user.id,
                "name": user.name,
                "age": user.age,
                "height": user.height
            })
            
        return {
            "type": "Users",
            "count": len(formatted_users),
            "attributes": formatted_users
        }
                                