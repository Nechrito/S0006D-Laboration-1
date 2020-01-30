from ..IState import IState
from ....engine.GameTime import GameTime
from ....environment.allbuildings import getHangout
from ...messaging.message import Message


class Hangout(IState):

    def __repr__(self):
        return 'Hangout'

    def onStateEnter(self, entity):
        Message.sendConsole(entity, "Can't wait to hangout with my pals")

    def onStateExecution(self, entity):
        if not entity.isCloseTo(getHangout().position):
            entity.moveTo(getHangout().position)
            return

        entity.bank -= 3 * GameTime.deltaTime
        entity.fatigue += 2 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
