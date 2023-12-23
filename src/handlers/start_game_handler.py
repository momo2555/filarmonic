from websockets.server import WebSocketServerProtocol

from handlerbase import HandlerBase
from models.request import Request


class StartGameHandler(HandlerBase):
    def __init__(self):
        HandlerBase.__init__(self)
    
    def can_handle(self, request: Request, connection : WebSocketServerProtocol) -> bool:
        return super().can_handle(request)
    
    def handle(self, request: Request) -> None:
        self._log.info("Handle Start Game request")