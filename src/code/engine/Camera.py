import pygame
from src.Settings import *
from src.code.engine.Entity import Entity


class CameraInstance:

    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def setRect(self, rect):
        return rect.move(self.camera.topleft)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target: Entity):
        self.x = -target.position[0] + int(WIDTH / 2)
        self.y = -target.position[1] + int(HEIGHT / 2)

        #  Make sure we're within map boundaries
        self.x = min(0, self.x)
        self.y = min(0, self.y)
        self.x = max(-(self.width - WIDTH), self.x)
        self.y = max(-(self.height - HEIGHT), self.y)

        self.camera = pygame.Rect(self.x, self.y, self.width, self.height)
