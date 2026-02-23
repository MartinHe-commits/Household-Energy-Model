import numpy as np
import pandas as pd
from dataclasses import dataclass

@dataclass
class BaseTime:
    time_series: pd.DataFrame

    def __post_init__(self):

        if not isinstance(self.time_series.index, pd.DatetimeIndex):
            raise TypeError('DatetimeIndex must be a pd.DatetimeIndex')

        if not self.time_series.index.is_unique:
            raise ValueError('DatetimeIndex must be unique')

        self.time_stamps = self.time_series.index
        self.N = len(self.time_series)

    def check_time_series(self, df):
        if self.time_stamps.equals(df.index) == False:
            raise ValueError("the timestamps do not match the base time")