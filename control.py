import os
import sys
import pygame
import snake
import snakeblock

class Control():
    
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_mode((600, 600))
        self.background = pygame.image.load("sand.png").convert()
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.done = False
        self.keys = pygame.key.get_pressed()
        snake_part = snakeblock.SnakeBlock('straight', (0,0,30,30), 1)
        self.snake = snake_part
        self.snake.rect.center = self.screen_rect.center

    # Handles key presses and quitting
    def event_loop(self):
        for event in pygame.event.get():
            self.keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.snake.key_check = True
                self.snake.change_direction(event.key)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.snake.update(self.screen_rect)
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.snake.image, self.snake.rect)
            pygame.display.update()

if __name__ == "__main__":
    run_it = Control()
    run_it.main_loop()
    pygame.quit()
    sys.exit()
