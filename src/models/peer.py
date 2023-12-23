from enum import Enum

from websockets.server import WebSocketServerProtocol

from models.address import Address


class PeerType(Enum):
    MONITOR = "monitor"
    CONTROLLER = "controller"
    DEVICE = " device"
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