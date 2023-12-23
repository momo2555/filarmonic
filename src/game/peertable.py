from typing import List

from models.peer import Peer


class PeerTable:
    def __init__(self) -> None:
        self.__peers : List[Peer] = []
    
    def add_peer(self, new_pper : Peer) -> None:
        self.__peers.append(new_pper)