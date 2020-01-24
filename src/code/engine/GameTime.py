import pygame


class GameTime:
    ticks = 0
    lastFrame = 0
    deltaTime = 0

    @classmethod
    def updateTicks(cls):
        cls.ticks = pygame.time.get_ticks()
        cls.deltaTime = (cls.ticks - cls.lastFrame) / 1000.0
        cls.lastFrame = cls.ticks
