import numpy as np

def flatten(list_of_lists):
    flat_list = []
    for sublist in list_of_lists:
        for x in sublist:
            flat_list.append(x)

    return flat_list
