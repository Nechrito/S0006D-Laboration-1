from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime
from src.code.environment.allbuildings import getStore


class Purchase(IState):

    def __repr__(self):
        return 'Purchasing'

    def onStateEnter(self, entity):
        print(entity.name + ": " + "Time to make use of this bank")

    def onStateExecution(self, entity):

        if not entity.isClose(getStore().position):
            entity.move(getStore().position)
            return

        if entity.hunger > 60:
            from .Eat import Eat
            entity.change(Eat())

        else:
            entity.bank -= 3 * GameTime.deltaTime
            entity.hunger += 1 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
