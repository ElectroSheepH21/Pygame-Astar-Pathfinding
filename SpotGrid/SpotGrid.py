from math import sqrt
import pygame
from SpotGrid.Spot import Spot


class SpotGrid:
    def __init__(self, cols, rows, scr, s, offset):
        self.cols = cols
        self.rows = rows
        self.screen = scr
        self.offset = offset
        self.grid_width = s[0]
        self.grid_height = s[1]
        self.sp_width = self.grid_width // cols
        self.spots = [[0 for r in range(rows)] for c in range(cols)]
        self._grid_on = False
        self._grid_color = None
        self.items = []
        self.background = None
        for r in range(rows):
            for c in range(cols):
                self.spots[c][r] = Spot(c, r, self.sp_width)

    def draw_grid(self):
        for r in range(self.rows + 1):
            for c in range(self.cols + 1):
                pygame.draw.line(self.screen, self.grid_color, (self.offset.x, r * self.sp_width + self.offset.y), (self.grid_width + self.offset.x, r * self.sp_width + self.offset.y))
                pygame.draw.line(self.screen, self.grid_color, (c * self.sp_width + self.offset.x, self.offset.y), (c * self.sp_width + self.offset.x, self.grid_height + self.offset.y))

    def draw_background(self):
        self.screen.blit(pygame.transform.scale(self.background, (self.grid_width, self.grid_height)), (self.offset.x, self.offset.y))

    def draw_spots(self):
        for r in range(self.rows):
            for c in range(self.cols):
                is_item = False
                ids = self.get_item_ids()
                try:
                    item_index = ids.index(self.spots[c][r].id)
                    is_item = True
                except Exception:
                    is_item = False

                if is_item:
                    self.items[item_index].draw(self.screen, c * self.sp_width + self.offset.x, r * self.sp_width + self.offset.y);
                else:
                    pass  # Transparent

    def draw(self):
        if self.background is not None:
            self.draw_background()
        self.draw_spots()
        if self.grid_on:
            self.draw_grid()

    def get_spot(self, x, y):
        return self.spots[x][y]

    def get_item_ids(self):
        arr = []
        for i in self.items:
            arr.append(i.id)
        return arr

    def get_neighbors(self, curr_sp, diagonal):
        neighbors = []

        if curr_sp.col + 1 < self.cols:
            neighbors.append(self.spots[curr_sp.col + 1][curr_sp.row])  # Right
        if curr_sp.col - 1 >= 0:
            neighbors.append(self.spots[curr_sp.col - 1][curr_sp.row])  # Left
        if curr_sp.row + 1 < self.rows:
            neighbors.append(self.spots[curr_sp.col][curr_sp.row + 1])  # Bottom
        if curr_sp.row - 1 >= 0:
            neighbors.append(self.spots[curr_sp.col][curr_sp.row - 1])  # Top

        if diagonal:
            if curr_sp.col + 1 < self.cols and curr_sp.row - 1 >= 0:
                neighbors.append(self.spots[curr_sp.col + 1][curr_sp.row - 1])  # Top right
            if curr_sp.col - 1 >= 0 and curr_sp.row - 1 >= 0:
                neighbors.append(self.spots[curr_sp.col - 1][curr_sp.row - 1])  # Top left
            if curr_sp.col + 1 < self.cols and curr_sp.row + 1 < self.rows:
                neighbors.append(self.spots[curr_sp.col + 1][curr_sp.row + 1])  # Bottom right
            if curr_sp.col - 1 >= 0 and curr_sp.row + 1 < self.rows:
                neighbors.append(self.spots[curr_sp.col - 1][curr_sp.row + 1])  # Bottom left
        return neighbors

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows

    def find_spot(self, item):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.spots[c][r].id == item.id:
                    return self.spots[c][r]

    def set_spot(self, p, id):
        if self.offset.x < p[0] < self.grid_width + self.offset.x and self.offset.y < p[1] < self.grid_height + self.offset.y:
            col = (p[0] - int(self.offset.x)) // self.sp_width
            row = (p[1] - int(self.offset.y)) // self.sp_width
            spot = self.spots[col][row]
            spot.id = id

    def clear_spot(self, p):
        if self.offset.x < p[0] < self.grid_width + self.offset.x and self.offset.y < p[1] < self.grid_height + self.offset.y:
            col = (p[0] - int(self.offset.x)) // self.sp_width
            row = (p[1] - int(self.offset.y)) // self.sp_width
            spot = self.spots[col][row]
            spot.id = -1

    def add_item(self, item):
        if item not in self.items:
            item.width = self.sp_width
            self.items.append(item)

    def load_background(self, bg):
        self.background = bg

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
