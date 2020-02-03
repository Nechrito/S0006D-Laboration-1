from datetime import datetime

import pygame
import datetime


class GameTime:

    ticks = 0
    lastFrame = 0
    deltaTime = 0
    fixedDeltaTime = 0
    totalTicks = 0
    scale = 1
    startDate: datetime

    @classmethod
    def init(cls):
        cls.startDate = datetime.datetime.now()

    @classmethod
    def setScale(cls, scale):
        cls.scale = scale
        return cls.scale

    @classmethod
    def updateTicks(cls, isPaused):
        cls.ticks = pygame.time.get_ticks()

        if not isPaused:
            cls.totalTicks += cls.ticks

        cls.deltaTime = cls.fixedDeltaTime = ((cls.ticks - cls.lastFrame) / 1000.0)
        cls.deltaTime *= cls.scale  # post multiplying only here prevents fixedDeltaTime from scaling

        cls.lastFrame = cls.ticks

    @classmethod
    def timeElapsed(cls):
        increment = datetime.timedelta(milliseconds=cls.totalTicks)
        return (cls.startDate + increment).strftime("%m-%d %H:%M")  # "%Y-%m-%d %H:%M:%S"

    @classmethod
    def minutesToMilliseconds(cls, minute):
        return (minute * 60000) / cls.scale
