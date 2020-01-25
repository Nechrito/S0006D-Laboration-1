import pygame
import pytmx


class Map:
    def __init__(self, filename):
        instance = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = instance.width * instance.tilewidth
        self.height = instance.height * instance.tileheight
        self.data = instance

    def render(self, surface):
        tileImg = self.data.get_tile_image_by_gid  # Fetches the image represented by the ID
        for layer in self.data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = tileImg(gid)
                    if tile:
                        surface.blit(tile, (x * self.data.tilewidth,
                                            y * self.data.tileheight))

    def create(self):
        surface = pygame.Surface((self.width, self.height))
        self.render(surface)
        return surface
