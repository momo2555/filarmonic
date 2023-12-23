from handlerbase import HandlerBase
from server.peertable import PeerTable
from models.request import Request, RequestType


class IdentificationHandler(HandlerBase):
    def __init__(self, peer_table):
        HandlerBase.__init__(self)

    def handle(self, request : Request) -> None:
        self._log.info("Handle Identification request")
        

    def can_handle(self, request : Request) -> bool:
        is_id = request.get_header_el("type") == RequestType.IDENTIFICATION
        return is_id  