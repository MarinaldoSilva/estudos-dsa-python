import uuid
from models.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, userRepository: UserRepository):
        self.userRepository = userRepository
        
    def search_user(self, user_id: uuid.UUID) -> User:
        if not user_id:
            raise ValueError("Usuário não informado")
        return self.userRepository.get_user_id(user_id=user_id)
