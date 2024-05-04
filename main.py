import pygame


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
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #screen.blit(TILE.image, (TILE.x, TILE.y))
    createTiles(tileposList)
    pygame.display.update()
    clock.tick(90)
pygame.quit()

