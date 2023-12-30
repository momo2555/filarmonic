import logging

import requests
import aiohttp

from models.game import Game


class Downloader:
    def __init__(self):
        self.__log = logging.getLogger("Filarmonic")
        pass

    async def download_game(self, game: Game):
        url = game.get_url()
        filename = game.get_path()

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
                self.__log.info(f"Downloaded {filename} from {url}")
        