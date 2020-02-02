from datetime import datetime, timedelta

from src.code.engine.Entity import Entity
from src.code.engine.GameTime import GameTime


class Message:

    @classmethod
    def sendConsole(cls, sender: Entity, msg: str):
        #now = datetime.datetime.now()
        #print('[' + now.ctime().__str__() + "] " + sender.name + ": " + msg)
        print('[' + GameTime.timeElapsed() + "] " + sender.name + ": " + msg)
