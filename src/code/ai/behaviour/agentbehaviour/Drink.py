from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime


class Drink(IState):

    def __repr__(self):
        return 'Drinking'

    def onStateEnter(self, entity):
        print(entity.name + ": " + "Need me a beavarage")

    def onStateExecution(self, entity):
        if entity.thirst <= 12:
            if entity.bank >= 120:
                from .Purchase import Purchase
                entity.change(Purchase())
            else:
                from .CollectMoney import CollectMoney
                entity.change(CollectMoney())
        else:
            entity.thirst -= 12 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
