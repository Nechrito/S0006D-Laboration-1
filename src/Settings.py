from os import path

# Application settings
TITLE = "S0006D - Laboration 1 - Philip Lindh"
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
RESOLUTION = [SCREEN_WIDTH, SCREEN_HEIGHT]
FPS = 144
TILESIZE = 16

# Shortcuts to resource folders
ApplicationPath = path.dirname(__file__)
ImagePath = path.join(ApplicationPath, 'resources/img')
MapPath = path.join(ApplicationPath, 'resources/map')

# Resource files direct path
ICON_PATH = "resources/icon/controller-icon64.png"
FONT_BLACK = "resources/fonts/Roboto-Black.ttf"
FONT_BOLD = "resources/fonts/Roboto-Bold.ttf"
FONT_REGULAR = "resources/fonts/Roboto-Regular.ttf"

