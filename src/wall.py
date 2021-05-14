import pygame

#this is litterally just a rectangle
class Wall:
     x = 0
     y = 0
     w = 0
     h = 0
     win = pygame.surface

     def __init__(self, x, y, w, h, win):
          self.x = x
          self.y = y
          self.w = w
          self.h = h
          self.win = win

     def display(self):
          pygame.draw.rect(self.win, (255, 0, 0), (self.x, self.y, self.w, self.h))
