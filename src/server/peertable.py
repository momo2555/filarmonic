from typing import List
import json
import asyncio
import logging

from models.peer import Peer, PeerType
from models.request import Request


class PeerTable:
    def __init__(self) -> None:
        self.__peers : List[Peer] = []
        self.__log = logging.getLogger("Filarmonic")
    
    def add_peer(self, new_pper : Peer) -> None:
        self.__peers.append(new_pper)
    
    async def send_to_all(self, request : Request, peers : List[PeerType]):
        message = json.dumps(request.to_object())
        for peer in self.__peers:
            if peer.type in peers:
                #self.__log.info(f"peer {peer.type.name} message : {message}")
                if peer.connection.open:
                    await peer.connection.send(message)