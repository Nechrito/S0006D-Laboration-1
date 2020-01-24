from src.code.ai.behaviour.IState import IState


class Drink(IState):

    def __init__(self, duration):
        self.duration = duration

    def __str__(self):
        pass

    def onStateEnter(self, entity):
        print("Drink (onStateEnter)")
        pass

    def onStateExecution(self, entity):
        print("Drink (onStateExecution)")
        pass

    def onStateExit(self, entity):
        print("Drink (onStateExit)")
        pass

