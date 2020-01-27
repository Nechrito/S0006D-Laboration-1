import random


class Building:
    def __init__(self, position, name: str, desc: str = None):
        self.position = position
        self.name = name
        self.description = desc

        threshold = 60
        self.randomized = self.position[0] + random.randrange(-threshold, threshold), self.position[1] + random.randrange(-threshold, 10)