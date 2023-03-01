import pygame
from pygame.sprite import AbstractGroup


class Generic(pygame.sprite.Sprite):
    def __init__(self, *groups: AbstractGroup, **kwargs):
        super().__init__(*groups)
        self.image = kwargs['image']
        self.rect = self.image.get_rect(topleft=kwargs['pos'])
        self.z = kwargs['z']
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.7, -self.rect.height * 0.75)


class Ground(Generic):
    def __init__(self, *groups: AbstractGroup, **kwargs):
        super().__init__(*groups, **kwargs)
        pass
