from pathlib import Path
import pandas as pd

def import_profile(path, data_type):
    if data_type == "csv":
        df = pd.read_csv(path)
    elif data_type == "excel":
        df = pd.read_excel(path, sheet_name=0, parse_dates=['Date'])

    return df



