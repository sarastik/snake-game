import os, sys
import pygame
import random
import control

if not pygame.font: print "Warning, fonts disabled"
if not pygame.mixer: print "Warning, sound disabled"

DIRECT_DICT = {pygame.K_LEFT: (-1, 0),
               pygame.K_RIGHT: (1, 0),
               pygame.K_UP: (0, -1),
               pygame.K_DOWN: (0, 1)}

class Snake(pygame.sprite.Sprite):

    """
    rect: snake's location and dimension, e.g. (0, 0, 30, 30)
    speed: speed of the snake in pixels/frame
    direction: starting direction
    """
    def __init__(self, rect, speed, direction = pygame.K_UP):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(rect)
        self.speed = speed
        
        self.old_direction = None
        self.direction = direction
        self.direction_stack = []
        self.redraw = False #force redraw if needed

        self.image = None
        self.frame = 0
        indices = [[0, 0], [1, 0], [2, 0], [3, 0]]
        self.sheet = pygame.image.load("snake.png").convert()
        self.frames = get_images(self.sheet, indices, self.rect.size)
        self.moveframes = []
        self.moveframe_dict = self.make_frame_dict()
        self.adjust_images()

    # Assigns frames to direction keys
    def make_frame_dict(self):
        frames = {pygame.K_LEFT: [pygame.transform.rotate(self.frames[0], 90)],
                  pygame.K_RIGHT: [pygame.transform.rotate(self.frames[0], 270)],
                  pygame.K_UP: [self.frames[0]],
                  pygame.K_DOWN: [pygame.transform.rotate(self.frames[0], 180)]}
        return frames

    # Updates the moveframes as direction changes
    def adjust_images(self):
        if self.direction != self.old_direction:
            self.moveframes = self.moveframe_dict[self.direction]
            self.old_direction = self.direction
            self.redraw = True
        self.make_image()

    # Update the sprite's animation as needed
    def make_image(self):
        if self.redraw:
            if self.direction_stack:
                self.frame = (self.frame+1)%len(self.moveframes)
                self.image = self.moveframes[self.frame]
        if not self.image:
            self.image = self.moveframes[self.frame]
        self.redraw = False

    # Add pressed direction to stack    
    def add_direction(self, key):
        if key in DIRECT_DICT:
            if key in self.direction_stack:
                self.direction_stack.remove(key)
            self.direction_stack.append(key)
            self.direction = self.direction_stack[-1]

    # Pop released direction from stack
    def pop_direction(self, key):
        if key in DIRECT_DICT:
            if key in self.direction_stack:
                self.direction_stack.remove(key)
            if self.direction_stack:
                self.direction = self.direction_stack[-1]

    # Updates snake movement
    def update(self, screen_rect):
        self.adjust_images()
        if self.direction_stack:
            direction_vector = DIRECT_DICT[self.direction]
            self.rect.x += self.speed*direction_vector[0]
            self.rect.y += self.speed*direction_vector[1]
            self.rect.clamp_ip(screen_rect)

    # Draws snake on surface    
    def draw(self, surface):
        surface.blit(self.image, self.rect)            

# Get images from a sprite sheet
def get_images(sheet, frame_indices, size):
    frames = []
    for cell in frame_indices:
        frame_rect = ((size[0]*cell[0], size[1]*cell[1]), size)
        frames.append(sheet.subsurface(frame_rect))
    return frames
