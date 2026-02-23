import uuid

class User:
    def __init__(self,name:str, email:str, password:str, id:uuid=None):
        self.id = id if id is not None else uuid.uuid4()
        self.name = name
        self.email = email
        self.password = password


class UserRepository:
    def __init__(self, db:dict=None):
        self._db_user = db if db is not None else {}
    
    def save(self, user: User)-> User:
        if not user:
            print("Para salvar é preciso primeiro criar o usuário.")
            return None
        self._db_user[user.id] = user
    
    def profileUser(self, user:User)->User:
        if not user:
            print("Usuário não encontrado.")
            return None
        print(f"Nome: {user.name} - email: {user.email} - ID: {user.id}")
        

class Video:
    def __init__(self, titulo:str, views:int=0 ,id:uuid=None):
        self.id = id if id is not None else uuid.uuid4()
        self.titulo = titulo if titulo is not None else "Não é possível criar vídeo sem título."
        self.views = 0
        self.likes = set()
        
        
class VideoRepository:
    def __init__(self, db:dict=None):
        self._db = db if db is not None else {}
    
    def save(self, video: Video):
        if not video:
            print("Vídeo não enviado!")
            return
        self._db[video.id] = video
    
    def get_by_id(self, id:uuid.UUID)-> Video:
        if not id:
            print("Nenhum video solicitado!")
            return None
            
        video = self._db.get(id)
        
        if not video:
            print("Vídeo não encontrado na base de dados.")
            return None
    
        return video
    
    def get_all(self) -> list:
        if not self._db:
            print("Nenhuma base de dados localizada.")
            return []
        return list(self._db.values())


class VideoService:
    def __init__(self, videoRepository:VideoRepository):
        self.videoRepository = videoRepository
        
    def search_video(self, video_id):
        video = self.videoRepository.get_by_id(id=video_id)
        return video
    
    def CountViews(self, video: Video):
        video.views += 1
        save = self.videoRepository.save(video)
        return video.views
        
    def watchVideo(self, video_id):
        video = self.search_video(video_id=video_id)
        if video is None:
            print("Video não localizado.")
            return None
            
        views = self.CountViews(video)
        print(f"{video.titulo} - Views: {views}")
    
    def ActionLike(self, video_id, usuario: str):
        video = self.search_video(video_id=video_id)
        
        if video is None:
            return None
        video.likes.add(usuario)
        
        self.videoRepository.save(video)
        
        print(f"Total: {len(video.likes)}")
        return len(video.likes)

    def likesForProfile(self, user):
        if 

if __name__ == "__main__":
    
    video = Video(titulo="Bitcoin o ouro digital!")
    conn_db_repositoy = VideoRepository()
    user_service = VideoService(videoRepository=conn_db_repositoy)
    conn_db_repositoy.save(video)
    
    user_service.watchVideo(video_id=video.id)
    user_service.watchVideo(video_id=video.id)
    user_service.watchVideo(video_id=video.id)
    user_service.watchVideo(video_id=video.id)
    
    
    
    