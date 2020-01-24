from src.code.ai.fsm.StateMachine import StateMachine
from src.code.engine.GameTime import GameTime


class Character:
    def __init__(self, name, state):
        self.name = name
        self.fatigue = 0
        self.bank = 0
        self.thirst = 0
        self.hunger = 0
        # self.bartenderState = CollectMoney("Bar", "Verandan", 100)
        # self.studentState = CollectMoney("Student", "LTU", 100)
        self.stateMachine = StateMachine(self, state)

    def update(self):
        self.thirst += 2 * GameTime.deltaTime
        self.hunger += 2 * GameTime.deltaTime
        self.fatigue += 1 * GameTime.deltaTime

        self.stateMachine.update()

    def change(self, state):
        self.stateMachine.changeState(state)

    def revertState(self):
        self.stateMachine.revertState()
