import uuid
from models.user import User
from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, userRepository: UserRepository):
        self.userRepository = userRepository

    def get_user_by_id(self, user_id: uuid.UUID) -> User:
        if not user_id:
            raise ValueError("Usuário não localizado")
        return self.userRepository.get_by_id(user_id=user_id)

    def get_user_likes_count(self, user: User) -> int:
        if not user:
            raise ValueError("Usuário não localizado")
        likes_user = len(user.likes_videos)
        return likes_user
