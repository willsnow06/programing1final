import pygame

from wall import Wall

from character import Character

from enemy import Enemie

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('game')

x = 225
y = 225
ex = -200
ey = -200
hx = 500
hy = 500
vel = 0
evel = 0
startScreen = True
go21 = True
killed21 = False

go22 = True
killed22 = False

go32 = True
killed32 = False

go20 = True
killed20 = False

go30 = True
killed30 = False

gameOver = False
gameEnd = False
width = 50
height = 50
kills = 0

levelx = 1
levely = 1

wall1x = 0
wall1y = 0
wall1w = 100
wall1h = 50

wall2x = 0
wall2y = 0
wall2w = 50
wall2h = 100

wall3x = 0
wall3y = 450
wall3w = 100
wall3h = 50

wall4x = 0
wall4y = 400
wall4w = 50
wall4h = 100

wall5x = 450
wall5y = 0
wall5w = 50
wall5h = 100

wall6x = 400
wall6y = 0
wall6w = 100
wall6h = 50

wall7x = 450
wall7y = 400
wall7w = 50
wall7h = 100

wall8x = 400
wall8y = 450
wall8w = 100
wall8h = 50

wall1 = Wall(wall1x, wall1y, wall1w, wall1h, win)
wall2 = Wall(wall2x, wall2y, wall2w, wall2h, win)
wall3 = Wall(wall3x, wall3y, wall3w, wall3h, win)
wall4 = Wall(wall4x, wall4y, wall4w, wall4h, win)
wall5 = Wall(wall5x, wall5y, wall5w, wall5h, win)
wall6 = Wall(wall6x, wall6y, wall6w, wall6h, win)
wall7 = Wall(wall7x, wall7y, wall7w, wall7h, win)
wall8 = Wall(wall8x, wall8y, wall8w, wall8h, win)

image = pygame.image
background = pygame.image.load(r'bricks.jpg')
gameover = pygame.image.load(r'game_over.jpg')
gameend = pygame.image.load(r'winscreen.jpg')
start = pygame.image.load(r'start_screen.jpg')
hole = pygame.image.load(r'hole.png')
sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont(None, 48)
left = bool
right = bool


run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.blit(background, (0, 0))
    if levelx == 3 and levely == 1:
        hx = -20
        hy = 50
    else:
        hx = 500
        hy = 500
    key = pygame.key.get_pressed()
    img = font.render(f'{kills}', True, (0, 0, 0))
    if right == True:
        left = False
    if left == True:
        right = False

    if key[pygame.K_LEFT] or key[pygame.K_a]:
        x -= vel
        left = True
        right = False
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        x += vel
        right = True
        left = False
    if key[pygame.K_UP] or key[pygame.K_w]:
        y -= vel
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        y += vel

    dude = Character(x, y, width, height, win)
    enemy = Enemie(ex, ey, 30, 30, win)



    if x <= 0:
        levelx = levelx + 1
        x = 499

    if x >= 500:
        levelx = levelx - 1
        x = 1

    if y <= 0:
        levely = levely + 1
        y = 499

    if y >= 500:
        levely = levely - 1
        y = 1

    if key[pygame.K_SPACE]:
        dude.attack = True
        if ex >= x - width and ex <= x + width and ey >= y - height and ey <= y + height:
            evel = 0
            ex = -100
            ey = -100
            kills = kills + 1
            if levelx == 2 and levely == 1:
              killed21 = True
            if levelx == 2 and levely == 2:
              killed22 = True
            if levelx == 3 and levely == 2:
              killed32 = True
            if levelx == 2 and levely == 0:
              killed20 = True
            if levelx == 3 and levely == 0:
              killed30 = True
        vel = 0
        startScreen = False
        if right:
            image = pygame.image.load(r'attack.png')
        if left:
            image = pygame.image.load(r'attackInverse.png')
        if gameOver:
          x = 225
          y = 225
          ex = -200
          ey = -200
          hx = 500
          hy = 500
          vel = 25
          evel = 0
          go21 = True
          killed21 = False

          go22 = True
          killed22 = False

          go32 = True
          killed32 = False

          go20 = True
          killed20 = False
          go30 = True
          killed30 = False
          width = 50
          height = 50
          kills = 0
          levelx = 1
          levely = 1 
          gameOver = False
          gameEnd = False   
        if gameEnd:
          x = 225
          y = 225
          ex = -200
          ey = -200
          hx = 500
          hy = 500
          vel = 25
          evel = 0
          go21 = True
          killed21 = False
          go22 = True
          killed22 = False
          go32 = True
          killed32 = False
          go20 = True
          killed20 = False
          go30 = True
          killed30 = False
          width = 50
          height = 50
          kills = 0
          levelx = 1
          levely = 1 
          gameOver = False
          gameEnd = False 
          killed32 = False
          go32 = True

    else:
        dude.attack = False
        vel = 25
        if right:
            image = pygame.image.load(r'sword_dude.png')
        if left:
            image = pygame.image.load(r'sword_dudeInverse.png')

    walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8]

    if levelx == 1 and levely == 1:
        go21 = True
        go22 = True
        go20 = True
        go30 = True
        go32 = True

        ex = -200
        ey = -200
        evel = 0
        wall1.w = 250
        wall1.h = 50
        wall1.x = 0
        wall1.y = 0

        wall2.x = 0
        wall2.y = 0
        wall2.w = 50
        wall2.h = 100

        wall3.w = 250
        wall3.h = 50
        wall3.x = 0
        wall3.y = 450

        wall4.x = 0
        wall4.y = 400
        wall4.w = 50
        wall4.h = 100

        wall5.h = 250
        wall5.w = 50
        wall5.x = 450
        wall5.y = 0

        wall6.x = 250
        wall6.w = 250
        wall6.h = 50
        wall6.y = 0

        wall7.y = 250
        wall7.h = 250
        wall7.x = 450
        wall7.w = 50

        wall8.x = 250
        wall8.w = 250
        wall8.h = 50
        wall8.y = 450

    if levelx == 2 and levely == 1:
        go22 = True
        go32 = True
        go20 = True
        go30 = True
        if go21 == True:
            ex = 250
            ey = 250
            evel = 1
        if killed21 == True and levelx == 2 and levely == 1:
          ex = -200
          ey = -200
          evel = 0
        go21 = False
        wall1.x = 0
        wall1.y = 0
        wall1.w = 100
        wall1.h = 50

        wall2.x = 0
        wall2.y = 0
        wall2.w = 50
        wall2.h = 100

        wall3.x = 0
        wall3.y = 450
        wall3.w = 100
        wall3.h = 50

        wall4.x = 0
        wall4.y = 400
        wall4.w = 50
        wall4.h = 100

        wall5.x = 450
        wall5.y = 0
        wall5.w = 50
        wall5.h = 100

        wall6.x = 400
        wall6.y = 0
        wall6.w = 100
        wall6.h = 50

        wall7.x = 450
        wall7.y = 400
        wall7.w = 50
        wall7.h = 100

        wall8.x = 400
        wall8.y = 450
        wall8.w = 100
        wall8.h = 50

    if levelx == 3 and levely == 1:
        go21 = True
        go22 = True
        go20 = True
        go30 = True
        go32 = True
        if kills == 5 and x <= 350:
            gameEnd = True
        ex = -200
        ey = -200
        evel = 0
        wall1.x = 0
        wall1.y = 0
        wall1.w = 250
        wall1.h = 50

        wall2.x = 0
        wall2.y = 0
        wall2.w = 50
        wall2.h = 250

        wall3.x = 0
        wall3.y = 450
        wall3.w = 250
        wall3.h = 50

        wall4.x = 0
        wall4.y = 250
        wall4.w = 50
        wall4.h = 250

        wall5.x = 450
        wall5.y = 0
        wall5.w = 50
        wall5.h = 100

        wall6.x = 250
        wall6.y = 0
        wall6.w = 250
        wall6.h = 50

        wall7.x = 450
        wall7.y = 400
        wall7.w = 50
        wall7.h = 100

        wall8.x = 250
        wall8.y = 450
        wall8.w = 250
        wall8.h = 50

    if levelx == 2 and levely == 0:
        go21 = True
        go22 = True
        go32 = True
        go30 = True
        if go20 == True:
          ex = 250
          ey = 250
          evel = 1
        if killed20 == True and levelx == 2 and levely == 0:
          ex = -200
          ey = -200
          evel = 0
        go20 = False
        wall1.x = 0
        wall1.y = 0
        wall1.w = 100
        wall1.h = 50

        wall2.x = 0
        wall2.y = 0
        wall2.w = 50
        wall2.h = 100

        wall3.x = 0
        wall3.y = 450
        wall3.w = 250
        wall3.h = 50

        wall4.x = 0
        wall4.y = 400
        wall4.w = 50
        wall4.h = 100

        wall5.x = 450
        wall5.y = 0
        wall5.w = 50
        wall5.h = 250

        wall6.x = 400
        wall6.y = 0
        wall6.w = 100
        wall6.h = 50

        wall7.x = 450
        wall7.y = 250
        wall7.w = 50
        wall7.h = 250

        wall8.x = 250
        wall8.y = 450
        wall8.w = 250
        wall8.h = 50

    if levelx == 3 and levely == 0:
        go21 = True
        go22 = True
        go32 = True
        go20 = True
        if go30 == True:
          ex = 250
          ey = 250
          evel = 1
        if killed30 == True and levelx == 3 and levely == 0:
          ex = -200
          ey = -200
          evel = 0
        go30 = False
        wall1.x = 0
        wall1.y = 0
        wall1.w = 250
        wall1.h = 50

        wall2.x = 0
        wall2.y = 0
        wall2.w = 50
        wall2.h = 250

        wall3.x = 0
        wall3.y = 450
        wall3.w = 250
        wall3.h = 50

        wall4.x = 0
        wall4.y = 250
        wall4.w = 50
        wall4.h = 250

        wall5.x = 450
        wall5.y = 0
        wall5.w = 50
        wall5.h = 100

        wall6.x = 250
        wall6.y = 0
        wall6.w = 250
        wall6.h = 50

        wall7.x = 450
        wall7.y = 400
        wall7.w = 50
        wall7.h = 100

        wall8.x = 250
        wall8.y = 450
        wall8.w = 250
        wall8.h = 50

    if levelx == 2 and levely == 2:
        go21 = True
        go20 = True
        go30 = True
        go32 = True
        g032 = True
        if go22 == True:
            ex = 250
            ey = 250
            evel = 1
        if killed22 == True and levelx == 2 and levely == 2:
          ex = -200
          ey = -200
          evel = 0
        go22 = False
        wall1.w = 250
        wall1.h = 50
        wall1.x = 0
        wall1.y = 0

        wall2.x = 0
        wall2.y = 0
        wall2.w = 50
        wall2.h = 100

        wall3.w = 100
        wall3.h = 50
        wall3.x = 0
        wall3.y = 450

        wall4.x = 0
        wall4.y = 400
        wall4.w = 50
        wall4.h = 100

        wall5.h = 250
        wall5.w = 50
        wall5.x = 450
        wall5.y = 0

        wall6.x = 250
        wall6.w = 250
        wall6.h = 50
        wall6.y = 0

        wall7.y = 250
        wall7.h = 250
        wall7.x = 450
        wall7.w = 50

        wall8.x = 400
        wall8.w = 100
        wall8.h = 50
        wall8.y = 450

    if levelx == 3 and levely == 2:
        go21 = True
        go30 = True
        go22 = True
        go20 = True
        if go32 == True:
         ex = 250
         ey = 250
         evel = 1
        if killed32 == True and levelx == 3 and levely == 2:
          ex = -200
          ey = -200
          evel = 0
        else:
          if go32 == True:
            ex = 250
            ey = 250
            evel = 1
        go32 = False
        wall1.x = 0
        wall1.y = 0
        wall1.w = 250
        wall1.h = 50

        wall2.x = 0
        wall2.y = 0
        wall2.w = 50
        wall2.h = 250

        wall3.x = 0
        wall3.y = 450
        wall3.w = 250
        wall3.h = 50

        wall4.x = 0
        wall4.y = 250
        wall4.w = 50
        wall4.h = 250

        wall5.x = 450
        wall5.y = 0
        wall5.w = 50
        wall5.h = 100

        wall6.x = 250
        wall6.y = 0
        wall6.w = 250
        wall6.h = 50

        wall7.x = 450
        wall7.y = 400
        wall7.w = 50
        wall7.h = 100

        wall8.x = 250
        wall8.y = 450
        wall8.w = 250
        wall8.h = 50
        
    win.blit(hole, (hx, hy))

    for Wall in walls:
        wall = Wall
        wall.display()
        dude.rightSide(wall)
        enemy.erightSide(wall)
        dude.leftSide(wall)
        enemy.eleftSide(wall)
        dude.topSide(wall)
        enemy.etopSide(wall)
        dude.bottomSide(wall)
        enemy.ebottomSide(wall)
        enemy.dRight(dude)
        enemy.dLeft(dude)
        enemy.dTop(dude)
        enemy.dBottom(dude)
        win.blit(image, (x - dude.w, y - dude.h))
        enemy.display()
        if dude.right:
            x = x + vel

        if dude.left:
            x = x - vel

        if dude.top:
            y = y - vel

        if dude.bottom:
            y = y + vel

        # enemy
        if enemy.right:
            ex = ex + vel

        if enemy.left:
            ex = ex - vel

        if enemy.top:
            ey = ey - vel

        if enemy.bottom:
            ey = ey + vel
        # tracking
        if enemy.dright:
            ex = ex - evel

        if enemy.dleft:
            ex = ex + evel

        if enemy.dtop:
            ey = ey + evel

        if enemy.dbottom:
            ey = ey - evel
        if ex <= x + 10 and ey <= y + 10 and ex >= x - 10 and ey >= y - 10:
            gameOver = True

    if gameOver:
        vel = 0
        evel = 0
        win.blit(gameover, (0, 0))

    if startScreen:
      win.blit(start, (0, 0))
      vel = 0
    else:
      win.blit(start, (600, 600))
      vel = 25

    if gameEnd:
        win.blit(gameend, (0, 0))
        vel = 0
        evel = 0
    win.blit(img, (20, 20))
    pygame.display.update()

pygame.quit()






