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

    def run(self, energy):
        if energy < 0:
            self.energy_output(-energy)

        elif energy >0:
            self.energy_input(energy)


    def energy_input(self, energy_input): #time_step in hours
        input_capacity = self.max_capacity - self.loaded_capacity
        if input_capacity >= energy_input:
            if self.max_loading_power >= energy_input:
                self.loaded_capacity += energy_input
                unstored_energy = 0
            else:
                self.loaded_capacity += self.max_loading_power
                unstored_energy = energy_input - self.max_loading_power

        elif input_capacity < energy_input:
            if self.max_loading_power >= input_capacity:
                self.loaded_capacity = self.max_capacity
                unstored_energy = energy_input - input_capacity
            else:
                self.loaded_capacity += self.max_loading_power
                unstored_energy = energy_input - self.max_loading_power

        self.soc = self.loaded_capacity / self.max_capacity
        return unstored_energy

    def energy_output(self, energy_output):
        # Batterie hat genug Energie geladen
        if self.loaded_capacity >= energy_output:
            if self.max_deloading_power >= energy_output:
                self.loaded_capacity -= energy_output
                missing_energy = 0

            else:
                missing_energy = energy_output - self.max_deloading_power

        # Batterie hat weniger Energie geladen als benötigt wird
        elif self.loaded_capacity < energy_output:
            if self.max_deloading_power >= self.loaded_capacity:
                missing_energy = energy_output - self.loaded_capacity
                self.loaded_capascity = 0

            else:
                missing_energy = energy_output - self.max_deloading_power
                self.loaded_capacity = self.loaded_capacity - self.max_deloading_power

        self.soc = self.loaded_capacity / self.max_capacity
        return -missing_energy

    def setup_results_schema(self):
        self.results_schema = ['E.el.in.Battery', 'E.el.out.Battery', 'E.el.balance.Battery']
