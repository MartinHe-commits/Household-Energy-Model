from household_energy_model.components.pv_system import PVSystem

pv_system = PVSystem(name = 'pv_system', power = 50)
pv_system.init_power_profile()