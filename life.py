import pygame

from population import Population
from pre_game_state import PreGameState


def life_game(width, height):
    pygame.init()
    screen_scale = 4
    screen = pygame.display.set_mode((width * screen_scale, height * screen_scale))
    population = Population(width, height)

    clock = pygame.time.Clock()
    state = PreGameState(population, width, height, screen_scale)

    while True:
        clock.tick(60)

        screen.fill((100, 100, 100))

        state = state.update()
        if state is None:
            return

        population.draw(screen, width, height)
        pygame.display.flip()


if __name__ == "__main__":
    life_game(320, 200)
