import pygame, sys
from pygame.event import Event
from game_state import GameState
from src.drawer import Drawer
from src.grid import Grid

UPDATE_FPS = 60
AUTO_MOVE_FPS = 5

pygame.init()
pygame.display.set_caption("Python Tetris")


def start() -> None:

    clock = pygame.time.Clock()

    AUTO_MOVE_EVENT = pygame.USEREVENT
    auto_move_delay_ms = int(1 / AUTO_MOVE_FPS * 1000)  # 200 ms
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
            if gs.game_over:
                gs.reset()
            else:
                if e.key == pygame.K_LEFT:
                    gs.move_left()
                elif e.key == pygame.K_RIGHT:
                    gs.move_right()
                elif e.key == pygame.K_DOWN:
                    gs.move_down()
                elif e.key == pygame.K_UP:
                    while gs.move_down():
                        pass
                elif e.key == pygame.K_r:
                    gs.rotate()
                    rotate_sound.play()
                elif e.key == pygame.K_h:
                    gs.hold()
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
