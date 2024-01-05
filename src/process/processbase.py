import asyncio
import logging


class ProcessBase:
    def __init__(self):
        self._log = logging.getLogger("Filarmonic")        

    async def run(self) -> None:
        pass
    
    async def exec_start_process(self, signal : asyncio.Queue):

        try:
            await self.run()
            await signal.put("endTask")
        except asyncio.CancelledError as e:
            self._log.info("asyncio.CancelledError has been thrown. Stop Process")
            await self.exec_stop_task(signal)


    async def stop(self) -> None:
        pass

    async def exec_stop_task(self, signal : asyncio.Queue):
        self._log.info("Stop Callback will be called")
        await self.stop()
        await signal.put("stopTask")