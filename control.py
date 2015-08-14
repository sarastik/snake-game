import os
import sys
import pygame as pg
import snake
import snakeblock

class Control():
    
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        pg.display.set_mode((600, 600))
        self.background = pg.image.load("sand.png").convert()
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.done = False
        self.keys = pg.key.get_pressed()
        self.snake = snake.Snake(self.screen_rect.center)        

    # Handles key presses and quitting
    def event_loop(self):
        for event in pg.event.get():
            self.keys = pg.key.get_pressed()
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.snake.key_check = True
                self.snake.change_direction(event.key)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            pg.time.delay(100)
            self.snake.update(self.screen_rect)
            self.screen.blit(self.background, (0,0))
            #self.screen.blit(self.snake.image, self.snake.rect)
            for part in self.snake.sprites:
                self.screen.blit(part.image, part.rect)
            pg.display.update()

if __name__ == "__main__":
    run_it = Control()
    run_it.main_loop()
    pg.quit()
    sys.exit()
