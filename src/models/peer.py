from enum import Enum

from websockets.server import WebSocketServerProtocol

from models.address import Address


class PeerType(Enum):
    MONITOR = "monitor"
    CONTROLLER = "controller"
    DEVICE = "device"
    SPECTACLE = "spectacle"
    KOPPELIA = "koppelia"
    NONE = "none"

class ConnectionState(Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"


class Peer:
    type : PeerType = PeerType.NONE
    name : str = ""
    connection : WebSocketServerProtocol
    state : ConnectionState
    address : Address
    def set_type_from_string(self, str_type : str):
        if str_type in PeerType._value2member_map_.keys():
            self.type = PeerType._value2member_map_[str_type]
        else: 
            type = PeerType.NONE

