from pathlib import Path
import os
import shutil

from errors import KoppeliaRepertoryNotExist


class FileUtils:
    @staticmethod
    def get_koppelia_folder() -> Path:
        p = Path('/koppelia')
        if not p.exists():
            KoppeliaRepertoryNotExist("The Koppelia repertory doese not exist, please create it and grant access")
        else:
            return p

    @staticmethod 
    def get_config_file() -> Path:
        config_folder = FileUtils.get_koppelia_folder() / Path("config")
        if not config_folder.exists():
            os.mkdir(config_folder)
        config_file = config_folder / Path("config.yaml")
        if not Path(config_file).exists():
            shutil.copyfile(Path("config/config.yaml"), config_file)
        return config_file

    @staticmethod
    def get_game_folder() -> Path:
        p = FileUtils.get_koppelia_folder() / Path("games")
        if not p.exists():
            os.mkdir(p)
        return p