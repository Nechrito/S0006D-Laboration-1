import pygame


class GameTime:
    ticks = 0
    lastFrame = 0
    deltaTime = 0
    fixedDeltaTime = 0

    @classmethod
    def updateTicks(cls, multiplier=1):
        cls.ticks = pygame.time.get_ticks()
        cls.deltaTime = cls.fixedDeltaTime = ((cls.ticks - cls.lastFrame) / 1000.0)
        cls.deltaTime *= multiplier

        cls.lastFrame = cls.ticks
