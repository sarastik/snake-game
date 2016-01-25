import os
import pygame as pg
import snake
import food
import score
import gameover
import title
import random

BACKGROUND_DICT = { 0: "sprites/sand.png",
                    1: "sprites/dirt.png"}
class Control():
    
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        pg.display.set_mode((630, 630))

        background_picker = random.choice([0, 1])
        self.background = pg.image.load(BACKGROUND_DICT[background_picker]).convert()
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.done = False
        self.keys = pg.key.get_pressed()
        
        snake_picker = random.choice([0, 1])
        self.snake = snake.Snake(snake_picker, self.screen_rect.center)
        self.food = food.Food(self.screen_rect.center, self.snake)
        self.score = score.Score(self.snake, self.screen_rect)
        self.game_over = gameover.GameOver(self.screen_rect)
        self.title = title.Title(self.screen_rect)

        self.state = "Title" #"Alive", "Dead"

    # Handles key presses and quitting while in game
    def event_loop(self):
        for event in pg.event.get():
            self.keys = pg.key.get_pressed()
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True
            elif event.type == pg.KEYDOWN:
                if self.state == "Alive":
                    self.snake.key_check = True
                    self.snake.change_direction(event.key)
                if event.key == pg.K_RETURN:
                    if self.state == "Dead":
                        self.__init__()
                        self.state = "Alive"
                        self.main_loop()
                    elif self.state == "Title":
                        self.state = "Alive"                        

    def main_loop(self):
        while not self.done:
            pg.time.delay(100) #for effect and slower speed
            self.event_loop()
            if self.snake.dead:
                self.state = "Dead"
            if self.state == "Title":
                self.title.draw(self.screen)
            elif self.state == "Dead":
                self.game_over.draw(self.screen)
            elif self.state == "Alive":
                #Update all the sprites
                self.snake.update(self.screen_rect)
                self.food.update()
                self.score.update()
                
                #Draw them on the screen
                self.screen.blit(self.background, (0,0))
                self.snake.draw(self.screen)
                self.food.draw(self.screen)
                self.score.draw(self.screen)
            pg.display.update()
            
