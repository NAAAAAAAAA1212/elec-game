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
    def __init__(self):
        self.image = None
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

class Button:
    def __init__(self):
        self.image = None
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

class GUI:
    def __init__(self):
        self.image = None
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

class Background:
    def __init__(self):
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
#==
