import socket
import logging
import json 
import asyncio
from io import StringIO


class DatagramSocket:
    def __init__(self):
        self.__log = logging.getLogger("Filarmonic")
        self.__server = None
    
    
    async def run_server(self):
        self.__server = await asyncio.to_thread(socket.socket, socket.AF_INET, socket.SOCK_DGRAM)
        self.__server.bind(("", 2222))
        self.__log.info("run datagram server")
        while True:
            data, addr = await asyncio.to_thread(self.__server.recvfrom, 200)
            self.__log.info(f"Received Datagram msg successful : {(data, addr)}")
            
            response = {
                "server" : True,
                "name" : "Koppelia de Momo",
                "ip" : socket.gethostname(),
            }
            
            self.__server.sendto(json.dumps(response).encode(), (addr[0], 2223))
