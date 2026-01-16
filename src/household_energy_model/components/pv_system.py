import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class PVSystem:
    def __init__(self, name, power):
        self.name = name
        #power in kW
        self.power = power

    #Probeweise initialisierung eines power-profiles - später: Profile-Import aus einer Datei
    def init_power_profile(self):
        power_profile = np.zeros(100)
        for i in range(100):
            if i >= 20 and i <= 40:
                power_profile[i] = 1

            if i >= 60 and i <= 80:
                power_profile[i] = 1

        self.power_profile = power_profile
        print(self.power_profile)
        plt.plot(self.power_profile)
        plt.show()

    #ToDo: Import von Erzeugungs-Profilen



