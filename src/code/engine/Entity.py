import pygame
from pygame.math import Vector2

from src.code.ai.fsm.StateMachine import StateMachine
from src.code.engine.GameTime import GameTime


class Entity(pygame.sprite.Sprite):
    def __init__(self, name, fatigue, bank, thirst, hunger, state, category, x, y, image):
        pygame.sprite.Sprite.__init__(self, category)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.position = [x, y]
        self.velocity = (0, 0)
        self.acc = (0, 0)
        self.rotation = 0

        self.name = name
        self.fatigue = fatigue
        self.bank = bank
        self.thirst = thirst
        self.hunger = hunger
        self.stateMachine = StateMachine(self, state)

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.thirst += 2 * GameTime.deltaTime
        self.hunger += 2 * GameTime.deltaTime
        self.fatigue += 1 * GameTime.deltaTime

        self.stateMachine.update()

    def move(self, position):
        self.position[0] += position[0] * GameTime.deltaTime
        self.position[1] += position[1] * GameTime.deltaTime

    def getPositon(self):
        return self.position

    def change(self, state):
        self.stateMachine.changeState(state)

    def revertState(self):
        self.stateMachine.revertState()
