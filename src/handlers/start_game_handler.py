import asyncio

from websockets.server import WebSocketServerProtocol

from handlers.handlerbase import HandlerBase
from models.request import Request, RequestType
from models.peer import PeerType
from models.game import Game
from server.peertable import PeerTable
from services.downloader import Downloader
from services.gamerunner import GameRunner


class StartGameHandler(HandlerBase):
    def __init__(self, peer_table : PeerTable):
        HandlerBase.__init__(self)
        self.peer_table = peer_table
    
    def can_handle(self, request: Request) -> bool:
        is_request = request.get_header_el("type") == RequestType.REQUEST
        is_launch_game = request.get_request_action() == "launchGame"
        return is_request and is_launch_game
    
    async def handle(self, request: Request, connection : WebSocketServerProtocol) -> None:
        self._log.info("Handle Start Game request")
        #What it should be
        # 1 - send a first request to spectacle -> start loading the game
        # 2 - if the game is not installed download it
        # 3 - launch the game
        # 4 - start the game (send a start request to spectacle and koppeliaApp) 
        #send the request back to spectacle
        game = Game(request.get_request_param("gameId"))
        game.set_url(request.get_request_param("gameUrl"))
        await self.peer_table.send_to_all(request, [PeerType.SPECTACLE])
        asyncio.create_task(self.run_game_task(game))
        

    async def run_game_task(self, game: Game):
        if not game.is_downloaded():
            downlader = Downloader()
            await downlader.download_game(game)
        if game.is_downloaded():
            game_runner = GameRunner()
            await game_runner.run_game(game)
        self._log.info("Game end")
