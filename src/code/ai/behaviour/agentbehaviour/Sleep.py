from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime
from src.code.environment.allbuildings import getSleep


class Sleep(IState):

    def __repr__(self):
        return 'Sleeping'

    def onStateEnter(self, entity):
        print(entity.name + ": " + "Zzzz...")

    def onStateExecution(self, entity):

        if not entity.isClose(getSleep().position):
            entity.move(getSleep().position)
            return

        if entity.fatigue <= 10:
            from .Eat import Eat
            entity.change(Eat())
        else:
            entity.fatigue -= 11 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass

