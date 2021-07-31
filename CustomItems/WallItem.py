from dataclasses import dataclass
import pygame
from SpotGrid.SpotItemImg import SpotItemImg


@dataclass
class WallItem(SpotItemImg):
    def __post_init__(self):
        self.id = 1
        self.image = pygame.image.load('Images/wall.png')
