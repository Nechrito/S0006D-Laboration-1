from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime


class Purchase(IState):

    def __repr__(self):
        return 'Purchasing'

    def onStateEnter(self, entity):
        print(entity.name + ": " + "Time to make use of this bank")

    def onStateExecution(self, entity):
        if entity.bank > 75:
            from .Hangout import Hangout
            entity.change(Hangout())

        elif entity.hunger > 60:
            from .Eat import Eat
            state = Eat()
            entity.change(state)

        else:
            entity.bank -= 7 * GameTime.deltaTime
            entity.hunger += 6 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
