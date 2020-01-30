import pygame
import pygame.freetype
from src.Settings import *


class Renderer:

    def __init__(self, surface):
        self.surface = surface
        self.texts = []

    def clear(self, mapImg, mapRect):
        pygame.display.update()
        #screen.fill(DARKGREY)
        self.surface.blit(mapImg, mapRect)

    def renderCircle(self, position, radius, color=(255, 255, 255)):
        pygame.draw.circle(self.surface, color, position, radius, 1)

    def renderRect(self, size, pos, color=(255, 255, 255), alpha=128):
        rect = pygame.Surface(size)
        rect.set_alpha(alpha)
        rect.fill(color)
        self.surface.blit(rect, pos)

    def renderText(self, text: str, position, size, color=(255, 255, 255)):
        font = pygame.freetype.Font(FONT_REGULAR, int(HEIGHT * size / WIDTH))  # Scaled with resolution
        fontRendered, fontRect = font.render(text, color)
        self.surface.blit(fontRendered, (position[0] - fontRect[2] / 2, position[1] - fontRect[3] / 2))

    def renderTexts(self, position, size, color=(0, 0, 0)):
        if len(self.texts) <= 0:
            raise Exception("Use method .append(...) first to render multiple lines of text!")

        pos = (position[0], position[1])
        for line in range(len(self.texts)):
            msg = self.texts[line]
            self.renderText(msg, pos, size, color)
            pos = (pos[0], pos[1] + size + 2)

        self.texts.clear()

    def append(self, msg):
        self.texts.append(msg)

    def showGrid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.surface, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE_Y):
            pygame.draw.line(self.surface, LIGHTGREY, (0, y), (WIDTH, y))