import sys

import pygame
import pygame.freetype

from src.Config.Settings import *
from src.code.ai.Character import Character
from src.code.ai.behaviour.AgentBehaviour.CollectMoney import CollectMoney
from src.code.engine.GameTime import GameTime


class Game:
    def __init__(self):
        pygame.init()
        pygame.freetype.init()

        logo = pygame.image.load(ICON)
        pygame.display.set_icon(logo)
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.font = pygame.freetype.Font(FONTREGULAR, 24)
        self.clock = pygame.time.Clock()
        self.running = True

        bartenderState = CollectMoney("Pinchos", "Bartender")
        self.character = Character("Alex", bartenderState)

    def update(self):

        if pygame.event.get(pygame.QUIT) or not self.running:
            pygame.quit()
            sys.exit()

        pygame.event.pump()
        pygame.display.update()

        GameTime.updateTicks()
        self.character.update()
        self.draw()

        self.clock.tick(FPS)
        pygame.display.set_caption(TITLE + " | FPS " + "{:.0f}".format(self.clock.get_fps()))

    def draw(self):
        self.screen.fill(DARKGREY)
        self.showGrid()
        self.drawText()
        pygame.display.flip()

    def drawText(self):
        fatigue = "{:.0f}".format(float(self.character.fatigue))
        hunger = "{:.0f}".format(float(self.character.hunger))
        thirst = "{:.0f}".format(float(self.character.thirst))
        bank = "{:.0f}".format(float(self.character.bank))
        text: str = "Fatigue: " + fatigue + "% | Hunger: " + hunger + "% | Thirst: " + thirst + "% | Bank: $" + bank
        self.font.render_to(self.screen, (WIDTH / 2 - 150, 50), text, (255, 255, 255))

    def showGrid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
