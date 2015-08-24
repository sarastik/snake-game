import pygame as pg

class Score():

    def __init__(self, snake, screen_rect):
        self.snake = snake
        self.font = pg.font.Font("DIMITRI_.TTF", 25)
        self.image = self.font.render("Score: 0", True, (0, 0, 0))
        self.rect = self.image.get_rect(center = (screen_rect.midtop[0], 20))

    def get_score(self):
        return len(self.snake.sprites) - 3

    def recenter(self):
        self.rect = self.image.get_rect(center = (screen_rect.midtop, 20))

    def update(self):
        text = "Score: " + str(self.get_score())
        self.image = self.font.render(text, False, (0, 0, 0))
