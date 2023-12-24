from websockets.server import WebSocketServerProtocol

from handlers.handlerbase import HandlerBase
from models.request import Request
from server.peertable import PeerTable


class DataExchangeHandler(HandlerBase):
    def __init__(self, peet_table : PeerTable):
        HandlerBase.__init__(self)
        self.__peer_table = peet_table
    
    def can_handle(self, request: Request) -> bool:
        return super().can_handle(request)
    
    def handle(self, request: Request, connection : WebSocketServerProtocol) -> None:
        self._log.info("Handle Data Exchange request")
        self.__peer_table.send_to_all(request, [request.get_header_el("to")])
    