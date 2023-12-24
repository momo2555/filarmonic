from server.peertable import PeerTable
from models.peer import Peer, PeerType
from models.request import Request, RequestType


class State():
    def __init__(self, peer_table):
        self.__game_state : dict = {}
        self.__peer_table : PeerTable = peer_table
    
    async def update_state(self, new_state : dict, spread : bool = True):
        self.__game_state = new_state
        state_request = Request()
        state_request.set_type(RequestType.REQUEST)
        state_request.set_request_action("changeState")
        state_request.create_param("state", self.__game_state)
        if spread:
            await self.__peer_table.send_to_all(state_request, [PeerType.MONITOR, PeerType.CONTROLLER])
