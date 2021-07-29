from math import sqrt
import pygame
from SpotGrid.Spot import Spot


class SpotGrid:
    def __init__(self, cols, rows, scr, s, offset):
        self._cols = cols
        self._rows = rows
        self._screen = scr
        self._offset = offset
        self._grid_width = s[0]
        self._grid_height = s[1]
        self._sp_width = self._grid_width // cols
        self._spots = [[0 for r in range(rows)] for c in range(cols)]
        self._grid_on = False
        self._grid_color = None
        self._diagonal = False
        self._items = []
        self._bg = None
        for r in range(rows):
            for c in range(cols):
                self._spots[c][r] = Spot(c, r, self._sp_width)

    def draw_grid(self):
        for r in range(self._rows + 1):
            for c in range(self._cols + 1):
                pygame.draw.line(self._screen, self._grid_color, (self._offset.x, r * self._sp_width + self._offset.y), (self._grid_width + self._offset.x, r * self._sp_width + self._offset.y))
                pygame.draw.line(self._screen, self._grid_color, (c * self._sp_width + self._offset.x, self._offset.y), (c * self._sp_width + self._offset.x, self._grid_height + self._offset.y))

    def draw_background(self):
        self._screen.blit(pygame.transform.scale(self._bg, (self._grid_width, self._grid_height)), (self._offset.x, self._offset.y))

    def draw_spots(self):
        for r in range(self._rows):
            for c in range(self._cols):
                is_item = False
                ids = self.get_item_ids()
                try:
                    item_index = ids.index(self._spots[c][r].id)
                    is_item = True
                except Exception:
                    is_item = False

                if is_item:
                    self._items[item_index].draw(self._screen, c * self._sp_width + self._offset.x, r * self._sp_width + self._offset.y);
                else:
                    pass  # Transparent

    def draw(self):
        if self._bg is not None:
            self.draw_background()
        self.draw_spots()
        if self._grid_on:
            self.draw_grid()

    def get_spot(self, x, y):
        return self._spots[x][y]

    def get_item_ids(self):
        arr = []
        for i in self._items:
            arr.append(i.id)
        return arr

    def get_neighbors(self, curr_sp, diagonal):
        neighbors = []

        if curr_sp.col + 1 < self._cols:
            neighbors.append(self._spots[curr_sp.col + 1][curr_sp.row])  # Right
        if curr_sp.col - 1 >= 0:
            neighbors.append(self._spots[curr_sp.col - 1][curr_sp.row])  # Left
        if curr_sp.row + 1 < self._rows:
            neighbors.append(self._spots[curr_sp.col][curr_sp.row + 1])  # Bottom
        if curr_sp.row - 1 >= 0:
            neighbors.append(self._spots[curr_sp.col][curr_sp.row - 1])  # Top

        if diagonal:
            if curr_sp.col + 1 < self._cols and curr_sp.row - 1 >= 0:
                neighbors.append(self._spots[curr_sp.col + 1][curr_sp.row - 1])  # Top right
            if curr_sp.col - 1 >= 0 and curr_sp.row - 1 >= 0:
                neighbors.append(self._spots[curr_sp.col - 1][curr_sp.row - 1])  # Top left
            if curr_sp.col + 1 < self._cols and curr_sp.row + 1 < self._rows:
                neighbors.append(self._spots[curr_sp.col + 1][curr_sp.row + 1])  # Bottom right
            if curr_sp.col - 1 >= 0 and curr_sp.row + 1 < self._rows:
                neighbors.append(self._spots[curr_sp.col - 1][curr_sp.row + 1])  # Bottom left
        return neighbors

    def get_cols(self):
        return self._cols

    def get_rows(self):
        return self._rows

    def find_spot(self, item):
        for r in range(self._rows):
            for c in range(self._cols):
                if self._spots[c][r].id == item.id:
                    return self._spots[c][r]

    def set_spot(self, p, id):
        if self._offset.x < p[0] < self._grid_width + self._offset.x and self._offset.y < p[1] < self._grid_height + self._offset.y:
            col = (p[0] - int(self._offset.x)) // self._sp_width
            row = (p[1] - int(self._offset.y)) // self._sp_width
            spot = self._spots[col][row]
            spot.id = id

    def clear_spot(self, p):
        if self._offset.x < p[0] < self._grid_width + self._offset.x and self._offset.y < p[1] < self._grid_height + self._offset.y:
            col = (p[0] - int(self._offset.x)) // self._sp_width
            row = (p[1] - int(self._offset.y)) // self._sp_width
            spot = self._spots[col][row]
            spot.id = -1

    def add_item(self, item):
        if item not in self._items:
            item.width = self._sp_width
            self._items.append(item)

    def load_background(self, bg):
        self._bg = bg

    @staticmethod
    def get_distance(sp1, sp2):
        x_dist = abs(sp1.col - sp2.col)
        y_dist = abs(sp1.row - sp2.row)

        return sqrt(x_dist**2 + y_dist**2)

    @property
    def grid_on(self):
        return self._grid_on

    @grid_on.setter
    def grid_on(self, value):
        self._grid_on = value

    @property
    def grid_color(self):
        return self._grid_color

    @grid_color.setter
    def grid_color(self, value):
        self._grid_color = value
