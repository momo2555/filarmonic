import socket
import logging
import json 
import asyncio
import psutil
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
            temp_sock = await asyncio.to_thread(socket.socket, socket.AF_INET, socket.SOCK_DGRAM)
            temp_sock.connect(("localhost", 2222))

            self.__log.info(f"host name : {self.get_ip()}")

            response = {
                "server" : True,
                "name" : "Koppelia de Momo",
                "ip" : self.get_ip(),
            }
            
            self.__server.sendto(json.dumps(response).encode(), (addr[0], 2223))

    def get_ip(self):
        interfaces = psutil.net_if_addrs()
        
        # Find the IPv4 address associated with the specified interface
        for itf in interfaces.keys():
            for addr in interfaces[itf]:
                if addr.family == socket.AF_INET and addr.address.split(".")[0]!="127":
                    return addr.address
