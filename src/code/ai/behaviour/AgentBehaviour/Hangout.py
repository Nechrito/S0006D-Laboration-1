from src.code.ai.behaviour.IState import IState


class Hangout(IState):

    def __init__(self, duration):
        self.duration = duration

    def __str__(self):
        pass

    def onStateEnter(self, entity):
        print("Hangout (onStateEnter)")
        pass

    def onStateExecution(self, entity):
        print("Hangout (onStateExecution)")
        pass

    def onStateExit(self, entity):
        print("Hangout (onStateExit)")
        pass

