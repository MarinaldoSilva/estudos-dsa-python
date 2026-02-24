import uuid
from models.video import Video
from models.user import User
from repositories.video_repository import VideoRepository

class VideoService:
    def __init__(self, videoRepository: VideoRepository):
        self.videoRepository = videoRepository
        
    def search_video(self, video_id: uuid.UUID) -> Video:
        return self.videoRepository.get_by_id(id=video_id)
    
    def CountViews(self, video_id: uuid.UUID):
        if video_id is not None:
            video = self.search_video(video_id=video_id)
            if video:
                video.views += 1
                self.videoRepository.save(video)
                return video.views
        return None
        
    def watchVideo(self, video_id: uuid.UUID):
        video = self.search_video(video_id=video_id)
        if video is None:
            raise ValueError("Video não localizado.")
        
        views = self.CountViews(video_id=video.id)
        return video, views
    
    def ActionLike(self, video_id: uuid.UUID, usuario: User):
        video = self.search_video(video_id=video_id)
        
        if video is None:
            raise ValueError("Video não localizado. Impossível dar like.")
            
        video.likes.add(usuario)
        self.videoRepository.save(video)
        return len(video.likes)

    def likesForProfile(self, user: User):
        pass
