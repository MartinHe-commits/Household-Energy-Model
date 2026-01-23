import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class PVSystem:
    def __init__(self, name, power):
        self.name = name
        self.power = power # power in W
        self.setup_results_schema()

    #Probeweise initialisierung eines power-profiles
    def init_energy_profile(self):
        energy_profile = np.full(100, np.nan)
        for i in range(len(energy_profile)):
            if i >= 20 and i <= 40:
                energy_profile[i] = 1

            if i >= 60 and i <= 80:
                energy_profile[i] = 1

        self.energy_profile = (energy_profile + 1) * self.power

    def set_profile(self):
        pass

    def calculate_energy(self):
        self.energy_output = self.energy_profile * self.power
        return self.energy_output

    def setup_results_schema(self):
        self.results_schema = ['E.PV']


