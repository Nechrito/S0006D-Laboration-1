import sys

import pygame
import pygame.freetype

from .Camera import CameraInstance
from .MapLoader import Map
from ..environment.allbuildings import getPinchos, getDrink, getLTU, getHangout, getSleep, getStackHQ, getStore, getEat
from ..environment.building import Building
from ..rendering.Renderer import Renderer
from src.Settings import *
from src.code.engine.Entity import Entity
from ..ai.behaviour.agentbehaviour.CollectMoney import CollectMoney
from .GameTime import GameTime


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.freetype.init()

        logo = pygame.image.load(ICON_PATH)
        pygame.display.set_icon(logo)
        pygame.display.set_caption(TITLE)
        pygame.display.set_mode(RESOLUTION)

    def load(self):

        self.sprites = pygame.sprite.Group()
        self.renderer = Renderer()
        self.map = Map(path.join(map_folder, 'environment.tmx'))
        self.mapImg = self.map.create()
        self.mapRect = self.mapImg.get_rect()
        self.camera = CameraInstance(self.map.width, self.map.height)

        self.clock = pygame.time.Clock()
        self.running = True

        self.buildings = [getPinchos(), getDrink(), getEat(), getStore(), getStackHQ(), getSleep(), getHangout(), getLTU()]

        sensei = pygame.image.load(path.join(img_folder, 'sensei.png')).convert_alpha()
        hatguy = pygame.image.load(path.join(img_folder, 'hat-guy.png')).convert_alpha()
        mani = pygame.image.load(path.join(img_folder, 'mani.png')).convert_alpha()

        self.characterAlex = Entity("Alex", CollectMoney(), self.sprites, 495, 405, sensei)
        self.characterWendy = Entity("Wendy", CollectMoney(), self.sprites, 150, 610, hatguy)
        self.characterJohn = Entity("John", CollectMoney(), self.sprites, 700, 380, hatguy)
        self.characters = [self.characterAlex, self.characterWendy, self.characterJohn]
        self.selectedCharacter = self.characterAlex

        for character in self.characters:
            self.sprites.add(character)

    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        speed = 150
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.selectedCharacter.move([0, speed])

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.selectedCharacter.move([0, -speed])

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.selectedCharacter.move([speed, 0])

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.selectedCharacter.move([-speed, 0])

        GameTime.updateTicks()

        self.sprites.update()
        self.camera.update(self.selectedCharacter)

        for character in self.characters:
            character.update()

        self.clock.tick(FPS)

    def draw(self):
       # (x, y) = pygame.mouse.get_pos()
        (x, y) = self.selectedCharacter.position
        pygame.display.set_caption(TITLE + " | FPS " + "{:.0f}".format(self.clock.get_fps()) + " | X: " + str(x) + " | Y: " + str(y))
        self.renderer.clear(self.mapImg, self.camera.setRect(self.mapRect))

        for sprite in self.sprites:
            screen = pygame.display.get_surface()
            screen.blit(sprite.image, self.camera.apply(sprite))

        for char in self.characters:
            self.renderer.renderText(char.name, (char.position[0], char.position[1] + self.camera.y + TILESIZE_Y), 20)

        for building in self.buildings:
            self.renderer.renderText(building.name, (building.position[0], building.position[1] + self.camera.y - TILESIZE_Y * 4), 32)

        self.drawText()
        pygame.display.flip()

    def drawText(self):
        for i in range(len(self.characters)):
            character = self.characters[i]
            self.renderer.append(character.name + " (" + str(character.stateMachine.currentState) + ")")
            self.renderer.append("Fatigue: {0}%".format("{:.0f}".format(float(character.fatigue))))
            self.renderer.append("Hunger: {0}%".format("{:.0f}".format(float(character.hunger))))
            self.renderer.append("Thirst: {0}%".format("{:.0f}".format(float(character.thirst))))
            self.renderer.append("Bank: {0}$".format("{:.0f}".format(float(character.bank))))
            self.renderer.renderTexts((WIDTH * 0.05 + 160 * i, HEIGHT * 0.10), 22)
