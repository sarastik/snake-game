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
        mid_rect = front.rect
        end_rect = front.rect
        mid_rect.center = (front.rect.centerx, front.rect.centery + 30)
        middle = snakeblock.SnakeBlock('straight', mid_rect, pg.K_UP, pg.K_DOWN)
        end_rect.center = (front.rect.centerx, middle.rect.centery + 30)
        end = snakeblock.SnakeBlock('straight', end_rect, pg.K_UP, pg.K_DOWN)
        self.sprites = [front, middle, end]
        self.direction = starting_direction
        self.old_direction = None
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
                self.old_direction = self.direction
                neck_rect = self.sprites[1].rect
                self.sprites[1] = snakeblock.SnakeBlock('bend', neck_rect, self.direction, self.old_direction)
            self.sprites.pop()
            if self.direction == pg.K_UP:
                centerx = self.sprites[0].rect.centerx
                centery = self.sprites[0].rect.centery + 30
            elif self.direction == pg.K_DOWN:
                centerx = self.sprites[0].rect.centerx
                centery = self.sprites[0].rect.centery - 30
            elif self.direction == pg.K_RIGHT:
                centerx = self.sprites[0].rect.centerx + 30
                centery = self.sprites[0].rect.centery
            else: #can only be left?
                centerx = self.sprites[0].rect.centerx - 30
                centery = self.sprites[0].rect.centery
            front_rect = self.sprites[0].rect.center(centerx, centery)
            self.sprites.add('straight', front_rect, self.direction, self.old_direction)
        
        
    
