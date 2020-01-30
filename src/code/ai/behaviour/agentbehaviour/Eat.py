from ..IState import IState
from ....engine.GameTime import GameTime
from ....environment.allbuildings import getResturant
from ...messaging.message import Message

class Eat(IState):

    def __repr__(self):
        return 'Eating'

    def onStateEnter(self, entity):
        Message.sendConsole(entity, "Time for lunch!")

    def onStateExecution(self, entity):

        if not entity.isCloseTo(getResturant().position):
            entity.moveTo(getResturant().position)
            return

        if entity.hunger <= 10:
            from .CollectMoney import CollectMoney
            entity.change(CollectMoney())
        else:
            entity.hunger -= 4 * GameTime.deltaTime
            entity.bank -= 0.40 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
