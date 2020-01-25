import pygame
from src.Settings import *
from src.code.engine.Entity import Entity


class CameraInstance:

    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width / 2, height / 2)
        self.width = width
        self.height = height

    def setRect(self, rect):
        return rect.move(self.camera.topleft)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target: Entity):
        x = -target.position[0] + int(WIDTH / 2)
        y = -target.position[1] + int(HEIGHT / 2)

        #  Make sure we're within map boundaries
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)
