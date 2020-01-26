from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime
from src.code.environment.allbuildings import getEat


class Eat(IState):

    def __repr__(self):
        return 'Eating'

    def onStateEnter(self, entity):
        print(entity.name + ": " + "Time for lunch!")

    def onStateExecution(self, entity):

        if not entity.isClose(getEat().position):
            entity.move(getEat().position)
            return

        if entity.hunger <= 10:
            if entity.thirst >= 30:
                from .Drink import Drink
                state = Drink()
                entity.change(state)
            else:
                from .CollectMoney import CollectMoney
                entity.change(CollectMoney())
        else:
            entity.hunger -= 12 * GameTime.deltaTime
            entity.bank -= 3 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
