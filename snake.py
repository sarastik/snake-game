import pygame as pg
import snakeblock
import control

DIRECT_DICT = {pg.K_LEFT: (-1, 0),
               pg.K_RIGHT: (1, 0),
               pg.K_UP: (0, -1),
               pg.K_DOWN: (0, 1)}

class Snake():

    def __init__(self, center, starting_direction = pg.K_UP):
        front = snakeblock.SnakeBlock('straight', (0,0,30,30), pg.K_UP, pg.K_DOWN)
        front.rect.center = center
        mid_rect = front.rect.move(0, 30)
        end_rect = mid_rect.move(0, 30)
        middle = snakeblock.SnakeBlock('straight', mid_rect, pg.K_UP, pg.K_DOWN)
        end = snakeblock.SnakeBlock('straight', end_rect, pg.K_UP, pg.K_DOWN)
        self.sprites = [front, middle, end]
        self.direction = starting_direction
        self.old_direction = pg.K_UP
        self.key_check = False

    # Sets the direction after a key is pressed
    def change_direction(self, key):
        if key in DIRECT_DICT:
            self.direction = key    

    def add(self, sprite):
        self.sprites.insert(0, sprite)

    def update(self, screen_rect):
        if self.key_check:
            if self.direction != self.old_direction:
                neck_rect = self.sprites[1].rect
                self.sprites[1] = snakeblock.SnakeBlock('bend', neck_rect, self.direction, self.old_direction)
                self.old_direction = self.direction
            self.sprites.pop()
            x = DIRECT_DICT[self.direction][0]
            y = DIRECT_DICT[self.direction][1]
            front_rect = self.sprites[0].rect.move(x*30, y*30)
            front = snakeblock.SnakeBlock('straight', front_rect, self.direction, self.old_direction)
            self.add(front)
        
        
    
