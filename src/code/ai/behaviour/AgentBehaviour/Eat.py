from src.code.ai.behaviour.IState import IState


class Eat(IState):

    def __init__(self, duration):
        self.duration = duration

    def __str__(self):
        pass

    def onStateEnter(self, entity):
        print("Eat (onStateEnter)")
        pass

    def onStateExecution(self, entity):
        print("Eat (onStateExecution)")
        pass

    def onStateExit(self, entity):
        print("Eat (onStateExit)")
        pass

