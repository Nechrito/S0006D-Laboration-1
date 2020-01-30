from typing import List
import random

from ..IState import IState
from ...messaging.message import Message
from ....engine.GameTime import GameTime

from ....environment.allbuildings import getLTU, getStackHQ, getClub
from ....environment.building import Building


class CollectMoney(IState):

    def __init__(self):
        alternatives: List[Building] = [getLTU(), getClub(), getStackHQ()]
        randValue = random.randrange(0, len(alternatives))
        self.workplace = alternatives[randValue]

    def __repr__(self):
        return 'Working'

    def onStateEnter(self, entity):
        Message.sendConsole(entity, "Sigh.. another day at " + self.workplace.name + " as a " + self.workplace.description)

    def onStateExecution(self, entity):

        if not entity.isCloseTo(self.workplace.randomized):
            entity.moveTo(self.workplace.randomized)
            return

        if entity.fatigue >= 80:
            if entity.bank > 90:
                from .Purchase import Purchase
                entity.change(Purchase())

            elif entity.bank > 100:
                from .Hangout import Hangout
                entity.change(Hangout())

        entity.fatigue += 2 * GameTime.deltaTime
        entity.bank += 3 * GameTime.deltaTime
        entity.hunger += 1 * GameTime.deltaTime
        entity.thirst += 0.5 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
