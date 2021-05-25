class Settings:
    """A class to store all setting for example game"""

    def __init__(self):
        """Initialize the game settings"""
        # screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (238,238,228)
        # ship settings

        self.ship_limit = 3
        # bullet settings

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 64, 64, 64
        self.bullets_allowed = 3
        # aliens settings

        self.fleet_drop_speed = 7
        # fleet direction right = 1, left = -1

        self.speedup_scale = 1.25

    def init_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor = 1.5

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale