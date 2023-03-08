import pygame as pg
from graph import *
class Ball:
    
        def __init__(self, x, y, radius, color):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
    
        def draw(self, screen):
            pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
        def move(self, x ,y):
            self.x = x
            self.y = y
        
       