import uuid


class User:
    def __init__(
        self,
        name: str,
        email: str,
        password: str,
        active: bool = True,
        id: uuid.UUID = None,
    ):
        self.id = id if id is not None else uuid.uuid4()
        self.likes_videos = set()
        self.name = name
        self.email = email
        self.active = active
        self.password = password
