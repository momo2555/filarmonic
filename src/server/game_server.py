import asyncio
import logging

from websockets.server import serve, WebSocketServerProtocol

from handlers.handler_manager import HandlerManager
from models.request import Request
from server.peertable import PeerTable


class GameServer:
    def __init__(self):
        self.__handler_manager : HandlerManager = HandlerManager()
        self.__peer_table : PeerTable = PeerTable()
        self.__log = logging.getLogger("Filarmonic")
        
    async def __receive_socket_handler(self, websocket : WebSocketServerProtocol):
        async for message in websocket:
            received_request : Request = Request()
            self.__log.info(f"Received new message : {message}")
            received_request.from_json(message)
            self.__handler_manager.run_handler(received_request)

    async def __entrypoint(self):
        self.__log.info("run game server")
        async with serve(self.__receive_socket_handler, "0.0.0.0", 2225):
            await asyncio.Future()
        

    async def run_server(self):
        await self.__entrypoint()