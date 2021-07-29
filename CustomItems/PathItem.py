from dataclasses import dataclass
from SpotGrid.SpotItemCol import SpotItemCol


@dataclass
class PathItem(SpotItemCol):
    def __post_init__(self):
        self.id = 4
        self.color = (0, 75, 250)
