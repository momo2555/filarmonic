from pathlib import Path
import subprocess
import asyncio

from models.game import Game


class GameRunner:
    def __init__(self):
        self.process = None
        

    async def run_game(self, game: Game):
        working_dir : Path = game.get_path()
        entry_point : Path = working_dir / Path("index.js")
        cmd = f"node {entry_point}"
        
        self.process = await asyncio.create_subprocess_shell(cmd, cwd=working_dir)
        await self.process.wait()
    
    async def  end_game(self):
        if not self.process is None:
            self.process.kill()
        
