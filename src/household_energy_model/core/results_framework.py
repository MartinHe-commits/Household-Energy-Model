import pandas as pd
import numpy as np

class ResulsFramework:
    def __init__(self, results, base_time):
        self.results = results
        self.base_time = base_time

    # erstelle leeres results-framework
    def results_setup(self):
        results_df = pd.DataFrame
        for result in self.results:
            if result == "E.PV":
                results_df['E.PV'] = np.full(self.base_time.N, np.nan)
