import pygame, sys
from pygame.event import Event
from game_state import GameState
from questions.question4 import solution4
from questions.question8 import solution8
from src.drawer import DrawerSingleton
from src.grid import Grid

UPDATE_SCREEN_FPS = 60

pygame.init()
pygame.display.set_caption("Python Tetris")


def start() -> None:
    clock = pygame.time.Clock()

    AUTO_MOVE_EVENT = pygame.USEREVENT
    auto_move_delay_ms = solution8()
    pygame.time.set_timer(AUTO_MOVE_EVENT, auto_move_delay_ms)

    drawer = DrawerSingleton()
    drawer.setup()

    pygame.mixer.music.load("src/Sounds/music.ogg")
    pygame.mixer.music.play(-1)

    rotate_sound = pygame.mixer.Sound("src/Sounds/rotate.ogg")

    grid = Grid()
    gs = GameState(grid)

    def react_to_event(ev: Event):
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if ev.type == pygame.KEYDOWN:
            if gs.game_over:
                gs.reset()
            elif ev.key == pygame.K_r:
                gs.rotate()
                rotate_sound.play()
            elif ev.key == pygame.K_h:
                gs.hold()
            else:
                solution4(gs, ev)
            return

        if not gs.game_over and event.type == AUTO_MOVE_EVENT:
            gs.move_down()

    while True:
        for event in pygame.event.get():
            react_to_event(event)
        drawer.draw_dynamic_elements(grid, gs)

        pygame.display.update()
        clock.tick(UPDATE_SCREEN_FPS)
