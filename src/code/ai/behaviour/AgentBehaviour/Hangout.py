from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime


class Hangout(IState):

    def __init__(self, entity):
        self.bankStart = entity.bank

    def onStateEnter(self, entity):
        print("Can't wait to hangout with my pal")
        pass

    def onStateExecution(self, entity):
        if entity.fatigue > 65:
            from .Sleep import Sleep
            state = Sleep()
            entity.change(state)

        elif entity.bank > 30:
            entity.bank -= 5 * GameTime.deltaTime

        entity.fatigue += 7 * GameTime.deltaTime


    def onStateExit(self, entity):
        pass
