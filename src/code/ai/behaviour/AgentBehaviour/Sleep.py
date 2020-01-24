from src.code.ai.behaviour.IState import IState


class Sleep(IState):

    def __init__(self, duration):
        self.duration = duration

    def __str__(self):
        pass

    def onStateEnter(self, entity):
        print("Sleep (onStateEnter)")
        pass

    def onStateExecution(self, entity):
        print("Sleep (onStateExecution)")
        pass

    def onStateExit(self, entity):
        print("Sleep (onStateExit)")
        pass

