import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]: self.direction.x = 1
        elif key[pygame.K_a]: self.direction.x = -1
        else: self.direction.x = 0
        if key[pygame.K_w]: self.direction.y = -1
        elif key[pygame.K_s]: self.direction.y = 1
        else: self.direction.y = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        #self.rect.center += self.direction * speed
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: #moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: #moving left
                        self.rect.left = sprite.rect.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: #moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: #moving up
                        self.rect.top = sprite.rect.bottom
    def update(self):
        self.input()
        self.move(self.speed)
        