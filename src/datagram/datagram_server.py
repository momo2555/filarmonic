import socket
import logging
import json 
from io import StringIO


class DatagramSocket:
    def __init__(self):
        self.__log = logging.getLogger("Filarmonic")
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__server.bind(("", 2222))
        
    def run_server(self):
        print("run server")
        while True:
            msg = self.__server.recvfrom(200)
            self.__log.info(f"Received Datagram msg successful : {msg}")
            
            response = {
                "server" : True,
                "name" : "Koppelia de Momo",
                "ip" : socket.gethostname(),
            }
            
            self.__server.sendto(json.dumps(response).encode(), (msg[1][0], 2223))
