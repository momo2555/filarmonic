import asyncio
import logging
from asyncio.tasks import Task
from typing import List

from process.processbase import ProcessBase


class ProcessManager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProcessManager, cls).__new__(cls)
            cls.instance.__init_instance()
            #cls.instance.logger = logging.getLogger("fiebooth")
            #cls.instance.logger.info("INIT CONFIG -------------------------------------------------------------")
        return cls.instance

    def __init_instance(self):
        self.__queue : List[Task] = []
        self.__process : Task | None = None #current excecuted task
        self.__messager = asyncio.Queue()
        self.__log = logging.getLogger("Filarmonic")
    
    async def create_process(self, process : ProcessBase, force : bool = False):
        self.__queue.append(process)
        await self.__messager.put("createTask") 

    async def stop_current_process(self):
        await self.__messager.put("stopCurrentTask")
    
    def __process_message(self, message):
        self.__log.info(f"Exec message => {message}")
        match message:
            case "createTask":
                self.__start_next_task()
            case "stopCurrentTask":
                self.__process.cancel()
                self.__start_next_task()
            case "endTask":
                self.__start_next_task()
            case "stopTask":
                self.__start_next_task()
                

    def __start_next_task(self):
        if (self.__process is None or self.__process.done()) and len(self.__queue) > 0 :
            self.__log.info("Exec the next Task in the queue")
            to_run : ProcessBase = self.__queue.pop(0)
            self.__process = asyncio.create_task(to_run.exec_start_process(self.__messager))


    async def run_loop(self):
        self.__log.info("run process loop")
        while True:
            new_message = await self.__messager.get()
            self.__process_message(new_message)
            