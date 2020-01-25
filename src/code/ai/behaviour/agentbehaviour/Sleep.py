from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime


class Sleep(IState):

    def __repr__(self):
        return 'Sleeping'

    def onStateEnter(self, entity):
        print(entity.name + ": " + "Zzzz...")

    def onStateExecution(self, entity):
        if entity.fatigue <= 10:
            from .Eat import Eat
            entity.change(Eat())
        else:
            entity.fatigue -= 11 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass

