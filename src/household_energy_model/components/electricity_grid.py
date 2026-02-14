import numpy as np
from household_energy_model.components.mixins import ProfileMixin


class ElectricityGrid(ProfileMixin):

    def __init__(self, base_time, name, energy_in=0, energy_out=0):
        self.name = name
        # self.energy_balance_profile = energy_balance_profile
        self.energy_in = energy_in
        self.energy_out = energy_out
        self.base_time = base_time

    def run(self):
        pass

    def setup_results_schema(self):
        self.results_schema = ['E.el.in.Grid', 'E.el.out.Grid', 'E.el.balance.Grid']

    def calculate_energy_input(self):
        energy_input = self.energy_balance_profile[self.energy_balance_profile >=0]
        self.energy_in = sum(energy_input)

    def calculate_energy_output(self):
        energy_output = self.energy_balance_profile[self.energy_balance_profile < 0]
        self.energy_out = sum(energy_output)




