import uuid
from models.video import Video
from models.user import User
from repositories.video_repository import VideoRepository


class VideoService:
    def __init__(self, videoRepository: VideoRepository):
        self.videoRepository = videoRepository

    def get_video_by_id(self, video_id: uuid.UUID) -> Video:
        return self.videoRepository.get_by_id(id=video_id)

    def register_view(self, video_id: uuid.UUID) -> int:
        video = self.get_video_by_id(video_id=video_id)
        if video is None:
            raise ValueError("Video não localizado.")
        video.views += 1
        self.videoRepository.save(video)
        return video.views

    def register_like(self, video_id: uuid.UUID, user: User) -> int:
        video = self.get_video_by_id(video_id=video_id)

        if video is None:
            raise ValueError("Video não localizado. Impossível dar like.")

        video.likes.add((user.id, user.name, user.email))
        user.likes_videos.add((video.id, video.titulo))

        self.videoRepository.save(video)
        return len(video.likes)

    def get_top_liked_videos(self, limit: int = 10) -> list[Video]:
        all_videos = self.videoRepository.get_all()
        ranking = sorted(all_videos, key=lambda v: len(v.likes), reverse=True)
        return ranking[:limit]
