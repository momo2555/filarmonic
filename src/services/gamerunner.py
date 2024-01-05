from pathlib import Path
import logging
import asyncio

from models.game import Game


class GameRunner:
    def __init__(self):
        self.__process = None
        self.__log = logging.getLogger("Filarmonic")
        

    async def run_game(self, game: Game):
        working_dir : Path = game.get_path()
        entry_point : Path = working_dir / Path("index.js")
        cmd = f"node {entry_point}"
        
        self.__process = await asyncio.create_subprocess_shell(cmd, cwd=working_dir)
        await self.__process.wait()
    
    async def  end_game(self):
        if not self.__process is None:
            self.__log.info("Game Runner is killing the game !")
            self.__process.kill()
            self.__process = None
        
