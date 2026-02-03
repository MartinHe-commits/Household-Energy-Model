from src.household_energy_model.io.import_profile import import_profile
from src.household_energy_model.core.base_time import BaseTime
from src.household_energy_model.components.pv_system import PVSystem
from pathlib import Path
from matplotlib import pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
data_path = PROJECT_ROOT / 'data'
pv_energy_df = import_profile(data_path/'pv_profile_random_10 kW.xlsx')
pv_energy_df.set_index('Date', inplace=True)
base_time = BaseTime(time_series=pv_energy_df)
# pv_energy_df.loc['2025-04-11 00:00:00'] = 500
print(pv_energy_df)
print(base_time.time_series)
print(base_time.N)
print(base_time.time_stamps)
pv_system = PVSystem(base_time=base_time,name="PV-Anlage", power=10e3)
pv_system.set_profile(pv_energy_df)
plt.plot(pv_system.energy_profile)
plt.show()