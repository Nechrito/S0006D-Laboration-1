from ....engine.Entity import Entity
from ..IState import IState
from .Drink import Drink
from .Sleep import Sleep
from .CollectMoney import CollectMoney
from .Eat import Eat


class Global(IState):

    def __init__(self):
        self.lastState = None

    def __repr__(self):
        pass

    def onStateEnter(self, entity: Entity):
        pass

    def onStateExecution(self, entity: Entity):

        if entity.hunger >= 99 and not self.lastState == Eat:
            self.lastState = Eat
            entity.change(Eat())

        if entity.thirst >= 99 and not self.lastState == Drink:
            self.lastState = Drink
            entity.change(Drink())

        if entity.fatigue >= 99 and not self.lastState == Sleep:
            self.lastState = Sleep
            entity.change(Sleep())

        if entity.bank <= 1 and not self.lastState == CollectMoney:
            self.lastState = CollectMoney
            entity.change(CollectMoney())

    def onStateExit(self, entity: Entity):
        pass
