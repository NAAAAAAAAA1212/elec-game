import pygame
import os
import sys

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill((255, 255, 255))
pygame.display.set_caption('山海和一遊戲')

class Structure:
    def __init__(self, image = int, name = str, high_level = int, cost = int, cost_per_upgrade = int) -> None:
        self.image = image
        self.name = name
        self.high_level = high_level
        self.cost = cost
        self.cost_per_upgrade = cost_per_upgrade

class Build:
    def __init__(self, building = Structure(), level = int) -> None:
        self.type = building
        self.level = level
        self.next_cost = self.type.cost + self.type.cost_per_upgrade
        self.image = None
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def upgrade(self, money) -> bool:
        if self.level == self.type.high_level and money >= self.next_cost:
            return False
        else:
            self.level = self.level + 1
            return True


class Button:
    def __init__(self) -> None:
        self.image = None
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

class GUI:
    def __init__(self) -> None:
        self.image = None
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

class Background:
    def __init__(self) -> None:
        self.image = None
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

