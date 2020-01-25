import pygame
import pygame.freetype
from src.Settings import *


class Renderer:
    texts = []

    @classmethod
    def clear(cls, mapImg, mapRect):
        screen = pygame.display.get_surface()
        pygame.display.update()
        #screen.fill(DARKGREY)
        screen.blit(mapImg, mapRect)

    @classmethod
    def renderText(cls, text: str, position, size, color=(255, 255, 255)):
        font = pygame.freetype.Font(FONT_REGULAR, int(HEIGHT * size / WIDTH))  # Scaled with resolution
        fontRendered, fontRect = font.render(text, color)
        screen = pygame.display.get_surface()
        screen.blit(fontRendered, (position[0] - fontRect[2] / 2, position[1] - fontRect[3] / 2))

    @classmethod
    def renderTexts(cls, position, size, color=(0, 0, 0)):
        if len(cls.texts) <= 0:
            raise Exception("Use method .append(...) first to render multiple lines of text!")

        pos = (position[0], position[1])
        for line in range(len(cls.texts)):
            msg = cls.texts[line]
            cls.renderText(msg, pos, size, color)
            pos = (pos[0], pos[1] + size + 2)

        cls.texts.clear()

    @classmethod
    def append(cls, msg):
        cls.texts.append(msg)

    @classmethod
    def showGrid(cls):
        screen = pygame.display.get_surface()
        for x in range(0, WIDTH, TILESIZE_X):
            pygame.draw.line(screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE_Y):
            pygame.draw.line(screen, LIGHTGREY, (0, y), (WIDTH, y))
