from src.code.ai.behaviour.AgentBehaviour.CollectMoney import CollectMoney


class Character:
    def __init__(self, name, stateMachine):
        self.name = name
        self.fatigue = 100
        self.bank = 0
        self.thirst = 0
        self.hunger = 0
        self.stateMachine = stateMachine
        self.collectMoney1 = CollectMoney("Bar", "Verandan", 100)
        self.collectMoney2 = CollectMoney("Student", "LTU", 100)

    def update(self):
        self.stateMachine.currentState.onStateExecution()

    def change(self, state):
        self.stateMachine.moveNext(state)

    def revertState(self):
        self.stateMachine.moveNext(self.stateMachine.previousState)
