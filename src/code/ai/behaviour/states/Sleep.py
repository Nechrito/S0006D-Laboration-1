from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime
from src.code.environment.AllBuildings import getHotel
from ...messaging.Message import Message

class Sleep(IState):

    def __repr__(self):
        return 'Sleeping'

    def enter(self, entity):
        Message.sendConsole(entity, "ZzzZz...")

    def execute(self, entity):

        if not entity.isCloseTo(getHotel().position):
            entity.moveTo(getHotel().position)
            return

        if entity.fatigue <= 10:
            from .Eat import Eat
            entity.change(Eat())
        else:
            entity.fatigue -= 7 * GameTime.deltaTime

    def exit(self, entity):
        pass

