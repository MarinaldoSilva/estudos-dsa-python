import uuid

class Video:
    def __init__(self, titulo: str, views: int = 0, id: uuid.UUID = None):
        self.id = id if id is not None else uuid.uuid4()
        self.titulo = titulo if titulo is not None else "Não é possível criar vídeo sem título."
        self.views = 0
        self.likes = set()
