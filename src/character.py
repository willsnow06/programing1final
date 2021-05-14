import pygame

from wall import Wall

class Character:
  x = 0
  y = 0
  w = 0
  h = 0
  win = pygame.surface
  r = w
  wall = Wall
  right = bool
  left = bool
  top = bool
  bottom = bool
  attack = bool

  def __init__(self, x, y, w, h, win):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.r = w
    self.win = win
    self.right = bool
    self.left = bool
    self.top = bool
    self.bottom = bool
    self.attack = bool

    #displays the character

  def display(self):
    color = (0, 255, 0)
    if self.attack == True:
      color = (0, 0, 255)
    else:
      color = (0, 255, 0)
    pygame.draw.circle(self.win, color, (self.x, self.y), self.w)

    #this is where the collision detection starts

  def rightSide(self, wall):
    self.wall = wall

    if self.x - self.w <= self.wall.x + self.wall.w and self.y >= self.wall.y and self.y <= self.wall.y + self.wall.h and self.x + self.w >= self.wall.x + self.wall.w:
      self.right = True
    else:
      self.right = False

  def leftSide(self, wall):
    self.wall = wall
    
    if self.x + self.w >= self.wall.x and self.y >= self.wall.y and self.y <= self.wall.y + self.wall.h and self.x - self.w <= self.wall.x:
      self.left = True
    else:
      self.left = False

  def topSide(self, wall):
    self.wall = wall

    if self.y + self.h >= self.wall.y and self.x >= self.wall.x and self.x <= self.wall.x + self.wall.w and self.y - self.h <= self.wall.y:
      self.top = True
    else:
      self.top = False

  def bottomSide(self, wall):
    self.wall = wall

    if self.y - self.h <= self.wall.y + self.wall.h and self.x >= self.wall.x and self.x <= self.wall.x + self.wall.w and self.y + self.h >= self.wall.y + self.wall.h:
      self.bottom = True
    else:
      self.bottom = False
