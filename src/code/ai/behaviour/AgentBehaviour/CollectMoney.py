import sys

from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime


class CollectMoney(IState):

    def __init__(self, location, workplaceName):
        self.location = location
        self.workplace = workplaceName

    def onStateEnter(self, entity):
        print("Time to start working at " + self.location + " as " + self.workplace)

    def onStateExecution(self, entity):
        if entity.fatigue >= 70:
            from .Sleep import Sleep
            state = Sleep()
            entity.change(state)

        elif entity.bank > 90:
            from .Purchase import Purchase
            state = Purchase()
            entity.change(state)

        else:
            entity.fatigue += 8 * GameTime.deltaTime
            entity.bank += 10 * GameTime.deltaTime
            entity.hunger += 4 * GameTime.deltaTime
            entity.thirst += 3 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
