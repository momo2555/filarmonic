from handlers.handlerbase import HandlerBase
from websockets.server import WebSocketServerProtocol

from models.request import Request, RequestType
from server.state import State
from server.peertable import PeerTable


class StateHandler(HandlerBase):
    def __init__(self, state : State):
        HandlerBase.__init__(self)
        self.__state = state
    
    def can_handle(self, request: Request) -> bool:
        is_request = request.get_header_el("type") == RequestType.REQUEST
        is_change_state = request.get_request_action() == "changeState"
        return is_request and is_change_state
    
    def handle(self, request: Request, connection : WebSocketServerProtocol) -> None:
        self._log.info("Handle State request")
        new_state = request.get_request_param("state")
        self.__state.update_state(new_state)


    