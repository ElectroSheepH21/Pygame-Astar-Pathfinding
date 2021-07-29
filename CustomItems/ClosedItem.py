from dataclasses import dataclass
from SpotGrid.SpotItemCol import SpotItemCol


@dataclass
class ClosedItem(SpotItemCol):
    def __post_init__(self):
        self.id = 6
        self.color = (255, 140, 0)
