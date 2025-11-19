import pygame


def _start_game(self):
    """Start a new game."""
    self.stats.reset_stats()
    self.stats.game_active = True
    self.sb.prep_images()

    self.aliens.empty()
    self.bullets.empty()
    self._create_fleet()
    self.ship.center_ship()
    
def _check_play_button(self, mouse_pos):
    button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not self.stats.game_active:
        self._start_game()

    pygame.mouse.set_visible(False)
