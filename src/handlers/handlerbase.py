from models.request import Request


class HandlerBase:
    def __init__(self):
        pass

    def can_handle(self, request) -> bool:
        return False
    
    def handle(self, request) -> None:
        return None