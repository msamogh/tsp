import numpy as np


def load_us_cities(normalize=True):
    cities = np.array(
        list(
            map(
                lambda line: list(map(int, line.split())),
                # open("att48_xy.txt").readlines(),
                open("ena/instances/tsp_22", "r").readlines()
            )
        )
    )
    norm_cities = (cities - cities.min(axis=0)) / (cities.max(axis=0) - cities.min(axis=0))
    return cities, norm_cities
