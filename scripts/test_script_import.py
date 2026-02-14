from src.household_energy_model.io.import_profile import import_profile
from src.household_energy_model.core.base_time import BaseTime
from src.household_energy_model.components.pv_system import PVSystem
from src.household_energy_model.components.battery import Battery
from src.household_energy_model.components.heating_system import HeatingSystem
from src.household_energy_model.components.electricity_grid import ElectricityGrid
from src.household_energy_model.utils.helper_functions import flatten
from pathlib import Path
import pandas as pd
from matplotlib import pyplot as plt

def main():
    # import profiles from .xlsx
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    data_path = PROJECT_ROOT / 'data'
    pv_energy_df = import_profile(data_path/'pv_profile_random_10 kW.xlsx')
    print(pv_energy_df)

    base_time = BaseTime(time_series=pv_energy_df)

    heating_system_el_energy_demad_df = import_profile(data_path/'heating_system_el_energy_demand_random_10 kW.xlsx')
    # print(pv_energy_df)
    # print(base_time.time_series)
    # print(base_time.N)
    # print(base_time.time_stamps)

    #initialize components
    component_list = []
    pv_system = PVSystem(base_time=base_time,name="PV-Anlage", power=10e3)
    pv_system.set_profile(pv_energy_df)
    battery = Battery(base_time=base_time, name="Battery", max_capacity=20e3)
    electricity_grid = ElectricityGrid(base_time=base_time, name="Electricity Grid")
    heating_system = HeatingSystem(base_time=base_time, name="Heating", heating_capacity=10e3, type='heat_pump')

    heating_system.set_profile(heating_system_el_energy_demad_df)
    # plt.plot(pv_system.energy_profile)
    # plt.show()
    component_list.append(pv_system)
    component_list.append(battery)
    component_list.append(electricity_grid)
    component_list.append(heating_system)

    results_columns_list = []

    for component in component_list:
        component.setup_results_schema()
        results_columns_list.extend(component.results_schema)

    results_df = pd.DataFrame(columns=results_columns_list, index=base_time.time_stamps)
    print(results_df)

if __name__ == '__main__':
    main()