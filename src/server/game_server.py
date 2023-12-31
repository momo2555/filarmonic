import asyncio
import logging

from websockets.server import serve, WebSocketServerProtocol

from handlers.handler_manager import HandlerManager
from handlers.data_exchange_handler import DataExchangeHandler
from handlers.identification_handler import IdentificationHandler
from handlers.state_handler import StateHandler
from handlers.start_game_handler import StartGameHandler
from handlers.close_game_handler import CloseGameHandler
from models.request import Request
from server.peertable import PeerTable
from server.state import State


class GameServer:
    def __init__(self):
        self.__handler_manager : HandlerManager = HandlerManager()
        self.__peer_table : PeerTable = PeerTable()
        self.__state : State = State(self.__peer_table)
        self.__log = logging.getLogger("Filarmonic")
        self.__init_handlers()
    
    def __init_handlers(self):
        data_exchange_handler = DataExchangeHandler(self.__peer_table)
        Identification_handler = IdentificationHandler(self.__peer_table)
        state_handler = StateHandler(self.__state)
        start_game_handler = StartGameHandler(self.__peer_table)
        close_game_handler = CloseGameHandler(self.__peer_table)
        self.__handler_manager.add_handler(data_exchange_handler)
        self.__handler_manager.add_handler(Identification_handler)
        self.__handler_manager.add_handler(state_handler)
        self.__handler_manager.add_handler(start_game_handler)
        self.__handler_manager.add_handler(close_game_handler)

    async def __receive_socket_handler(self, websocket : WebSocketServerProtocol):
        async for message in websocket:
            received_request : Request = Request()
            self.__log.info(f"Received new message : {message}")
            received_request.from_json(message)
            await self.__handler_manager.run_handler(received_request, websocket)

    async def __entrypoint(self):
        self.__log.info("run game server")
        async with serve(self.__receive_socket_handler, "0.0.0.0", 2225):
            await asyncio.Future()
        

    async def run_server(self):
        await self.__entrypoint()