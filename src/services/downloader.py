import logging
from pathlib import Path
import zipfile
import asyncio

import requests
import aiohttp

from models.game import Game
from utils.file_utils import FileUtils


class Downloader:
    def __init__(self):
        self.__log = logging.getLogger("Filarmonic")
        pass

    async def download_game(self, game: Game):
        url = game.get_url()
        filename = Path(game.get_path().as_posix()+".zip")

        #download game
        response = requests.get(url, stream=True)
        async with aiohttp.ClientSession() as session:
            self.__log.info(f"Starting download file from {url}")
            async with session.get(url) as response:
                assert response.status == 200
                with open(filename, "wb") as f:
                    while True:
                        chunk = await response.content.readany()
                        if not chunk:
                            break
                        f.write(chunk)
                self.__log.info(f"End successful Downloaded {filename} from {url}")
        
        # Unzip the file
        self.__log.info(f"Start unzip file {filename}")
        with zipfile.ZipFile(filename, "r") as zip_ref:
            await asyncio.to_thread(zip_ref.extractall, FileUtils.get_game_folder())
        self.__log.info(f"file unzipped {filename} successful")
        
        game.update()