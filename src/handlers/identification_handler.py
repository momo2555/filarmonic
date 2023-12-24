from websockets.server import WebSocketServerProtocol

from handlers.handlerbase import HandlerBase
from server.peertable import PeerTable
from models.peer import Peer, PeerType
from models.request import Request, RequestType


class IdentificationHandler(HandlerBase):
    def __init__(self, peer_table: PeerTable):
        HandlerBase.__init__(self)
        self.__peer_table : PeerTable = peer_table

    def handle(self, request : Request, connection : WebSocketServerProtocol) -> None:
        self._log.info("Handle Identification request")
        new_peer : Peer = Peer()
        new_peer.connection = connection
        new_peer.type = request.get_header_el("from")
        self.__peer_table.add_peer(new_peer)


    def can_handle(self, request : Request) -> bool:
        is_id = request.get_header_el("type") == RequestType.IDENTIFICATION
        return is_id  