import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class HeatingSystem:
    def __init__(self, base_time, name, heating_capacity, type):
        self.name = name
        self.heating_capacity = heating_capacity
        self.type = type
        self.base_time = base_time

    def run(self):
        pass

    def set_profile(self):
        pass

    def setup_results_schema(self):
        self.results_schema = ['E.el.in.Heating', 'E.th.out.Heating']

    #initialize heating_profile for tests
    def init_heating_profile(self):
        heating_profile = np.zeros(100)
        a = 0

        for counter, element in enumerate(heating_profile):
            a += 1
            heating_profile[counter] = a/20
            if a == 20:
                a = 0

        self.heating_profile = heating_profile * self.heating_capacity


    def calculate_cop(self):
        pass

    def heating(self, power_input):
        pass



