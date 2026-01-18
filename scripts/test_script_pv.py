import numpy as np
from matplotlib import pyplot as plt

from household_energy_model.components.electricity_grid import ElectricityGrid
from household_energy_model.components.heating_system import HeatingSystem
from household_energy_model.components.pv_system import PVSystem

#initialisiere Systemkomponenten
pv_system = PVSystem(name = 'pv_system', power = 10e3)
pv_system.init_energy_profile()

heat_pump = HeatingSystem(name = 'heat_pump', type = 'heat_pump', heating_capacity = 20e3)
heat_pump.init_heating_profile()

electricity_grid = ElectricityGrid(name = 'electric_grid')

# rechne einfache Bilanz und teste ElectricityGrid

electricity_balancing_household_profile = pv_system.energy_profile - heat_pump.heating_profile

electricity_grid.calculate_energy_balancing_profile(electricity_balancing_household_profile)
electricity_grid.calculate_energy_input()
electricity_grid.calculate_energy_output()

print(electricity_grid.energy_in)
print(electricity_grid.energy_out)
plt.plot(electricity_grid.energy_balance_profile)
plt.show()

