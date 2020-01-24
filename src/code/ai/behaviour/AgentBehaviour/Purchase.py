from src.code.ai.behaviour.IState import IState


class Purchase(IState):

    def __init__(self, duration):
        self.duration = duration

    def __str__(self):
        pass

    def onStateEnter(self, entity):
        print("Purchase (onStateEnter)")
        pass

    def onStateExecution(self, entity):
        print("Purchase (onStateExecution)")
        pass

    def onStateExit(self, entity):
        print("Purchase (onStateExit)")
        pass

