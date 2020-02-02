class StateMachine:

    def __init__(self, entity, currentstate, globalState):
        self.owner = entity
        self.globalState = globalState
        self.locked = False
        self.previousState = None
        self.currentState = currentstate
        self.currentState.enter(self.owner)

    def update(self):
        if not self.locked:
            self.currentState.execute(self.owner)
        self.globalState.execute(self.owner)

    def toggleLockState(self, value):
        self.locked = value

    def revertState(self):
        if self.previousState is not None:
            self.changeState(self.previousState)

    def changeState(self, nextState):

        self.previousState = self.currentState

        self.currentState.exit(self.owner)

        self.currentState = nextState

        self.currentState.enter(self.owner)
