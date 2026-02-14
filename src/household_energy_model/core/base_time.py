import numpy as np
import pandas as pd
from dataclasses import dataclass

@dataclass
class BaseTime:
    time_series: pd.DataFrame

    def __post_init__(self):
        self.time_stamps = self.time_series.index
        self.N = len(self.time_series)

    def check_time_series(self, df):
        if self.time_stamps.equals(df.index) == False:
            raise ValueError("the timestamps do not match the base time")