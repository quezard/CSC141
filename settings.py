self.target_speed = 1.0
self.ship_speed = 1.5
self.bullet_speed = 3.0

self.misses_allowed = 3

self.target_speed_scale = 1.1

self.settings.target_speed *= self.settings.target_speed_scale
_start_game(): self.settings.target_speed = 1.0

def apply_difficulty(self, level):
    if level == 'easy':
        self.ship_speed = 1.0
        self.bullet_speed = 2.0
        self.alien_speed = 0.5
        self.fleet_drop_speed = 7

    elif level == 'medium':
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

    elif level == 'hard':
        self.ship_speed = 2.0
        self.bullet_speed = 4.0
        self.alien_speed = 1.5
        self.fleet_drop_speed = 12
