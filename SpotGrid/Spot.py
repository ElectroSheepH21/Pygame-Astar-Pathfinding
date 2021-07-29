from dataclasses import dataclass, field


@dataclass
class Spot:
    col: int = field(default=0)
    row: int = field(default=0)
    width: int = field(default=0)
    id: int = field(default=-1)
    g_cost: float = field(default=0)
    h_cost: float = field(default=0)
    f_cost: float = field(default=0)
    came_from: None = field(default=None)

    def __str__(self):
        return "(" + str(self.col) + ", " + str(self.row) + ")"

    def update_f_cost(self):
        self.f_cost = self.g_cost + self.h_cost

    def __lt__(self, other):
        return self.f_cost < other.f_cost

    def draw(self, screen, x, y):
        raise NotImplementedError()
