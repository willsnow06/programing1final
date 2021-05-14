import pygame

from wall import Wall

from character import Character

class Enemie:
  x = 0
  y = 0
  w = 0
  h = 0
  win = pygame.surface
  r = w
  wall = Wall
  character = Character
  right = bool
  left = bool
  top = bool
  bottom = bool
  dright = bool
  dleft = bool
  dtop = bool
  dbottom = bool

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
    self.dright = bool
    self.dleft = bool
    self.dtop = bool
    self.dbottom = bool

    #displays the character

  def display(self):
    pygame.draw.circle(self.win, (255, 255, 0), (self.x, self.y), self.w)

    #this is where the collision detection starts

  def erightSide(self, wall):
    self.wall = wall

    if self.x - self.w <= self.wall.x + self.wall.w and self.y >= self.wall.y and self.y <= self.wall.y + self.wall.h and self.x + self.w >= self.wall.x + self.wall.w:
      self.right = True
    else:
      self.right = False

  def eleftSide(self, wall):
    self.wall = wall
    
    if self.x + self.w >= self.wall.x and self.y >= self.wall.y and self.y <= self.wall.y + self.wall.h and self.x - self.w <= self.wall.x:
      self.left = True
    else:
      self.left = False

  def etopSide(self, wall):
    self.wall = wall

    if self.y + self.h >= self.wall.y and self.x >= self.wall.x and self.x <= self.wall.x + self.wall.w and self.y - self.h <= self.wall.y:
      self.top = True
    else:
      self.top = False

  def ebottomSide(self, wall):
    self.wall = wall

    if self.y - self.h <= self.wall.y + self.wall.h and self.x >= self.wall.x and self.x <= self.wall.x + self.wall.w and self.y + self.h >= self.wall.y + self.wall.h:
      self.bottom = True
    else:
      self.bottom = False
  
  #movement towards character
  def dRight(self, character):
    self.character = character
    if self.x > self.character.x:
      self.dright = True
    else:
      self.dright = False

  def dLeft(self, character):
    self.character = character
    if self.x < self.character.x:
      self.dleft = True
    else:
      self.dleft = False

  def dTop(self, character):
    self.character = character
    if self.y < self.character.y:
      self.dtop = True
    else:
      self.dtop = False

  def dBottom(self, character):
    self.character = character
    if self.y > self.character.y:
      self.dbottom = True
    else:
      self.dbottom = False
      
