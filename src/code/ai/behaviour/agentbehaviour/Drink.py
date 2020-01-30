from ..IState import IState
from ...messaging.message import Message
from ....engine.GameTime import GameTime
from ....environment.allbuildings import getDrink


class Drink(IState):

    def __repr__(self):
        return 'Drinking'

    def onStateEnter(self, entity):
        Message.sendConsole(entity, "Need me a beavarage")

    def onStateExecution(self, entity):

        if not entity.isCloseTo(getDrink().position):
            entity.moveTo(getDrink().position)
            return

        if entity.thirst <= 8:
            entity.revertState()
        else:
            entity.thirst -= 5 * GameTime.deltaTime
            entity.bank -= 0.30 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
