from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime
from src.code.environment.allbuildings import getHotel
from ...messaging.message import Message

class Sleep(IState):

    def __repr__(self):
        return 'Sleeping'

    def onStateEnter(self, entity):
        Message.sendConsole(entity, "ZzzZz...")

    def onStateExecution(self, entity):

        if not entity.isCloseTo(getHotel().position):
            entity.moveTo(getHotel().position)
            return

        if entity.fatigue <= 10:
            from .Eat import Eat
            entity.change(Eat())
        else:
            entity.fatigue -= 7 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass

