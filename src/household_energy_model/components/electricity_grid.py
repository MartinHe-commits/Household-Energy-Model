import numpy as np


class ElectricityGrid:

    def __init__(self, name, energy_balance_profile = np.zeros(100), energy_in=0, energy_out=0):
        self.name = name
        self.energy_balance_profile = energy_balance_profile
        self.energy_in = energy_in
        self.energy_out = energy_out


    def calculate_energy_balancing_profile(self, array):
        for index, value in enumerate(array):
            self.energy_balance_profile[index] += value


    def calculate_energy_input(self):
        energy_input = self.energy_balance_profile[self.energy_balance_profile >=0]
        self.energy_in = sum(energy_input)

    def calculate_energy_output(self):
        energy_output = self.energy_balance_profile[self.energy_balance_profile < 0]
        self.energy_out = sum(energy_output)


