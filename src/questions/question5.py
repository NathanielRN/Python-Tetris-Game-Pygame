from pygame.event import Event
from pygame.mixer import Sound
import pygame

from game_state import GameState

# If blocks with finally getting to move the pieces.

def solution5(gs: GameState, e: Event, rotate_sound: Sound) -> None:
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
