from dataclasses import dataclass
from SpotGrid.SpotItemCol import SpotItemCol


@dataclass
class OpenItem(SpotItemCol):
    def __post_init__(self):
        self.id = 5
        self.color = (0, 170, 250)
