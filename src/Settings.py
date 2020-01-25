# define some colors (R, G, B)
from os import path

game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'resources/img')
map_folder = path.join(game_folder, 'resources/map')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
SKYBLUE = (135, 206, 235)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024
HEIGHT = 768
RESOLUTION = [WIDTH, HEIGHT]

FPS = 60

TITLE = "S0006D - Laboration 1 - Philip Lindh"

ICON_PATH = "resources/icon/controller-icon64.png"
FONT_BLACK = "resources/fonts/Roboto-Black.ttf"
FONT_BOLD = "resources/fonts/Roboto-Bold.ttf"
FONT_REGULAR = "resources/fonts/Roboto-Regular.ttf"

TILESIZE_X = 16
TILESIZE_Y = 16

GRIDWIDTH = WIDTH / TILESIZE_X
GRIDHEIGHT = HEIGHT / TILESIZE_Y
