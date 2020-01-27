from ..IState import IState
from ....engine.GameTime import GameTime
from ....environment.allbuildings import getResturant


class Eat(IState):

    def __repr__(self):
        return 'Eating'

    def onStateEnter(self, entity):
        print(entity.name + ": " + "Time for lunch!")

    def onStateExecution(self, entity):

        if not entity.isClose(getResturant().position):
            entity.move(getResturant().position)
            return

        if entity.hunger <= 10:
            from .CollectMoney import CollectMoney
            entity.change(CollectMoney())
        else:
            entity.hunger -= 4 * GameTime.deltaTime
            entity.bank -= 0.40 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
