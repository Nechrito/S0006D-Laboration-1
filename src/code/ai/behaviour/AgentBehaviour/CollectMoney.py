from src.code.ai.behaviour.IState import IState


class CollectMoney(IState):

    def __init__(self, location, workplaceName, duration):
        self.location = location
        self.workplace = workplaceName
        self.duration = duration

    def __str__(self):
        pass

    def onStateEnter(self, entity):
        print("CollectMoney (onStateEnter) " + self.workplace)
        pass

    def onStateExecution(self, entity):
        print("CollectMoney (onStateExecution) " + self.workplace)
        pass

    def onStateExit(self, entity):
        print("CollectMoney (onStateExit) " + self.workplace)
        pass

