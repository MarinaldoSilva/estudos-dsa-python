import uuid
from models.user import User


class UserRepository:
    def __init__(self, db: dict = None):
        self._db_user = db if db is not None else {}

    def save(self, user: User) -> User:
        if not user:
            raise ValueError("Para salvar é preciso primeiro criar o usuário.")
        self._db_user[user.id] = user
        return user

    def get_by_id(self, user_id: uuid.UUID) -> User:
        if not user_id:
            raise ValueError("Usuário não encontrado (ID vazio).")
        return self._db_user.get(user_id)
