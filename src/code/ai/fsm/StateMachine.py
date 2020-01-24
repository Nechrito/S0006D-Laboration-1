from src.code.ai.fsm.StateTransition import StateTransition


class StateMachine:

    def __init__(self, transitions, currentstate, endstate):
        self.transitions = transitions
        self.currentState = currentstate
        self.previousState = endstate
        self.endState = endstate

    def getNext(self, nextState):
        transition = StateTransition(self.currentState, nextState)
        try:
            nextTransition = self.transitions.get(transition)
        except Exception:
            raise Exception("Invalid transition: " + str(self.currentState) + " -> " + str(nextState))

        return nextTransition

    def canReachNext(self, nextState):
        transition = StateTransition(self.currentState, nextState)
        if self.transitions.get(transition):
            return True
        else:
            return False

    def moveNext(self, nextState):
        if not self.canReachNext(nextState):
            print("Failed to change state!")
            return

        self.previousState = self.currentState
        self.currentState = self.getNext(nextState)

        print("Changed state from " + str(self.previousState) + " to " + str(self.currentState))