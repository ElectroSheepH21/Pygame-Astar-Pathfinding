from dataclasses import dataclass
import pygame
from SpotGrid.SpotItemImg import SpotItemImg


@dataclass
class TargetItem(SpotItemImg):
    def __post_init__(self):
        self.id = 3
        self.image = pygame.image.load('Images/target.png')
