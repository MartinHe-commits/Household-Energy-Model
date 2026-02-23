from pathlib import Path
import pandas as pd

def import_profile(path):
    suffix = ""
    for index, sign in enumerate(str(path)):
        if sign == '.':
            suffix = str(path)[index:]
            break

    if suffix == ".csv":
        df = pd.read_csv(path)

    elif suffix == ".xlsx":
        df = pd.read_excel(path, sheet_name=0, parse_dates=['Date'])


    else: raise NotImplementedError("unkonwn data type suffix")

    if 'Date' not in df.columns:
        raise ValueError("import error: missing 'Date' column")

    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date').sort_index()

    return df



