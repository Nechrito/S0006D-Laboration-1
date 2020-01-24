class StateMachine:

    def __init__(self, entity, currentstate):
        self.owner = entity
        self.currentState = currentstate
        self.previousState = currentstate
        self.currentState.onStateEnter(self.owner)

    def update(self):
        self.currentState.onStateExecution(self.owner)

    def revertState(self):
        self.changeState(self.previousState)

    def changeState(self, nextState):
        self.currentState.onStateExit(self.owner)

        self.previousState = self.currentState
        self.currentState = nextState

        self.currentState.onStateEnter(self.owner)

        # print("Changed state from " + str(self.previousState) + " to " + str(self.currentState))
