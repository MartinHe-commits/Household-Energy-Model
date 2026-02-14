import numpy as np

class ProfileMixin:
    def set_profile(self, df):
        self.base_time.check_time_series(df)
        self.energy_profile = np.array(df.values)