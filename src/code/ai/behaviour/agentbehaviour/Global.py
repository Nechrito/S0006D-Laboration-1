from ....engine.Entity import Entity
from ..IState import IState
from .Drink import Drink
from .Sleep import Sleep
from .CollectMoney import CollectMoney
from .Eat import Eat

class Global(IState):

    def __init__(self):
        self.currentState = None

    def __repr__(self):
        pass

    def onStateEnter(self, entity: Entity):
        pass

    def onStateExecution(self, entity: Entity):

        if entity.hunger >= 95 and not self.currentState == Eat:
            self.currentState = Eat
            entity.change(Eat())

        if entity.thirst >= 95 and not self.currentState == Drink:
            self.currentState = Drink
            entity.change(Drink())

        if entity.fatigue >= 95 and not self.currentState == Sleep:
            self.currentState = Sleep
            entity.change(Sleep())

        if entity.bank <= 5 and not self.currentState == CollectMoney:
            self.currentState = CollectMoney
            entity.change(CollectMoney())

    def onStateExit(self, entity: Entity):
        pass
