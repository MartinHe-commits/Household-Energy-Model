import pandas as pd
import numpy as np
from household_energy_model.components.mixins import ProfileMixin

class Consumer(ProfileMixin):

    def __init__(self, base_time):
        self.base_time = base_time

    def run(self):
        pass

    def setup_results_schee(self):
        pass

