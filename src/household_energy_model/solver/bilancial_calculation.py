from household_energy_model.components import electricity_grid
from household_energy_model.components import heating_system
from household_energy_model.components import pv_system

class BilancialCircle():

    def __init__(self, connection_dict):
        self.connection_dict = connection_dict