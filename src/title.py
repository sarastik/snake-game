import pygame as pg

class Title():

    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.font = pg.font.Font("DIMITRI_.TTF", 30)
        self.image = pg.image.load("sprites/title_screen.png").convert()

        self.title = pg.image.load("sprites/title.png").convert()
        self.title.set_colorkey((0, 255, 0))
        self.title_rect = self.title.get_rect(center = self.screen_rect.center)
        self.title_rect.centery -= 150

        starting_text = "PRESS ENTER TO BEGIN"
        self.starting = self.font.render(starting_text, False, (255, 255, 255))
        self.starting_rect = self.starting.get_rect(center = self.screen_rect.center)
        self.starting_rect.centery += 215

        select_text = "SNAKE SELECTION: COMING SOON!"
        self.select = self.font.render(select_text, False, (255, 255, 255))
        self.select_rect = self.select.get_rect(center = self.screen_rect.center)
        self.select_rect.centery += 150

    def draw(self, screen):
        screen.blit(self.image, self.screen_rect)
        screen.blit(self.title, self.title_rect)
        screen.blit(self.select, self.select_rect)
        screen.blit(self.starting, self.starting_rect)
        
