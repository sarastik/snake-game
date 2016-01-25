import pygame as pg

class SnakeBlock():

    def __init__(self, snake, part, rect, direct_to, direct_from, dead):
        self.part = part #straight, bend, head, tail
        self.rect = pg.Rect(rect)
        self.direct_to = direct_to
        self.direct_from = direct_from
        self.dead = dead

        # Get the frames from the sprite sheet
        if snake == 0: #normal snake
            self.sheet = pg.image.load("sprites/snake.png").convert()
        elif snake == 1: #coral snake
            self.sheet = pg.image.load("sprites/coral_snake.png").convert()
        indices = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
        self.frames = get_images(self.sheet, indices, self.rect.size)

        self.image = self.get_image()

    def get_image(self):
        if self.part == "bend":
            directs = (self.direct_to, self.direct_from)
            if directs == (pg.K_UP, pg.K_RIGHT) or \
               directs == (pg.K_LEFT, pg.K_DOWN):
                return pg.transform.rotate(self.frames[1], 270)
            elif directs == (pg.K_UP, pg.K_LEFT) or \
                 directs == (pg.K_RIGHT, pg.K_DOWN):
                return pg.transform.rotate(self.frames[1], 180)
            elif directs == (pg.K_LEFT, pg.K_UP) or \
                 directs == (pg.K_DOWN, pg.K_RIGHT):
                return self.frames[1]
            elif directs == (pg.K_RIGHT, pg.K_UP) or \
                 directs == (pg.K_DOWN, pg.K_LEFT):
                return pg.transform.rotate(self.frames[1], 90)
        elif self.part == "head":
            head_sprite = self.frames[4] if self.dead else self.frames[0]
            if self.direct_to == pg.K_UP:
                return head_sprite
            elif self.direct_to == pg.K_RIGHT:
                return pg.transform.rotate(head_sprite, 270)
            elif self.direct_to == pg.K_LEFT:
                return pg.transform.rotate(head_sprite, 90)
            else:
                return pg.transform.rotate(head_sprite, 180)
        elif self.part == "tail":
            if self.direct_to == pg.K_UP:
                return self.frames[3]
            elif self.direct_to == pg.K_RIGHT:
                return pg.transform.rotate(self.frames[3], 270)
            elif self.direct_to == pg.K_LEFT:
                return pg.transform.rotate(self.frames[3], 90)
            else:
                return pg.transform.rotate(self.frames[3], 180)
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
        
        
