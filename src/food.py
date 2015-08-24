import pygame as pg
import random

class Food():

    def __init__(self, center, snake):
        self.snake = snake

        # Start with food above snake
        self.rect = pg.Rect((0, 0, 30, 30))
        self.rect.center = center
        self.rect = self.rect.move(0, -60)
        self.image = pg.image.load("sprites/meat.png").convert()
        self.sound = pg.mixer.Sound("sounds/bite.wav")

    def move(self):
        x = random.randint(0, 600)
        x = ((x/30) * 30) + 15
        y = random.randint(0, 600)
        y = ((y/30) * 30) + 15
        self.rect.center = (x, y)
        for block in self.snake.sprites:
            if self.rect.colliderect(block.rect):
                self.move()

    def update(self):
        if self.rect.colliderect(self.snake.sprites[0].rect):
            self.sound.play()
            self.move()
            self.snake.grow = True

    
