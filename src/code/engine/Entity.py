import math

import pygame
from src.Settings import *
from src.code.ai.fsm.StateMachine import StateMachine
from src.code.engine.GameTime import GameTime
import random


class Entity(pygame.sprite.Sprite):
    def __init__(self, name, state, globalState, category, x, y, image):
        pygame.sprite.Sprite.__init__(self, category)
        self.image = image

        self.position = [x + TILESIZE_X / 2, y + TILESIZE_Y / 2]
        self.name = name

        self.fatigue = random.randrange(0, 70)
        self.bank = random.randrange(0, 120)
        self.thirst = random.randrange(0, 50)
        self.hunger = random.randrange(0, 50)
        self.stateMachine = StateMachine(self, state, globalState)

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]

        self.thirst += 0.5 * GameTime.deltaTime
        self.hunger += 0.5 * GameTime.deltaTime
        self.fatigue += 0.5 * GameTime.deltaTime

        self.stateMachine.update()

    def isClose(self, target, distance=20):
        return self.distanceTo(target) <= distance

    def distanceTo(self, target):
        return math.sqrt((self.rect.centerx - target[0]) ** 2 + (self.rect.centery - target[1]) ** 2)

    def move(self, target):
        length = self.distanceTo(target)

        self.position[0] += ((target[0] - self.position[0]) / length) * GameTime.deltaTime * 70
        self.position[1] += ((target[1] - self.position[1]) / length) * GameTime.deltaTime * 70

    def change(self, state):
        self.stateMachine.changeState(state)

    def revertState(self):
        self.stateMachine.revertState()
