import pygame

from game_running_state import GameRunningState
from game_state import GameState


class PreGameState(GameState):
    def update(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return None
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return GameRunningState(self.population, self.width, self.height, self.scale)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.population.toggle_cell(self.width, self.scale, event.pos)
        return self
