import math

import pygame
from src.Settings import *
from src.code.ai.fsm.StateMachine import StateMachine
from src.code.engine.GameTime import GameTime
import random


class Entity(pygame.sprite.Sprite):
    def __init__(self, name, state, category, x, y, image):
        pygame.sprite.Sprite.__init__(self, category)
        self.image = image

        self.position = [x + TILESIZE_X / 2, y + TILESIZE_Y / 2]
        self.name = name

        self.fatigue = random.randrange(0, 70)
        self.bank = random.randrange(0, 120)
        self.thirst = random.randrange(0, 50)
        self.hunger = random.randrange(0, 50)
        self.stateMachine = StateMachine(self, state)

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.thirst += 2 * GameTime.deltaTime
        self.hunger += 2 * GameTime.deltaTime
        self.fatigue += 1 * GameTime.deltaTime

        self.stateMachine.update()

    def isClose(self, target):
        return math.sqrt((self.position[0] - target[0])**2 + (self.position[1] - target[1])**2) < 20

    def move(self, target):
        self.position[0] += (target[0] - self.position[0]) * GameTime.deltaTime
        self.position[1] += (target[1] - self.position[1]) * GameTime.deltaTime

    def change(self, state):
        self.stateMachine.changeState(state)

    def revertState(self):
        self.stateMachine.revertState()