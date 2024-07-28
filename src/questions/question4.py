from pygame.event import Event
import pygame

from game_state import GameState


"""
Objective: Be able to use arrow keys to move blocks.
"""


def solution4(gs: GameState, e: Event) -> None:
    if e.key == pygame.K_LEFT:
        gs.move_left()
    elif e.key == pygame.K_RIGHT:
        gs.move_right()
    elif e.key == pygame.K_DOWN:
        _ = gs.move_down()
    elif e.key == pygame.K_UP:
        while gs.move_down():
            pass
