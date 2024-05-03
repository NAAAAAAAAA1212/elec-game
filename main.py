import pygame
import pyautogui

class sturcture:
    def __init__(self):
        pass

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill((255, 255, 255))
pygame.display.set_caption('山海和一 電力供應局')

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
#==
