from ..IState import IState
from ....engine.GameTime import GameTime
from ....environment.allbuildings import getHangout


class Hangout(IState):

    def __repr__(self):
        return 'Hangout'

    def onStateEnter(self, entity):
        print(entity.name + ": " + "Can't wait to hangout with my pal")

    def onStateExecution(self, entity):

        if not entity.isClose(getHangout().position):
            entity.move(getHangout().position)
            return

        entity.bank -= 3 * GameTime.deltaTime
        entity.fatigue += 2 * GameTime.deltaTime

    def onStateExit(self, entity):
        pass
