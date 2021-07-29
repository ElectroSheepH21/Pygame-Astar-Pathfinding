from dataclasses import dataclass, field
import pygame
from SpotGrid.Spot import Spot


@dataclass
class SpotItemCol(Spot):
    color: pygame.Color = field(default=None)

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, self.color, (x, y, self.width, self.width))
