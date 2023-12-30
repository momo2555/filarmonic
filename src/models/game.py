from pathlib import Path

from utils.game_utils import GameUtils


class Game:
    def __init__(self, id):
        self.__id = id
        self.__name = ""
        self.__url = ""
        self.__path = GameUtils.get_path_by_game_id(self.__id)
        self.__downloaded = GameUtils.is_game_downloaded(self.__id)
    
    def get_path(self) -> Path:
        return self.__path
    
    def is_downloaded(self) -> bool:
        return self.__downloaded
    
    def set_url(self, url):
        self.__url = url
    
    def get_url(self):
        return self.__url
    
