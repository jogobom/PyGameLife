import pygame

from game_running_state import GameRunningState
from game_state import GameState


class PreGameState(GameState):
    def __init__(self, population, width, height, scale):
        super().__init__(population, width, height, scale)
        self.drawing = False

    def update(self, clock):
        clock.tick(240)

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return None
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return GameRunningState(self.population, self.width, self.height, self.scale)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.population.set_cell(self.width, self.scale, event.pos)
            self.drawing = False
        elif event.type == pygame.MOUSEMOTION and self.drawing:
            self.population.set_cell(self.width, self.scale, event.pos)

        return self
