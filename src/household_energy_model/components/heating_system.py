import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class HeatingSystem:
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

    def heating(self):
        if self.type == 'heat_pump':
            cop = 3
