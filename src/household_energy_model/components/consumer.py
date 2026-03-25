import pandas as pd
import numpy as np
from household_energy_model.components.mixins import ProfileMixin

class Consumer(ProfileMixin):

    def __init__(self, base_time, name):
        self.base_time = base_time
        self.name = name

    def run(self):
        pass

    def setup_results_schema(self):
        self.results_schema = ['E.el.in.Consumer', 'E.th.in.Consumer']

