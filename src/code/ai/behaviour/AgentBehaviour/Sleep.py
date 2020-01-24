from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime


class Sleep(IState):

    def onStateEnter(self, entity):
        print("Zzzz...")

    def onStateExecution(self, entity):
        if entity.fatigue <= 10:
            from .Eat import Eat
            state = Eat()
            entity.change(state)
        else:
            entity.fatigue -= 11 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass

