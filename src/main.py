import pygame

from wall import Wall

from character import Character

from enemy import Enemie



pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('game')


x = 225
y = 225
ex = 0
ey = 250
vel = 25
evel = 1

width = 50
height = 50

levelx = 1
levely = 1

wall1 = Wall(0, 0, 100, 50, win)
wall2 = Wall(0, 0, 50, 100, win)

wall3 = Wall(0, 450, 100, 50, win)
wall4 = Wall(0, 400, 50, 100, win)

wall5 = Wall(450, 0, 50, 100, win)
wall6 = Wall(400, 0, 100, 50, win)

wall7 = Wall(450, 400, 50, 100, win)
wall8 = Wall(400, 450, 100, 50, win) 

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8]

image = pygame.image
background = pygame.image.load(r'bricks.jpg')
left = bool
right = bool

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.blit(background, (0, 0))

    key = pygame.key.get_pressed()

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
    bruh = Enemie(ex, ey, 30, 30, win)

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
      vel = 0
      if right:
        image = pygame.image.load(r'attack.png')
      if left:
        image = pygame.image.load(r'attackInverse.png')
    else:
      dude.attack = False
      vel = 25
      if right:
        image = pygame.image.load(r'sword_dude.png')
      if left:
        image = pygame.image.load(r'sword_dudeInverse.png')

    for Wall in walls:
      wall = Wall
      wall.display()
      dude.rightSide(wall)
      bruh.erightSide(wall)
      dude.leftSide(wall)
      bruh.eleftSide(wall)
      dude.topSide(wall)
      bruh.etopSide(wall)
      dude.bottomSide(wall)
      bruh.ebottomSide(wall)
      bruh.dRight(dude)
      bruh.dLeft(dude)
      bruh.dTop(dude)
      bruh.dBottom(dude) 
      win.blit(image, (x - dude.w, y - dude.h))
      bruh.display()
      if dude.right:
        x  = x + vel
    
      if dude.left:
        x  = x - vel
    
      if dude.top:
        y = y - vel

      if dude.bottom:
        y = y + vel

      #enemy
      if bruh.right:
        ex  = ex + vel
    
      if bruh.left:
        ex  = ex - vel
    
      if bruh.top:
        ey = ey - vel

      if bruh.bottom:
        ey = ey + vel
      #tracking
      if bruh.dright:
        ex = ex - evel

      if bruh.dleft:
        ex = ex + evel

      if bruh.dtop:
        ey = ey + evel

      if bruh.dbottom:
        ey = ey - evel
    pygame.display.update()

pygame.quit()






