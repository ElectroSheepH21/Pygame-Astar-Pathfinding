from dataclasses import dataclass, field
import pygame
from SpotGrid.Spot import Spot


@dataclass
class SpotItemImg(Spot):
    image: pygame.image = field(default=None)

    def draw(self, screen, x, y):
        screen.blit(pygame.transform.scale(self.image, (self.width, self.width)), (x, y))
