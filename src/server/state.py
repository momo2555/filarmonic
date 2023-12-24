from server.peertable import PeerTable
from models.peer import Peer, PeerType
from models.request import Request, RequestType


class State():
    def __init__(self, peer_table):
        self.__game_state : dict = {}
        self.__peer_table : PeerTable = peer_table
    
    def update_state(self, new_state : dict, spread : bool = True):
        state_request = Request()
        state_request.set_type(RequestType.REQUEST)
        state_request.set_request_action("changeState")
        state_request.create_param("state", self.__game_state)
        
        self.__peer_table.send_to_all(state_request, [PeerType.MONITOR, PeerType.CONTROLLER])
