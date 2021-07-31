from dataclasses import dataclass
import pygame
from SpotGrid.SpotItemImg import SpotItemImg


@dataclass
class BoxItem(SpotItemImg):
    def __post_init__(self):
        self.id = 7
        self.image = pygame.image.load('Images/box.png')
