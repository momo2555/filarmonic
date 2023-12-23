from websockets.server import serve, WebSocketServerProtocol
import asyncio

from handlers.handler_manager import HandlerManager
from models.request import Request


class GameServer:
    def __init__(self):
        self.__handler_manager : HandlerManager = HandlerManager()
        
    
    async def __receive_socket_handler(self, websocket : WebSocketServerProtocol):
        async for message in websocket:
            received_request : Request = Request()
            received_request.from_json(message)
            self.__handler_manager.run_handler()

    async def __entrypoint(self):
        async with serve(self.__receive_socket_handler, "0.0.0.0", 2225):
            await asyncio.Future()
        

    def run_server(self):
        asyncio.run(self.__entrypoint)