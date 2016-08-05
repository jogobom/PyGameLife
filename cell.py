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
        live_neighbours = len([n for n in self.neighbours if n.alive])
        if self.alive:
            if live_neighbours < 2 or live_neighbours > 3:
                self.alive = False
        else:
            if live_neighbours == 3:
                self.alive = True

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, (160, 255, 20), (self.x * 4, self.y * 4, 4, 4))
