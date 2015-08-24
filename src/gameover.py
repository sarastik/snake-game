import pygame as pg

class GameOver():

    def __init__(self, snake, screen_rect):
        self.snake = snake
        self.screen_rect = screen_rect
        self.font = pg.font.Font("DIMITRI_.TTF", 30)
        
        self.game_over = pg.image.load("sprites/game_over_text.png").convert()
        self.game_over.set_colorkey((51, 250, 1))
        self.game_over_rect = self.game_over.get_rect(center = self.screen_rect.center)
                
        self.replay_text = "PRESS ENTER TO PLAY AGAIN"
        self.replay = self.font.render(self.replay_text, False, (0, 0, 0))
        self.replay_rect = self.replay.get_rect(center = self.screen_rect.center)
        self.replay_rect.centery += 150
        
        self.exit_text = "PRESS ESCAPE TO QUIT"
        self.exit = self.font.render(self.exit_text, False, (0, 0, 0))
        self.exit_rect = self.exit.get_rect(center = self.screen_rect.center)
        self.exit_rect.centery += 200

    def draw(self, screen):
        if self.snake.dead:
            screen.blit(self.game_over, self.game_over_rect)
            screen.blit(self.exit, self.exit_rect)
            screen.blit(self.replay, self.replay_rect)
        
