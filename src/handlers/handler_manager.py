from typing import List

from websockets.server import WebSocketServerProtocol

from handlers.handlerbase import HandlerBase
from models.request import Request


class HandlerManager:
    def __init__(self):
        self.__handlers : List[HandlerBase] = []
    
    def add_handler(self, new_handler : HandlerBase):
        self.__handlers.append(new_handler)
    
    def run_handler(self, request: Request, connection : WebSocketServerProtocol):
        for handler in self.__handlers:
            if handler.can_handle(request):
                handler.handle(request, connection)