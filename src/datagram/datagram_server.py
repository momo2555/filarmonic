import socket


class DatagramSocket:
    def __init__(self):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__server.bind(("0.0.0.0", 2222))
        
    def run_server(self):
        print("run server")
        while True:
            msg = self.__server.recvfrom(1024)
            print("Received msg", msg)