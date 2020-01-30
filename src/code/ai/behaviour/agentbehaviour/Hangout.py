from src.code.ai.behaviour.IState import IState
from src.code.engine.GameTime import GameTime
from src.code.environment.allbuildings import getHangout
from src.code.ai.messaging.message import Message


class Hangout(IState):

    def __repr__(self):
        return 'Hangout'

    def onStateEnter(self, entity):
        Message.sendConsole(entity, "Can't wait to hangout with my pals")

    def onStateExecution(self, entity):
        if not entity.isCloseTo(getHangout().position):
            entity.moveTo(getHangout().position)
            return

        if entity.hunger > 60:
            from .Eat import Eat
            entity.change(Eat())
        else:
            entity.bank -= 3 * GameTime.deltaTime
            entity.fatigue += 2 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
