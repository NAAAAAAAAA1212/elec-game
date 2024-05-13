def main(budget = int, infinity = bool, elec = float, envi = float):
    import pygame
    pygame.init()
    clock = pygame.time.Clock()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    pygame.font.init()
    FONT = pygame.font.Font('./assets/font/华文楷体.ttf', 50)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
            tile = BGtiles("./assets/Tiles/tile_"+tilelist[tempx]+".png", tileposList[tempx][0]*16, tileposList[tempx][1]*16)
            screen.blit(tile.image, (tile.x, tile.y))
            tempx += 1
    def showtext(font, text, color, x, y):
    
        showtext_ = font.render(text, True, color)
        textRect = showtext_.get_rect(center = (x, y))
        screen.blit(showtext_, textRect)
    #variables
    TILE = None
    text_x = SCREEN_WIDTH//2
    text_y = SCREEN_HEIGHT//2
    #lists
    tileposList = createTileList()
    tilelist = tileListInit()
    #run
    run = True
    current = "2001"
    elec_add = 100
    envi_add = -60
    elec_point = 0
    envi_point = 100
    cost = 300
    while run:
        #screen.fill((255, 255, 255))
        createTiles(tileposList)
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
        
    
        if infinity:
            showtext(FONT, "當前剩餘資金：無限", (0,0,0), text_x, text_y)
        else:
            showtext(FONT, "當前剩餘資金："+str(budget), (0,0,0), text_x, text_y)
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
