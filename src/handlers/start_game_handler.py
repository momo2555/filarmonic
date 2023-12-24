from websockets.server import WebSocketServerProtocol

from handlers.handlerbase import HandlerBase
from models.request import Request


class StartGameHandler(HandlerBase):
    def __init__(self):
        HandlerBase.__init__(self)
    
    def can_handle(self, request: Request) -> bool:
        return super().can_handle(request)
    
    async def handle(self, request: Request, connection : WebSocketServerProtocol) -> None:
        self._log.info("Handle Start Game request")