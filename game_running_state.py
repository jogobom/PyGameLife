import pygame

from game_state import GameState


class GameRunningState(GameState):
    def update(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return None

        self.population.update(self.width, self.height)
        return self
