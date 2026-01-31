from src.models.connection.db_connection_handler import DbConnectionHandler
from src.models.entities.users import Users
class UsersRepository:
    def __init__(self, db_conn_handler: DbConnectionHandler):
        self.__db_conn_handler = db_conn_handler
        
    def insert_user(self, name: str, age: int, height: float) -> None:
        with self.__db_conn_handler as database:
            try:
                new_user = Users(
                    name=name,
                    age=age,
                    height=height        
                )
                database.session.add(new_user)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def select_user(self, name: str) -> list[Users]:
        with self.__db_conn_handler as database:
            users = (
                database.session
                    .query(Users)
                    .filter(Users.name == name)
                    .all()
            )
            return users