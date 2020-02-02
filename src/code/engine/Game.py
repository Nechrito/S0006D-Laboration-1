import sys

import pygame
import pygame.freetype

from src.Settings import *
from src.code.engine.Entity import Entity
from .Camera import CameraInstance
from .GameTime import GameTime
from .MapLoader import Map
from ..ai.behaviour.agentbehaviour.CollectMoney import CollectMoney
from ..ai.behaviour.agentbehaviour.Global import Global
from ..ai.behaviour.agentbehaviour.Hangout import Hangout
from ..ai.behaviour.agentbehaviour.Purchase import Purchase
from ..environment.allbuildings import getClub, getDrink, getLTU, getHangout, getHotel, getStackHQ, getStore, getResturant
from src.code.engine.Renderer import Renderer


class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.freetype.init()

        logo = pygame.image.load(ICON_PATH)
        pygame.display.set_icon(logo)
        pygame.display.set_caption(TITLE)
        self.surface = pygame.display.set_mode(RESOLUTION)

    def load(self):

        self.renderer = Renderer(self.surface)

        self.map = Map(path.join(map_folder, 'environment.tmx'))
        self.mapImg = self.map.create()
        self.mapRect = self.mapImg.get_rect()

        self.camera = CameraInstance(self.map.width, self.map.height)

        self.clock = pygame.time.Clock()
        self.running = True
        self.slowmo = 1

        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        self.cursor = (WIDTH / 2, HEIGHT / 2)
        self.cursorRect = pygame.Rect(self.cursor, (10, 10))

        self.buildings = [getClub(), getDrink(), getResturant(), getStore(),
                          getStackHQ(), getHotel(), getHangout(), getLTU()]

        sensei = pygame.image.load(path.join(img_folder, 'sensei.png'))
        hatguy = pygame.image.load(path.join(img_folder, 'hat-guy.png'))

        self.entityGroup = pygame.sprite.Group()
        self.characterAlex = Entity("Alex", Hangout(), Global(), self.entityGroup, 495, 405, sensei)
        self.characterWendy = Entity("Wendy", CollectMoney(), Global(), self.entityGroup, 150, 610, hatguy)
        self.characterJohn = Entity("John", Purchase(), Global(), self.entityGroup, 700, 380, sensei)
        self.characterJames = Entity("James", CollectMoney(), Global(), self.entityGroup, 940, 400, hatguy)

        self.characters = [self.characterAlex, self.characterWendy, self.characterJohn, self.characterJames]

        for char in self.characters:
            self.entityGroup.add(char)

    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.slowmo = 0.1
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.slowmo = 1

        GameTime.updateTicks(self.slowmo)

        # this would've been great if I was aware of it earlier.. pygame.math.Vector2(pygame.mouse.get_pos()) // TILESIZE
        (x, y) = pygame.mouse.get_rel()
        self.cursor = (int(self.cursor[0] + x), int(self.cursor[1] + y))
        self.cursorRect = pygame.Rect((self.cursor[0] - 200, self.cursor[1] - 200), (400, 400))

        self.entityGroup.update()

        lastVal = 0
        selected = None
        for character in self.characters:
            distance = character.distanceTo((self.cursorRect.centerx, self.cursorRect.centery))
            if distance < lastVal and distance < 400 or lastVal == 0:
                character.update()
                selected = character
                lastVal = character.distanceTo(self.cursor)

        if selected:
            self.camera.update(selected)

    def draw(self):

        self.renderer.clear(self.mapImg, self.camera.moveRect(self.mapRect))

        self.renderer.renderRect((self.cursorRect.width, self.cursorRect.height),
                                 (self.cursorRect.left, self.cursorRect.top), (37, 37, 38), 80)

        self.renderer.renderRect((10, 10), (self.cursorRect.centerx, self.cursorRect.centery), (37, 37, 38), 200)

        for sprite in self.entityGroup:
            self.surface.blit(sprite.image, self.camera.moveSprite(sprite))

        for char in self.characters:
            (x, y) = (char.position[0], char.position[1] + self.camera.y - TILESIZE - 5)
            self.renderer.renderRect((46, 14), (x - 23, y - 7), (0, 0, 0), 130)
            self.renderer.renderText(char.name, (x, y), 20)

        for building in self.buildings:
            self.renderer.renderText(building.name,
                                     (building.position[0], building.position[1] + self.camera.y - TILESIZE * 4), 32)

        self.drawText()

        pygame.display.set_caption(TITLE + " | FPS " + "{:.0f}".format(self.clock.get_fps()))
        self.clock.tick(FPS)
        pygame.display.update()

    def drawText(self):

        renderCount = 0
        for i in range(len(self.characters)):

            character = self.characters[i]
            relativePosition = (
            character.position[0] + self.camera.x, character.position[1] + self.camera.y + TILESIZE_Y)

            if not self.cursorRect.collidepoint(relativePosition[0], relativePosition[1]):
                continue

            pygame.draw.line(self.surface, (220, 220, 220), (self.cursorRect.centerx, self.cursorRect.centery),
                             relativePosition)

            self.renderer.renderRect((150, 150), (renderCount * 150, 50), (0, 0, 0), 160)

            self.renderer.append(character.name + " (" + str(character.stateMachine.currentState) + ")")
            self.renderer.append("Fatigue: {0}%".format("{:.0f}".format(float(character.fatigue))))
            self.renderer.append("Hunger: {0}%".format("{:.0f}".format(float(character.hunger))))
            self.renderer.append("Thirst: {0}%".format("{:.0f}".format(float(character.thirst))))
            self.renderer.append("Bank: {0}$".format("{:.0f}".format(float(character.bank))))
            self.renderer.renderTexts((25 + WIDTH * 0.05 + 160 * renderCount, HEIGHT * 0.10), 22, (255, 255, 255))

            renderCount += 1
