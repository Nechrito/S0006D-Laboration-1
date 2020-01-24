from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime


class Drink(IState):

    def onStateEnter(self, entity):
        print("Need me a beavarage")

    def onStateExecution(self, entity):
        if entity.thirst <= 12:
            if entity.bank >= 120:
                from .Purchase import Purchase
                state = Purchase()
                entity.change(state)
            else:
                from .CollectMoney import CollectMoney
                state = CollectMoney("LTU", "Student")
                entity.change(state)
        else:
            entity.thirst -= 12 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
