from ..IState import IState
from src.code.engine.Entity import Entity


class Global(IState):

    def __repr__(self):
        pass

    def onStateEnter(self, entity: Entity):
        pass

    def onStateExecution(self, entity: Entity):
        if entity.hunger >= 90:
            from .Eat import Eat
            entity.change(Eat())

        elif entity.thirst >= 90:
            from .Drink import Drink
            entity.change(Drink())

        elif entity.fatigue >= 90:
            from .Sleep import Sleep
            entity.change(Sleep())

    def onStateExit(self, entity: Entity):
        pass
