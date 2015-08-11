import os
import sys
import pygame
import snake

RESOLUTION = (600, 600)

class Control():
    
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.done = False
        self.keys = pygame.key.get_pressed()
        self.snake = snake.Snake((0, 0, 30, 30), 2)
        self.snake.rect.center = self.screen_rect.center

    # Handles key events by adding to/popping from direction stack
    def event_loop(self):
        for event in pygame.event.get():
            self.keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.snake.add_direction(event.key)
            elif event.type == pygame.KEYUP:
                self.snake.pop_direction(event.key)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.snake.update(self.screen_rect)
            self.screen.blit(BACKGROUND, (0,0))
            self.snake.draw(self.screen)
            pygame.display.update()

def main():
    global BACKGROUND, MEAT
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_mode(RESOLUTION)
    BACKGROUND = pygame.image.load("sand.png").convert()
    MEAT = pygame.image.load("meat.png").convert()
    run_it = Control()
    run_it.main_loop()
    pygame.quit()
    sys.exit()
        

if __name__ == "__main__":
    main()
