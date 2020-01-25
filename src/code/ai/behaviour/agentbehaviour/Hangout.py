from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime


class Hangout(IState):

    def __repr__(self):
        return 'Hanging out'

    def onStateEnter(self, entity):
        print(entity.name + ": " + "Can't wait to hangout with my pal")

    def onStateExecution(self, entity):
        if entity.fatigue > 65:
            from .Sleep import Sleep
            entity.change(Sleep())

        elif entity.bank > 30:
            entity.bank -= 5 * GameTime.deltaTime

        entity.fatigue += 7 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
