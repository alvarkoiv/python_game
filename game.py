import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from alien import Alien
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    # init game and create display object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Example Game")

    play_button = Button(game_settings, screen, "Start")

    stats = GameStats(game_settings)

    sb = Scoreboard(game_settings, screen, stats)

    ship = Ship(game_settings, screen)
    bullets = Group()

    aliens = Group()
    gf.create_fleet(game_settings, screen, ship, aliens)

    while True:
        gf.check_events(game_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(game_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, play_button)
# test game
run_game()
