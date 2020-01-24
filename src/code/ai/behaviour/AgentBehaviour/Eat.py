from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime


class Eat(IState):

    def onStateEnter(self, entity):
        print("Time for lunch!")

    def onStateExecution(self, entity):
        if entity.hunger <= 10:
            if entity.thirst >= 30:
                from .Drink import Drink
                state = Drink()
                entity.change(state)
            else:
                from .CollectMoney import CollectMoney
                state = CollectMoney("Pinchos", "Bartender")
                entity.change(state)
        else:
            entity.hunger -= 12 * GameTime.deltaTime
            entity.bank -= 3 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
