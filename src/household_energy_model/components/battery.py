import numpy as np


class Battery:
    def __init__(self, name, battery_capacity, max_loading_power = 1e9, max_deloading_power = 1e9, soc=0):
        self.name = name
        self.battery_capacity = battery_capacity # in Wh
        self.max_loading_power = max_loading_power # in W
        self.max_deloading_power = max_deloading_power #in W
        self.soc = soc # float from 0 to 1 0.5 equals 50%
        self.loaded_capacity = battery_capacity * soc

    def power_input(self, input_power, time_step): #time_step in hours
        if self.soc < 1:
            if input_power > self.max_loading_power:
                self.loaded_capacity += self.max_loading_power * time_step

            else:
                self.loaded_capacity += input_power

        self.soc = self.loaded_capacity / self.battery_capacity

    def power_output(self, output_power, time_step):
        if self.soc > 1:
            if output_power > self.max_deloading_power:
                self.loaded_capacity -= self.max_deloading_power * time_step

            else:
                self.loaded_capacity -= output_power * time_step

        self.soc = self.loaded_capacity / self.battery_capacity





