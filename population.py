from cell import Cell


class Population:
    def __init__(self, width, height):
        self.population = []
        for y in range(height):
            for x in range(width):
                self.population.append(Cell(x, y, False))
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

    def set_cell(self, width, scale, pos):
        cell_x = int(pos[0] / scale)
        cell_y = int(pos[1] / scale)
        cell = self.population[(cell_y * width) + cell_x]
        cell.alive = True
