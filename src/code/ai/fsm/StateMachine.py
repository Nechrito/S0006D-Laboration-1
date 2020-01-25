class StateMachine:

    def __init__(self, entity, currentstate):
        self.owner = entity
        self.globalState = None
        self.previousState = None
        self.currentState = currentstate
        self.currentState.onStateEnter(self.owner)

    def update(self):
        self.currentState.onStateExecution(self.owner)
        if self.globalState:
            self.globalState.onStateExecution(self.owner)

    def setGlobal(self, state):
        self.globalState = state

    def revertState(self):
        self.changeState(self.previousState)

    def changeState(self, nextState):
        self.currentState.onStateExit(self.owner)

        self.previousState = self.currentState
        self.currentState = nextState

        self.currentState.onStateEnter(self.owner)