import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from household_energy_model.components.mixins import ProfileMixin

class PVSystem(ProfileMixin):
    def __init__(self, base_time, name, power):
        self.name = name
        self.power = power # power in W
        self.base_time = base_time
        self.setup_results_schema()

    def run(self):
        pass

    def setup_results_schema(self):
        self.results_schema = ['E.el.out.PV']

    #Probeweise initialisierung eines power-profiles
    def init_energy_profile(self):
        energy_profile = np.full(100, np.nan)
        for i in range(len(energy_profile)):
            if i >= 20 and i <= 40:
                energy_profile[i] = 1

            if i >= 60 and i <= 80:
                energy_profile[i] = 1

        self.energy_profile = (energy_profile + 1) * self.power

    def calculate_energy(self):
        self.energy_output = self.energy_profile * self.power
        return self.energy_output



