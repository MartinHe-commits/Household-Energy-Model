import numpy as np

from household_energy_model.components.mixins import ProfileMixin


class Battery(ProfileMixin):
    def __init__(self, base_time, name, max_capacity, max_loading_power = 1e9, max_deloading_power = 1e9, soc=0):
        self.name = name
        self.max_capacity = max_capacity # in Wh
        self.max_loading_power = max_loading_power # in W
        self.max_deloading_power = max_deloading_power #in W
        self.soc = soc # float from 0 to 1 0.5 equals 50%
        self.base_time = base_time
        self.loaded_capacity = max_capacity * soc

    def run(self):
        pass


    def setup_results_schema(self):
        self.results_schema = ['E.el.in.Battery', 'E.el.out.Battery', 'E.el.balance.Battery']

    def energy_input(self, energy_input): #time_step in hours
        # if self.soc < 1:
        #     if energy_input > self.max_loading_power:
        #         self.loaded_capacity += self.max_loading_power * time_step
        #
        #     else:
        #         self.loaded_capacity += energy_input
        #
        # self.soc = self.loaded_capacity / self.battery_capacity

        if self.loaded_capacity + energy_input <= self.max_capacity:
            # ToDo was wenn zu viel Strom auf einmal rein soll und die Batterie nicht hinterher kommt?
            self.loaded_capacity += energy_input
            unstored_energy = 0

        else:
            capacity = self.max_capacity - self.loaded_capacity
            self.loaded_capacity += capacity
            unstored_energy = energy_input - capacity

        self.soc = self.loaded_capacity / self.max_capacity
        return unstored_energy

    def energy_output(self, energy_output):
        # if self.soc > 1:
        #     if output_power > self.max_deloading_power:
        #         self.loaded_capacity -= self.max_deloading_power * time_step
        #

        #     else:
        #         self.loaded_capacity -= output_power * time_step
        #
        # self.soc = self.loaded_capacity / self.max_capacity

        if self.loaded_capacity - energy_output >= 0:
            # ToDo auch hier den Fall Programmieren, dass die Batterie nicht schnell genug ein- und ausspeisen kann
            self.loaded_capacity -= energy_output
            missing_energy = 0

        else:
            missing_energy = energy_output - self.loaded_capacity
            self.loaded_capascity = 0

        self.soc = self.loaded_capacity / self.max_capacity
        return missing_energy
