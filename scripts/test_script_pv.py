import numpy as np
from matplotlib import pyplot as plt

from household_energy_model.components.electricity_grid import ElectricityGrid
from household_energy_model.components.heating_system import HeatingSystem
from household_energy_model.components.pv_system import PVSystem
from household_energy_model.components.battery import Battery

time_series_length = 100

#initialisiere Systemkomponenten
pv_system = PVSystem(name = 'pv_system', power = 10e3)
pv_system.init_energy_profile()

heat_pump = HeatingSystem(name = 'heat_pump', type = 'heat_pump', heating_capacity = 20e3)
heat_pump.init_heating_profile()

battery = Battery(name = 'battery', capacity = 8e3)

electricity_grid = ElectricityGrid(name = 'electric_grid')

# rechne einfache Bilanz und teste ElectricityGrid
electricity_balance_source_consumer = np.zeros(100)
for i, value in enumerate(pv_system.energy_profile):
    electricity_balance_source_consumer[i] = pv_system.energy_profile[i] - heat_pump.heating_profile[i]

    if electricity_balance_source_consumer[i] >= 0:
        electricity_grid.energy_balance_profile[i] = battery.energy_input(electricity_balance_source_consumer[i])
        battery_soc_profile[i] = battery.soc


    else:
        electricity_grid.energy_balance_profile[i] = battery.energy_output(electricity_balance_source_consumer[i])







print('energy_in = {}'.format(electricity_grid.energy_in))
print('energy_out = {}'.format(electricity_grid.energy_out))
plt.plot(electricity_grid.energy_balance_profile)
plt.show()

