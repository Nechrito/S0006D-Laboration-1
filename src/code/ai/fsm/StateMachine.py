class StateMachine:

    def __init__(self, entity, currentstate, globalState):
        self.owner = entity
        self.globalState = globalState
        self.locked = False
        self.previousState = None
        self.currentState = currentstate
        self.currentState.onStateEnter(self.owner)

    def update(self):
        if not self.locked:
            self.currentState.onStateExecution(self.owner)

    def toggleLockState(self, value):
        self.locked = value

    def revertState(self):
        if self.previousState is not None:
            self.changeState(self.previousState)

    def changeState(self, nextState):

        self.currentState.onStateExit(self.owner)

        self.previousState = self.currentState
        self.currentState = nextState

        self.currentState.onStateEnter(self.owner)
