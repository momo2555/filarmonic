from websockets.server import WebSocketServerProtocol

from handlers.handlerbase import HandlerBase
from models.request import Request, RequestType
from models.peer import PeerType
from server.peertable import PeerTable


class CloseGameHandler(HandlerBase):
    def __init__(self, peer_table : PeerTable):
        HandlerBase.__init__(self)
        self.peer_table = peer_table
    
    def can_handle(self, request: Request) -> bool:
        is_request = request.get_header_el("type") == RequestType.REQUEST
        is_close_game = request.get_request_action() == "closeGame"
        return is_request and is_close_game
    
    async def handle(self, request: Request, connection : WebSocketServerProtocol) -> None:
        self._log.info("Handle Start Game request")
        #What it should be
        # 1 - send a first request to spectacle -> start loading the game
        # 2 - if the game is not installed download it
        # 3 - launch the game
        # 4 - start the game (send a start request to spectacle and koppeliaApp) 
        #send the request back to spectacle
        await self.peer_table.send_to_all(request, [PeerType.SPECTACLE])