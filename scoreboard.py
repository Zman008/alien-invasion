import pygame.font

class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (55, 10, 200)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_level()
        self.prep_ship()
        self.prep_high_score()
    def prep_score(self):
        round_score = round(self.stats.score, -1)
        self.score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(self.score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def prep_level(self):
        level_no = str(self.stats.level)
        self.level_image = self.font.render(level_no, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.topleft = self.screen_rect.topleft
    def prep_ship(self):
        self.ship_image = pygame.image.load('images/ship.bmp')
        self.ship_image = pygame.transform.scale(self.ship_image, (30, 24))
        self.ship_rect = self.ship_image.get_rect()
        self.ship_rect.y = 40
        for space in range(0,self.stats.ships_left):
            self.ship_rect.x = 10 + self.ship_rect.width * space
            self.screen.blit(self.ship_image, self.ship_rect)

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_round = "HIGH SCORE: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_round, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
