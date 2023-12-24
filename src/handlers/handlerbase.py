import logging

from websockets.server import WebSocketServerProtocol

from models.request import Request


class HandlerBase:
    def __init__(self):
        self._log = logging.getLogger("Filarmonic")

    def can_handle(self, request : Request) -> bool:
        return False
    
    def handle(self, request : Request, connection : WebSocketServerProtocol) -> None:
        return None