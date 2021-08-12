class Settings():
    def __init__(self):
        self.width = 1300
        self.height = 700
        self.bg_color = (230, 230, 200)
        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed = 2.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.5

        self.fleet_direction = 1
        self.alien_point = 50
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)

