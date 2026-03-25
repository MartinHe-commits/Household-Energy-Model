import numpy as np

class ProfileMixin:
    def set_profile(self, df, profile_type='absolute'):
        self.base_time.check_time_series(df)
        if profile_type == 'absolute':
            self.energy_profile = np.array(df.values)
        if profile_type == 'relative':
            self.energy_profile = np.array(df.values) * self.power