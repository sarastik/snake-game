import os
import sys
import pygame as pg
import snake
import snakeblock
import food

class Control():
    
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        pg.display.set_mode((630, 630))
        self.background = pg.image.load("sand.png").convert()
        self.game_over = pg.image.load("game_over.png").convert()
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.done = False
        self.keys = pg.key.get_pressed()
        self.snake = snake.Snake(self.screen_rect.center)
        self.food = food.Food(self.screen_rect.center, self.snake)

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

            if self.snake.dead:
                self.screen.blit(self.game_over, (0,0))
            else:
                pg.time.delay(100) #for effect and slower speed
                self.snake.update(self.screen_rect)
                self.food.update()
                self.screen.blit(self.background, (0,0))
                for part in self.snake.sprites:
                    self.screen.blit(part.image, part.rect)
                self.screen.blit(self.food.image, self.food.rect)
            pg.display.update()

if __name__ == "__main__":
    run_it = Control()
    run_it.main_loop()
    pg.quit()
    sys.exit()
