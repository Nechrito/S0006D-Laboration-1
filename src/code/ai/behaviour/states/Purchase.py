from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime
from src.code.environment.AllBuildings import getStore
from ...messaging.Message import Message


class Purchase(IState):

    def __repr__(self):
        return 'Purchasing'

    def enter(self, entity):
        Message.sendConsole(entity, "Time to make use of my funds")

    def execute(self, entity):

        if not entity.isCloseTo(getStore().position):
            entity.moveTo(getStore().position)
            return

        if entity.hunger > 60:
            from .Eat import Eat
            entity.change(Eat())

        else:
            entity.bank -= 3 * GameTime.deltaTime
            entity.hunger += 1 * GameTime.deltaTime

    def exit(self, entity):
        pass
