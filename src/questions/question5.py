from pygame.event import Event
from pygame.mixer import Sound
import pygame

from game_state import GameState

# If blocks to finally start moving pieces!!!

def solution5(gs: GameState, e: Event, rotate_sound: Sound) -> None:
    if gs.game_over:
        # --> Reset the game state if the game is over
        pass
    else:
        if e.key == pygame.K_LEFT:
            # --> Move the piece left
            pass
        elif e.key == pygame.K_RIGHT:
            # --> Move the piece right
            pass
        elif e.key == pygame.K_DOWN:
            # --> Move the piece down
            pass
        elif e.key == pygame.K_UP:
            # --> Continuously move the piece down
            pass
        elif e.key == pygame.K_r:
            # --> Rotate the piece
            # --> Play the rotation sound
            pass
        elif e.key == pygame.K_h:
            # --> Hold the piece
            pass