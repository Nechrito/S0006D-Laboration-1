class StateMachine:

    def __init__(self, entity, currentstate, globalState):
        self.owner = entity
        self.globalState = globalState
        self.previousState = None
        self.currentState = currentstate
        self.currentState.onStateEnter(self.owner)

    def update(self):
        self.currentState.onStateExecution(self.owner)
        self.globalState.onStateExecution(self.owner)

    def revertState(self):
        if self.previousState is not None:
            self.changeState(self.previousState)

    def changeState(self, nextState):
        self.currentState.onStateExit(self.owner)

        self.previousState = self.currentState
        self.currentState = nextState

        self.currentState.onStateEnter(self.owner)