import pygame as pg
import snakeblock
import control

DIRECT_DICT = {pg.K_LEFT: (-1, 0),
               pg.K_RIGHT: (1, 0),
               pg.K_UP: (0, -1),
               pg.K_DOWN: (0, 1)}

class Snake():

    def __init__(self, center, starting_direction = pg.K_UP):
        front = snakeblock.SnakeBlock("head", (0, 0, 30, 30), pg.K_UP, pg.K_DOWN)
        front.rect.center = center
        mid_rect = front.rect.move(0, 30)
        end_rect = mid_rect.move(0, 30)
        middle = snakeblock.SnakeBlock("straight", mid_rect, pg.K_UP, pg.K_DOWN)
        end = snakeblock.SnakeBlock('tail', end_rect, pg.K_UP, pg.K_DOWN)
        self.sprites = [front, middle, end]
        self.direction = starting_direction
        self.old_direction = pg.K_UP

        self.key_check = False
        self.dead = False
        self.grow = False

    #Sets the direction after a key is pressed
    def change_direction(self, key):
        if key in DIRECT_DICT:
            self.direction = key

    def add(self, sprite):
        self.sprites.insert(0, sprite)

    def update(self, screen_rect):
        if opposite(self.direction, self.old_direction):
            self.direction = self.old_direction

        #Once the first key has been pressed    
        if self.key_check:

            #If the snake is turning
            if self.direction != self.old_direction:
                neck_rect = self.sprites[0].rect
                self.sprites[0] = snakeblock.SnakeBlock("bend",
                                                        neck_rect,
                                                        self.direction,
                                                        self.old_direction)
                self.old_direction = self.direction

            #If the snake is going straight     
            else:
                neck_rect = self.sprites[0].rect
                self.sprites[0] = snakeblock.SnakeBlock("straight",
                                                        neck_rect,
                                                        self.direction,
                                                        self.old_direction)

            #The head gets added in the front
            x = DIRECT_DICT[self.direction][0]
            y = DIRECT_DICT[self.direction][1]
            front_rect = self.sprites[0].rect.move(x*30, y*30)
            front = snakeblock.SnakeBlock("head", front_rect,
                                          self.direction, self.old_direction)
            self.add(front)
            for block in self.sprites[1:]:
                if block.rect.collidepoint(front_rect.midtop):
                    self.dead = True

            #Grows when necessary, keeping tail at the end
            if not self.grow:
                self.sprites.pop()
            end_rect = self.sprites[-1].rect
            self.sprites[-1] = snakeblock.SnakeBlock("tail", end_rect,
                                                     self.sprites[-2].direct_from,
                                                     self.old_direction)
            self.grow = False
            
        #Checks for collision with screen edges
        clamped = self.sprites[0].rect.clamp(screen_rect)
        if clamped != self.sprites[0].rect:
            self.dead = True

def opposite(dir1, dir2):
    dead_list = [(pg.K_UP, pg.K_DOWN), (pg.K_DOWN, pg.K_UP),
                 (pg.K_RIGHT, pg.K_LEFT), (pg.K_LEFT, pg.K_RIGHT)]
    return (dir1, dir2) in dead_list
        
        
    
