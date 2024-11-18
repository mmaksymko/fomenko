from config.singleton import Singleton
from model import db

class DatabaseSessionManager(metaclass=Singleton):
    def __init__(self):
        self.session = db.session