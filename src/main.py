#!/usr/bin/env python
from multiprocessing import Process
import asyncio

from datagram.datagram_server import DatagramSocket
from server.game_server import GameServer
from process.process_manager import ProcessManager
from utils.log import ini_logger


if __name__ == "__main__":
    ini_logger()

    async def main():
        
        process = ProcessManager()
        datagram = DatagramSocket()
        server = GameServer()

        #run all processes
        await asyncio.gather(
            datagram.run_server(), 
            server.run_server(), 
            process.run_loop()
            )
    
    asyncio.run(main())
