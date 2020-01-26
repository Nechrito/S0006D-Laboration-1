from ..IState import IState
from ....engine.GameTime import GameTime
import random

from ....environment.allbuildings import getLTU, getStackHQ, getPinchos


class CollectMoney(IState):

    def __init__(self):
        alternatives = [getLTU(), getPinchos(), getStackHQ()]
        randValue = random.randrange(0, len(alternatives))
        self.workplace = alternatives[randValue]

    def __repr__(self):
        return 'Working'

    def onStateEnter(self, entity):
        print(entity.name + ": " + "Sigh.. another day at " + self.workplace.name + " as a " + self.workplace.description)

    def onStateExecution(self, entity):

        if not entity.isClose(self.workplace.position):
            entity.move(self.workplace.position)
            return

        if entity.fatigue >= 70:
            from .Sleep import Sleep
            state = Sleep()
            entity.change(state)

        elif entity.bank > 150:
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
