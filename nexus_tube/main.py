from models.video import Video
from models.user import User
from repositories.video_repository import VideoRepository
from repositories.user_repository import UserRepository
from services.video_service import VideoService
from services.user_service import UserService


def main():

    video_repo = VideoRepository()
    user_repo = UserRepository()

    video_service = VideoService(videoRepository=video_repo)
    UserService(userRepository=user_repo)

    video = Video(titulo="Bitcoin o ouro digital!")
    user1 = User(name="Marinaldo", email="marinaldo@dev.com", password="123")
    user2 = User(name="Satoshi", email="satoshi@dev.com", password="abc")

    video_repo.save(video)
    user_repo.save(user1)
    user_repo.save(user2)

    for _ in range(4):
        try:
            v, views = video_service.register_view(video_id=video.id)
            print(f"Vídeo Assistido: '{v.titulo}' - Total Views: {views}")
        except ValueError as e:
            print(f"Erro ao assistir: {e}")

    try:
        t_likes = video_service.register_like(video_id=video.id, user=user1)
        print(f"{user1.name} deu like! Total no vídeo: {t_likes}")

        t_likes = video_service.register_like(video_id=video.id, user=user1)
        print(f"{user1.name} tentou dar like de novo! Total no vídeo: {t_likes}")

        t_likes = video_service.register_like(video_id=video.id, user=user2)
        print(f"{user2.name} deu like! Total no vídeo: {t_likes}")

    except ValueError as e:
        print(f"Erro no Like: {e}")


if __name__ == "__main__":
    main()
