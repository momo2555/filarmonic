#!/usr/bin/env python
from multiprocessing import Process

from datagram.datagram_server import DatagramSocket
from utils.log import ini_logger


if __name__ == "__main__":
    ini_logger()
    detection = DatagramSocket()
    detection.run_server()
    Process(target=detection.run_server(), args=(), deamon=True)
