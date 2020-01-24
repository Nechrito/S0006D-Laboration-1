from src.code.ai.Character import Character
from src.code.ai.behaviour.AgentBehaviour.CollectMoney import CollectMoney
from src.code.ai.behaviour.IState import IState
from src.code.ai.fsm.StateTransition import StateTransition
from src.code.ai.fsm.StateMachine import StateMachine
from src.Enums.AgentStates import AgentStates

from typing import Dict

import pygame


def main():
    pygame.init()
    logo = pygame.image.load("resources/controller-icon64.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("S0006D - Laboration 1 - Philip Lindh")
    screen = pygame.display.set_mode([1176, 664])

    statemachine = StateMachine(transitions, AgentStates.CollectMoney, AgentStates.Hangout)
    character = Character("Alex", statemachine)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill([135, 206, 235])
        pygame.display.update()
        character.update()


# Only executes the main method if this module is executed as the main script
if __name__ == "__main__":
    main()
