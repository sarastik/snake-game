import os, sys
import pygame
import random

if not pygame.font: print "Warning, fonts disabled"
if not pygame.mixer: print "Warning, sound disabled"

RESOLUTION = (600, 600)
DIRECT_DICT = {pygame.K_LEFT: (-1, 0),
               pygame.K_RIGHT: (1, 0),
               pygame.K_UP: (0, -1),
               pygame.K_DOWN: (0, 1)}

class Snake(pygame.sprite.Sprite):
    """Handles initialization of the game."""

    def __init__(self, rect, speed, direction = pygame.K_UP):
        """rect is the snake's location and dimension,
           speed is speed of player in pixels/frame,
           and direction is starting direction"""
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(rect)
        self.speed = speed
        self.direction = direction
        self.collision_direction = None
        self.old_direction = None #previous direction every frame
        self.direction_stack = []
        self.redraw = False #force redraw if needed
        self.image = None
        self.frame = 0
        self.frames = self.get_frames()
        self.walkframes = []
        self.walkframe_dict = self.make_frame_dict()
        self.adjust_images()

    def get_frames(self):
        """Get a list of all frames"""
        sheet = SNAKE
        indices = [[0, 0], [1, 0], [2, 0], [3, 0]]
        return get_images(sheet, indices, self.rect.size)

    def make_frame_dict(self):
        """Assign frames to direction keys"""
        frames = {pygame.K_LEFT: [pygame.transform.rotate(self.frames[0], 90)],
                  pygame.K_RIGHT: [pygame.transform.rotate(self.frames[0], 270)],
                  pygame.K_UP: [self.frames[0]],
                  pygame.K_DOWN: [pygame.transform.rotate(self.frames[0], 180)]}
        return frames

    def adjust_images(self):
        """Update the walkframes as direction changes"""
        if self.direction != self.old_direction:
            self.walkframes = self.walkframe_dict[self.direction]
            self.old_direction = self.direction
            self.redraw = True
        self.make_image()

    def make_image(self):
        """Update the sprite's animation as needed"""
        if self.redraw:
            if self.direction_stack:
                self.frame = (self.frame+1)%len(self.walkframes)
                self.image = self.walkframes[self.frame]
        if not self.image:
            self.image = self.walkframes[self.frame]
        self.redraw = False
        
    def add_direction(self, key):
        """Add a pressed direction key on the direction stack"""
        if key in DIRECT_DICT:
            if key in self.direction_stack:
                self.direction_stack.remove(key)
            self.direction_stack.append(key)
            self.direction = self.direction_stack[-1]

    def pop_direction(self, key):
        """Pop a released key from the direction stack"""
        if key in DIRECT_DICT:
            if key in self.direction_stack:
                self.direction_stack.remove(key)
            if self.direction_stack:
                self.direction = self.direction_stack[-1]

    def update(self, screen_rect):
        """Updates the snake"""
        self.adjust_images()
        if self.direction_stack:
            direction_vector = DIRECT_DICT[self.direction]
            self.rect.x += self.speed*direction_vector[0]
            self.rect.y += self.speed*direction_vector[1]
            self.rect.clamp_ip(screen_rect)
        
    def draw(self, surface):
        """Draws snake to target surface"""
        surface.blit(self.image, self.rect)
            
class Control():
    
    def __init__(self):
        """Initialize standard attributes"""
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.done = False
        self.keys = pygame.key.get_pressed()
        self.snake = Snake((0, 0, 30, 30), 2)
        self.snake.rect.center = self.screen_rect.center

    def event_loop(self):
        """Add/pop directions from stack"""
        for event in pygame.event.get():
            self.keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.snake.add_direction(event.key)
            elif event.type == pygame.KEYUP:
                self.snake.pop_direction(event.key)

    def main_loop(self):
        """Main game loop"""
        while not self.done:
            self.event_loop()
            self.snake.update(self.screen_rect)
            self.screen.blit(BACKGROUND, (0,0))
            self.snake.draw(self.screen)
            pygame.display.update()

def get_images(sheet, frame_indices, size):
    """Get images from a sprite sheet"""
    frames = []
    for cell in frame_indices:
        frame_rect = ((size[0]*cell[0], size[1]*cell[1]), size)
        frames.append(sheet.subsurface(frame_rect))
    return frames
        
def main():
    """Initialize, load images, run program"""
    global BACKGROUND, MEAT, SNAKE
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_mode(RESOLUTION)
    BACKGROUND = pygame.image.load("sand.png").convert()
    MEAT = pygame.image.load("meat.png").convert()
    SNAKE = pygame.image.load("snake.png").convert()
    run_it = Control()
    run_it.main_loop()
    pygame.quit()
    sys.exit()
        

if __name__ == "__main__":
    main()
