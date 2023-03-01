import pygame
from pygame.sprite import AbstractGroup
from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups: AbstractGroup, **kwargs):
        super().__init__(*groups)
        self.animations = dict()
        self.import_assets()
        self.speed = 200
        self.frame_index = 0
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=kwargs['pos'])
        self.z = kwargs['z']

        # 移动
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 100
        self.play_speed = {
            'idle': 12,
            'run': 24}

    def import_assets(self):
        self.animations = {
            'idle': [],
            'run': [],
            'jump': [],
            'atk': [],
            'hurt2': []
        }
        for animation in self.animations.keys():
            path = r'resources/graphics/character' + '/' + animation
            self.animations[animation] = import_folder(path)

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = 'idle'

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def input(self):
        keys = pygame.key.get_pressed()

        # 水平方向
        if keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'run'
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'run'
        else:
            self.direction.x = 0

        # 垂直方向
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def animate(self, dt):
        self.frame_index += dt * self.play_speed[self.status]
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def update(self, dt) -> None:
        self.input()
        self.get_status()
        self.move(dt)
        self.animate(dt)
