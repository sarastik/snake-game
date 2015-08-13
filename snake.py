import pygame
import snakeblock

class Snake():

    def __init__(self, sprite):
        self.sprites = [sprite]

    def add(self, sprite):
        self.sprites.insert(0, sprite)
        # draw new part at the front of the snake

    def remove(self, sprite):
        self.sprites.pop(sprite)
        # clear this part from the end of the snake

    
