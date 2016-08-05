import random

import pygame


class Cell:
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive
        self.neighbours = []

    def init_neighbours(self, x, y, width, height, population):
        if y > 0:
            if x > 0:
                self.neighbours.append(population[(width * (self.y - 1)) + self.x - 1])
            self.neighbours.append(population[(width * (self.y - 1)) + self.x])
            if x < width - 1:
                self.neighbours.append(population[(width * (self.y - 1)) + self.x + 1])
        if y < height - 1:
            if x > 0:
                self.neighbours.append(population[(width * (self.y + 1)) + self.x - 1])
            self.neighbours.append(population[(width * (self.y + 1)) + self.x])
            if x < width - 1:
                self.neighbours.append(population[(width * (self.y + 1)) + self.x + 1])
        if x > 0:
            self.neighbours.append(population[(width * self.y) + self.x - 1])
        self.neighbours.append(population[(width * self.y) + self.x])
        if x < width - 1:
            self.neighbours.append(population[(width * self.y) + self.x + 1])

    def update(self):
        live_neighbours = [n for n in self.neighbours if n.alive]
        if self.alive:
            if len(live_neighbours) < 2:
                self.alive = False
            elif len(live_neighbours) > 3:
                self.alive = False
        else:
            if len(live_neighbours) == 3:
                self.alive = True

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, (160, 255, 20), (self.x*4, self.y*4, 4, 4))


class Population:
    def __init__(self, width, height):
        self.population = []
        for y in range(height):
            for x in range(width):
                self.population.append(Cell(x, y, random.randrange(100) > 90))
        for y in range(height):
            for x in range(width):
                self.population[(y * width) + x].init_neighbours(x, y, width, height, self.population)

    def draw(self, screen, width, height):
        for y in range(height):
            for x in range(width):
                self.population[(y * width) + x].draw(screen, )

    def update(self, width, height):
        for y in range(height):
            for x in range(width):
                self.population[(y * width) + x].update()


def life_game(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width*4, height*4))
    population = Population(width, height)

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return

        screen.fill((100, 100, 100))

        population.update(width, height)
        population.draw(screen, width, height)

        pygame.display.flip()


if __name__ == "__main__":
    life_game(320, 200)
