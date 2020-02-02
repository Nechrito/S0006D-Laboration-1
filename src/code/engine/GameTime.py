import pygame
import datetime


class GameTime:
    ticks = 0
    lastFrame = 0
    deltaTime = 0
    fixedDeltaTime = 0
    totalTicks = 0

    @classmethod
    def updateTicks(cls, scale):
        cls.ticks = pygame.time.get_ticks()
        cls.totalTicks += cls.ticks

        cls.deltaTime = cls.fixedDeltaTime = ((cls.ticks - cls.lastFrame) / 1000.0)
        cls.deltaTime *= scale  # post multiplying only here prevents fixedDeltaTime from scaling

        cls.lastFrame = cls.ticks

    @classmethod
    def timeElapsed(cls):
        increment = datetime.timedelta(milliseconds=cls.totalTicks * 10)
        return (datetime.datetime.now() + increment).strftime("%d %H:%M")  # "%Y-%m-%d %H:%M:%S"
