from ..IState import IState
from ....engine.GameTime import GameTime
from ....environment.AllBuildings import getResturant
from ...messaging.Message import Message

class Eat(IState):

    def __repr__(self):
        return 'Eating'

    def enter(self, entity):
        Message.sendConsole(entity, "Time for lunch!")

    def execute(self, entity):

        if not entity.isCloseTo(getResturant().position):
            entity.moveTo(getResturant().position)
            return

        if entity.hunger <= 10:
            from .CollectMoney import CollectMoney
            entity.change(CollectMoney())
        else:
            entity.hunger -= 4 * GameTime.deltaTime
            entity.bank -= 0.40 * GameTime.deltaTime

    def exit(self, entity):
        pass
