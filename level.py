import pygame
from player import Player
from sprites import Generic
from setting import *


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        # 创建玩家
        self.player = Player(self.all_sprites, pos=(200, SCREEN_HEIGHT - 50), z=LAYERS['main'])
        self.setup()

    def setup(self):
        # 创建背景
        Generic(self.all_sprites,
                pos=(0, 0),
                image=pygame.image.load('resources/graphics/world/background.png'),
                z=LAYERS['ground'])

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.customize_draw(self.display_surface)
        self.all_sprites.update(dt)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super(CameraGroup, self).__init__()
        self.display_surface = pygame.display.get_surface()

    def customize_draw(self, player):
        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    self.display_surface.blit(sprite.image, sprite.rect)
