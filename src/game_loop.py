import pygame, sys
from pygame.event import Event
from game_state import GameState
from questions.question1 import solution1
from questions.question5 import solution5
from questions.question8 import solution8
from src.drawer import Drawer
from src.grid import Grid

UPDATE_FPS = 60

pygame.init()
pygame.display.set_caption("Python Tetris")


def start() -> None:
    solution1()

    clock = pygame.time.Clock()

    AUTO_MOVE_EVENT = pygame.USEREVENT
    auto_move_delay_ms = solution8()
    pygame.time.set_timer(AUTO_MOVE_EVENT, auto_move_delay_ms)

    drawer = Drawer()
    drawer.setup()

    pygame.mixer.music.load("src/Sounds/music.ogg")
    pygame.mixer.music.play(-1)

    rotate_sound = pygame.mixer.Sound("src/Sounds/rotate.ogg")

    grid = Grid()
    gs = GameState(grid)

    def react_to_event(e: Event):
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN:
            solution5(gs, e, rotate_sound)
            return

        if not gs.game_over and event.type == AUTO_MOVE_EVENT:
            gs.move_down()

    while True:
        for event in pygame.event.get():
            react_to_event(event)
            continue

        drawer.draw_base_elements()
        drawer.draw_grid(grid)
        drawer.draw_gs(gs)

        pygame.display.update()
        clock.tick(UPDATE_FPS)
