from ..IState import IState
from ....engine.GameTime import GameTime
import random


class CollectMoney(IState):

    def __init__(self):
        alternatives = {'Pinchos': 'Bartender', 'LTU': 'Student', 'Stackoverflow HQ': 'Smartass'}
        randValue = random.choice(list(alternatives.items()))
        self.workplace = randValue

    def __repr__(self):
        return 'Working'

    def onStateEnter(self, entity):
        print(entity.name + ": " + "Sigh.. another day at " + self.workplace[0] + " as a " + self.workplace[1])

    def onStateExecution(self, entity):
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
