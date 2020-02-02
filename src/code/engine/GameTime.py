import pygame
import datetime


class GameTime:
    ticks = 0
    lastFrame = 0
    deltaTime = 0
    fixedDeltaTime = 0

    @classmethod
    def updateTicks(cls, scale):
        cls.ticks = pygame.time.get_ticks()

        cls.deltaTime = cls.fixedDeltaTime = ((cls.ticks - cls.lastFrame) / 1000.0)
        cls.deltaTime *= scale  # post multiplying only here prevents fixedDeltaTime from scaling

        cls.lastFrame = cls.ticks

    @classmethod
    def timeElapsed(cls):
        tickToDatetime = datetime.datetime.now() + datetime.timedelta(microseconds=cls.ticks / 10)
        return tickToDatetime.strftime("%Y-%m-%d %H:%M:%S")
