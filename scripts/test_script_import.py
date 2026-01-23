from src.household_energy_model.io.import_profile import import_profile
from pathlib import Path
from matplotlib import pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
data_path = PROJECT_ROOT / 'data'
pv_energy_df = import_profile(data_path/'pv_profile_random_10 kW.xlsx', data_type="excel")
print(pv_energy_df)

plt.plot(pv_energy_df['Energy'])
plt.show()