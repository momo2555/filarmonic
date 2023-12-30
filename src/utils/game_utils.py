from pathlib import Path

from utils.file_utils import FileUtils


class GameUtils:
    @staticmethod
    def get_path_by_game_id(game_id : str) -> Path:
        p : Path = FileUtils.get_game_folder() / Path(game_id)
        return p
    
    @staticmethod
    def is_game_downloaded(game_id : str) -> bool:
        p : Path = GameUtils.get_path_by_game_id()
        return p.exists()
    
    

