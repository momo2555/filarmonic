import logging
from typing import Any, Coroutine

from process.processbase import ProcessBase
from models.game import Game
from services.downloader import Downloader
from services.gamerunner import GameRunner


class StartGameProcess(ProcessBase):
    def __init__(self, game: Game):
        super().__init__()

        self.__game : Game = game
        self._log = logging.getLogger("Filarmonic")
        self.__downloader = Downloader()
        self.__game_runner = GameRunner()
    
    async def run(self) -> Coroutine[Any, Any, None]:
        if not self.__game.is_downloaded():
            
            await self.__downloader.download_game(self.__game)
        if self.__game.is_downloaded():
            await self.__game_runner.run_game(self.__game)
        self._log.info("Game end")
        
        
    
    async def stop(self) -> Coroutine[Any, Any, None]:
        self._log.info("Stop functio is called : The game will end")
        await self.__game_runner.end_game()
        

    