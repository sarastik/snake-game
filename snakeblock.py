import os
import sys
import pygame as pg
import control

class SnakeBlock(pg.sprite.Sprite):

    def __init__(self, part, rect, direct_to, direct_from):
        pg.sprite.Sprite.__init__(self)

        self.part = part #straight, bend
        print rect
        self.rect = pg.Rect(rect)
        self.direct_to = direct_to
        self.direct_from = direct_from

        # Get the frames from the sprite sheet
        self.sheet = pg.image.load("snake.png").convert()
        indices = [[0, 0], [1, 0], [2, 0], [3, 0]]
        self.frames = get_images(self.sheet, indices, self.rect.size)

        self.image = self.get_image()

    def get_image(self):
        if self.part == 'bend':
            if self.direct_to == pg.K_UP and self.direct_from == pg.K_RIGHT:
                return pg.transform.rotate(self.frames[1], 270)
            elif self.direct_to == pg.K_UP and self.direct_from == pg.K_LEFT:
                return pg.transform.rotate(self.frames[1], 180)
            elif self.direct_to == pg.K_LEFT and self.direct_from == pg.K_UP:
                return self.frames[1]
            elif self.direct_to == pg.K_LEFT and self.direct_from == pg.K_DOWN:
                return pg.transform.rotate(self.frames[1], 270)
            elif self.direct_to == pg.K_RIGHT and self.direct_from == K_UP:
                return pg.transform.rotate(self.frames[1], 90)
            elif self.direct_to == pg.K_RIGHT and self.direct_from == K_DOWN:
                return pg.transform.rotate(self.frames[1], 180)
            elif self.direct_to == pg.K_DOWN and self.direct_from == K_RIGHT:
                return self.frames[1]
            elif self.direct_to == pg.K_DOWN and self.direct_from == K_LEFT:
                return pg.transform.rotate(self.frames[1], 90)
        else: #straight
            if self.direct_to == pg.K_UP or self.direct_to == pg.K_DOWN:
                return pg.transform.rotate(self.frames[2], 90)
            else:
                return self.frames[2]

# Get images from a sprite sheet
def get_images(sheet, frame_indices, size):
    frames = []
    for cell in frame_indices:
        frame_rect = ((size[0]*cell[0], size[1]*cell[1]), size)
        frames.append(sheet.subsurface(frame_rect))
    return frames
        
        
