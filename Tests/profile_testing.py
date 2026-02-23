from src.household_energy_model.io.import_profile import import_profile
from src.household_energy_model.core.base_time import BaseTime
from src.household_energy_model.components.pv_system import PVSystem
from src.household_energy_model.components.battery import Battery
from src.household_energy_model.components.heating_system import HeatingSystem
from src.household_energy_model.components.electricity_grid import ElectricityGrid

from pathlib import Path
import pytest
import pandas as pd
import numpy as np

def test_basetime_timestamp_datetime_index_validation():
    # get data path and import profile
    timestamps_dict = {'Date': ['2025-01-01', '2025-01-02', '2025-01-03'],
                     'Values': [1,2,3]}

    timestamps_df = pd.DataFrame(timestamps_dict)

    with pytest.raises(TypeError):
        base_time = BaseTime(time_series=timestamps_df)

def test_basetime_timestamp_duplicate_validation():
    timestamps_dict = {'Date': ['2025-02-01', '2025-02-01', '2025-03-02', '2025-04-03'],
                             'Values': [1, 2, 2, 3]}
    timestamps_df = pd.DataFrame(timestamps_dict)
    timestamps_df['Date'] = pd.to_datetime(timestamps_df['Date'])

    timestamps_df = timestamps_df.set_index('Date').sort_index()

    with pytest.raises(ValueError):
        base_time = BaseTime(time_series=timestamps_df)


def test_basetime_timestamp_comparison_validation():
    correct_timestamps_dict = {'Date': ['2025-01-01', '2025-01-02', '2025-01-03'],
                       'Values': [1, 2, 3]}
    wrong_timestamps_dict = {'Date': ['2025-02-01', '2025-03-02', '2025-04-03'],
                       'Values': [1, 2, 3]}
    correct_timestamps_df = pd.DataFrame(correct_timestamps_dict)
    wrong_timestamps_df = pd.DataFrame(wrong_timestamps_dict)

    correct_timestamps_df['Date'] = pd.to_datetime(correct_timestamps_df['Date'])
    wrong_timestamps_df['Date'] = pd.to_datetime(wrong_timestamps_df['Date'])

    correct_timestamps_df = correct_timestamps_df.set_index('Date').sort_index()
    wrong_timestamps_df = wrong_timestamps_df.set_index('Date').sort_index()

    # initialize base_time
    base_time = BaseTime(time_series=correct_timestamps_df)

    # initialize pv and heating_system
    base_time.check_time_series(correct_timestamps_df)

    with pytest.raises(ValueError):
        base_time.check_time_series(wrong_timestamps_df)

def test_component_set_profile():
    correct_timestamps_dict = {'Date': ['2025-01-01', '2025-01-02', '2025-01-03'],
                               'Values': [1, 2, 3]}
    wrong_timestamps_dict = {'Date': ['2025-02-01', '2025-03-02', '2025-04-03'],
                             'Values': [1, 2, 3]}
    correct_timestamps_df = pd.DataFrame(correct_timestamps_dict)
    wrong_timestamps_df = pd.DataFrame(wrong_timestamps_dict)

    correct_timestamps_df['Date'] = pd.to_datetime(correct_timestamps_df['Date'])
    wrong_timestamps_df['Date'] = pd.to_datetime(wrong_timestamps_df['Date'])

    correct_timestamps_df = correct_timestamps_df.set_index('Date').sort_index()
    wrong_timestamps_df = wrong_timestamps_df.set_index('Date').sort_index()

    # initialize base_time
    base_time = BaseTime(time_series=correct_timestamps_df)

    pv_system = PVSystem(base_time,name='pv_system', power=1)

    pv_system.set_profile(correct_timestamps_df)
    with pytest.raises(ValueError):
        pv_system.set_profile(wrong_timestamps_df)




if __name__ == '__main__':
    test_basetime_timestamp_datetime_index_validation()
    test_basetime_timestamp_duplicate_validation()
    test_basetime_timestamp_comparison_validation()
    test_component_set_profile()




