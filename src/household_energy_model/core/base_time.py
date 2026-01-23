import numpy as np
from dataclasses import dataclass

@dataclass
class BaseTime:
    time_series: np.ndarray

    def __post_init__(self):
        self.N = len(self.time_series)