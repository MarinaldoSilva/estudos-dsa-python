import uuid
from models.video import Video


class VideoRepository:
    def __init__(self, db: dict = None):
        self._db = db if db is not None else {}

    def save(self, video: Video) -> Video:
        if not video:
            raise ValueError("Vídeo não enviado!")
        self._db[video.id] = video

    def get_by_id(self, id: uuid.UUID) -> Video:
        if not id:
            return None
        return self._db.get(id)

    def get_all(self) -> list:
        return list(self._db.values())
