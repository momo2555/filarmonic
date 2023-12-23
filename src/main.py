#!/usr/bin/env python
from multiprocessing import Process
import asyncio

from datagram.datagram_server import DatagramSocket
from server.game_server import GameServer
from utils.log import ini_logger


if __name__ == "__main__":
    ini_logger()

    async def main():
        
        datagram = DatagramSocket()
        server = GameServer()
        await asyncio.gather(datagram.run_server(), server.run_server())
    
    asyncio.run(main())
