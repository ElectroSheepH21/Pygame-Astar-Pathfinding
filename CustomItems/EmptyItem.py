from dataclasses import dataclass
from SpotGrid.SpotItemCol import SpotItemCol


@dataclass
class EmptyItem(SpotItemCol):
    def __post_init__(self):
        self.id = 0
        self.color = (255, 255, 255)

