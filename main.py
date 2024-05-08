'''
import pygame
import easygui

#Tile pixel = 16x16
#set
pygame.init()

#fps
clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill((255, 255, 255))
pygame.display.set_caption('山海和一遊戲')

#class
class Structure:
    def __init__(self, image = str, name = str, high_level = int, cost = int, cost_per_upgrade = int):
        self.image = image
        self.name = name
        self.high_level = high_level
        self.cost = cost
        self.cost_per_upgrade = cost_per_upgrade

class Build:
    def __init__(self, building = Structure(), level = int, x = int, y = int):
        self.type = building
        self.level = level
        self.next_cost = self.type.cost + self.type.cost_per_upgrade
        self.image = self.type.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def upgrade(self, money):
        if self.level == self.type.high_level and money >= self.next_cost:
            return False
        else:
            self.level = self.level + 1
            return True


class Button:
    def __init__(self, image, x = int, y = int):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

class GUI:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

class Background:
    def __init__(self, image, x = int, y = int):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

class BGtiles:
    def __init__(self, image, x = int, y = int):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y



#define
def createTileList():
    temp = []
    for i in range(int(SCREEN_WIDTH/16)+1):
        for j in range(int(SCREEN_HEIGHT/16)+1):
            temp.append([i,j])
            #pygame.draw.circle(screen, (0,0,0), (i*16+5,j*16+5), 5)
    return temp

def tileListInit():
    temp = []
    for x in range(len(tileposList)):
        temp.append("0002")
    return temp

def createTiles(list):
    tempx = 0
    for x in range(len(list)):
        TILE = BGtiles("./assets/Tiles/tile_"+tilelist[tempx]+".png", tileposList[tempx][0]*16, tileposList[tempx][1]*16)
        screen.blit(TILE.image, (TILE.x, TILE.y))
        tempx += 1



#variables
TILE = None

#lists
tileposList = createTileList()
tilelist = tileListInit()
#run
run = True
createTiles(tileposList)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx, posy = pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())
            TILE = BGtiles("./assets/Tiles/tile_0006.png", posx/16*16-8, posy/16*16-8)
            screen.blit(TILE.image, (TILE.x, TILE.y))
    #screen.blit(TILE.image, (TILE.x, TILE.y))
    #createTiles(tileposList)
    pygame.display.update()
    clock.tick(144)
pygame.quit()

exit()
'''
import pygame
import math
def main(budget = int, infinity = bool, elec = float, envi = float):
    pygame.init()
    pygame.font.init()
    FONT = pygame.font.Font('./assets/font/atop-font/Atop-R99O3.ttf', 70)
    clock = pygame.time.Clock()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((255, 255, 255))
    pygame.display.set_caption('山海和一遊戲')
    class BGtiles:
        def __init__(self, image, x = int, y = int):
            self.image = pygame.image.load(image)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
    #define
    def createTileList():
        temp = []
        for i in range(int(SCREEN_WIDTH/16)+1):
            for j in range(int(SCREEN_HEIGHT/16)+1):
                temp.append([i,j])
        return temp
    def tileListInit():
        temp = []
        for x in range(len(tileposList)):
            temp.append("0002")
        return temp
    def createTiles(list):
        tempx = 0
        for x in range(len(list)):
            TILE = BGtiles("./assets/Tiles/tile_"+tilelist[tempx]+".png", tileposList[tempx][0]*16, tileposList[tempx][1]*16)
            screen.blit(TILE.image, (TILE.x, TILE.y))
            tempx += 1
    def Showtext(font, text, color, x, y):
        text = font.render(text, True, color)
        textRect = text.get_rect(center = (x, y))
        screen.blit(text, textRect)
        
    #variables
    TILE = None
    #lists
    tileposList = createTileList()
    tilelist = tileListInit()
    #print(tileposList)
    #run
    run = True
    createTiles(tileposList)
    current = "2001"
    elec_add = 100
    envi_add = -60
    elec_point = 0
    envi_point = 100
    cost = 300
    while run:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if keys[pygame.K_1]:
                current = "2001"
                elec_add = 100
                envi_add = -60
                cost = 300
            if keys[pygame.K_2]:
                current = "2002"
                elec_add = 200
                envi_add = -100
                cost = 400
            if keys[pygame.K_3]:
                current = "2003"
                elec_add = 150
                envi_add = -90
                cost = 350
            if keys[pygame.K_4]:
                current = "2004"
                elec_add = 10000
                envi_add = -10
                cost = 10000
            if keys[pygame.K_5]:
                current = "2005"
                elec_add = 150
                envi_add = 50
                cost = 350
            if keys[pygame.K_6]:
                current = "2006"
                elec_add = 200
                envi_add = 100
                cost = 500
            if keys[pygame.K_7]:
                current = "2007"
                elec_add = 350
                envi_add = 150
                cost = 750
            if keys[pygame.K_8]:
                current = "2008"
                elec_add = 500
                envi_add = 300
                cost = 1000
            if keys[pygame.K_9]:
                current = "2009"
                elec_add = 5000
                envi_add = 0
                cost = 40000
            if keys[pygame.K_0]:
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = pygame.mouse.get_pos()
                if budget >= cost or infinity:
                    TILE = BGtiles("./assets/Tiles/tile_" + current + ".png", posx/16*16-8, posy/16*16-8)
                    
                    screen.blit(TILE.image, (TILE.x, TILE.y))
                    budget-=cost
                    elec_point+=elec_add
                    envi_point+=envi_add
        Showtext(FONT, "署", (0,0,0), 100, 100)
        pygame.display.update()
        clock.tick(144)
    pygame.quit()

    point = 0.0
    point = ((elec_point * elec / 100) + (envi_point * envi / 100)) * 10000000000
    if infinity:
        point /= 1000000
    else:
        point /= budget
    return point

main(9000, True, 50, 50)