import datetime

from src.code.engine.Entity import Entity


class Message:

    @classmethod
    def sendConsole(cls, sender: Entity, msg: str):
        now = datetime.datetime.now()
        print('[' + now.ctime().__str__() + "] " + sender.name + ": " + msg)
