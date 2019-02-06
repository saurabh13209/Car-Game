import random 
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 3 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Game')


GREEN = (0, 250, 0)
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = ( 0, 0, 255)
GREY = (128, 128, 128)

car1Img = pygame.image.load('car1.bmp')                             #270   ,   380,   490
car1x = 380
car1y = 450

MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1

c = random.randint(1,3)
c1 = random.randint(1,3)

sc=1

run = 0

carImg = pygame.image.load('car.bmp')
carx = 270
cary = 10
direction = 'down'

car3Img = pygame.image.load('car.bmp')
car3x = 490
car3y = 300
direction = 'down'

car4Img = pygame.image.load('car.bmp')
car4x = 490
car4y = 500
direction = 'down'

houseImg = pygame.image.load('ho.bmp')
housex = 150
housey = 10
direction = 'down'

house1Img = pygame.image.load('ho.bmp')
house1x = 700
house1y = 310
direction = 'down'

expImg = pygame.image.load('exp.bmp')
expx = 830
expy = 400

explo =1

i=0


while True: # the main game loop
    
    DISPLAYSURF.fill(GREY)

    BIGFONT = pygame.font.Font('freesansbold.ttf', 40)
    yesSurf = BIGFONT.render('Start', True, BLACK )
    yesRect = yesSurf.get_rect()
    yesRect.center = (400,300)
    DISPLAYSURF.blit(yesSurf, yesRect)

    gameOverFont = pygame.font.Font('freesansbold.ttf', 60)
    gameSurf = gameOverFont.render('CAR GAME', True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.center = (400,100)
    DISPLAYSURF.blit(gameSurf, gameRect)

    BIGFONT = pygame.font.Font('freesansbold.ttf', 40)
    endSurf = BIGFONT.render('Quit', True, BLACK )
    endRect = yesSurf.get_rect()
    endRect.center = (400,400)
    DISPLAYSURF.blit(endSurf, endRect)

    while run >0:

        DISPLAYSURF.fill(GREEN)

        pygame.draw.rect(DISPLAYSURF, BLACK, (250, 0, 350, 695), 5)
        pygame.draw.rect(DISPLAYSURF, GREY, (253, 0, 344, 698))
        pixObj = pygame.PixelArray(DISPLAYSURF)
        pixObj[480][380] = BLACK

        del pixObj

        

        if direction == 'down':
            cary += 2
            car3y += 2
            car4y += 2
            housey +=2
            house1y +=2
            if cary == 680:
                cary = 10
                c = random.randint(1,3)
                if c==1:
                    carx = 270
                if c==2:
                    carx = 380
                if c==3:
                    carx= 490

                sc = sc+1

            if car3y == 680:
                car3y = 10
                c1 = random.randint(1,3)
                if c1==1:
                    car3x = 270
                if c1==2:
                    car3x = 380
                if c1==3:
                    car3x= 490

            if car4y == 680:
                car4y = 10
                c2 = random.randint(1,3)
                if c2==1:
                    car4x = 270
                if c2==2:
                    car4x = 380
                if c2==3:
                    car4x= 490
                
            
            if housey == 690:
                housey = 10
            if house1y == 690:
                house1y = 10

            if carx==car1x and cary==car1y-80 :
                expx = car1x
                expy = car1y
                explo += 1

                    
            if car3x==car1x and car3y==car1y-80 :
                expx = car1x
                expy = car1y
                explo += 1

            if car4x==car1x and car4y==car1y-80 :
                expx = car1x
                expy = car1y
                explo += 1

            scoreFont = pygame.font.Font('freesansbold.ttf', 15)
            scoreSurf = scoreFont.render('Score:' + str(sc), True, BLUE)
            scoreRect = scoreSurf.get_rect()
            scoreRect.topleft = (10, 40)
            DISPLAYSURF.blit(scoreSurf, scoreRect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    if car1x < 490:
                        car1x = car1x + 110

                if event.key == K_LEFT:
                    if car1x > 270:
                        car1x = car1x - 110

                if event.key == K_UP :
                    if car1y < 800:
                        if car1y > 325:
                            car1y = car1y-10
                if event.key == K_DOWN :
                    if car1y < 800:
                        if car1y > 325:
                            car1y = car1y+10
        
        DISPLAYSURF.blit(carImg, (carx, cary))
        DISPLAYSURF.blit(houseImg, (housex, housey))
        DISPLAYSURF.blit(house1Img, (house1x, house1y))
        DISPLAYSURF.blit(car1Img, (car1x, car1y))
        DISPLAYSURF.blit(car3Img, (car3x, car3y))
        DISPLAYSURF.blit(car3Img, (car4x, car4y))


        if explo > 1 :
            DISPLAYSURF.blit(expImg, (expx, expy))
            gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
            gameSurf = gameOverFont.render('Game', True, WHITE)
            overSurf = gameOverFont.render('Over', True, WHITE)
            gameRect = gameSurf.get_rect()
            overRect = overSurf.get_rect()
            gameRect.midtop = (800 / 2, 10)
            overRect.midtop = (800 / 2, gameRect.height + 10 + 25)

            DISPLAYSURF.blit(gameSurf, gameRect)
            DISPLAYSURF.blit(overSurf, overRect)
            pygame.time.wait(1000)


        pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if yesRect.collidepoint( (mousex, mousey) ):
                run = run+1

        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if endRect.collidepoint( (mousex, mousey) ):
                pygame.quit()
                sys.exit()

    

        pygame.display.update()
        






    
