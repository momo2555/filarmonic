from typing import List
import json
import asyncio

from models.peer import Peer, PeerType
from models.request import Request


class PeerTable:
    def __init__(self) -> None:
        self.__peers : List[Peer] = []
    
    def add_peer(self, new_pper : Peer) -> None:
        self.__peers.append(new_pper)
    
    async def send_to_all(self, request : Request, peers : List[PeerType]):
        message = json.dumps(request.to_object())
        for peer in self.__peers:
            if peer.type in peers:
                await peer.connection.send(message)