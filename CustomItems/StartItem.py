from dataclasses import dataclass
import pygame
from SpotGrid.SpotItemImg import SpotItemImg


@dataclass
class StartItem(SpotItemImg):
    def __post_init__(self):
        self.id = 2
        self.image = pygame.image.load('images/start.png')