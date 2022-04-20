import numpy as np


def load_cities(source, normalize=True):
    cities = np.array(
        list(
            map(
                lambda line: list(map(int, line.split())),
                open(f"city_data/{source}", "r").readlines()
            )
        )
    )
    norm_cities = (cities - cities.min(axis=0)) / (cities.max(axis=0) - cities.min(axis=0))
    return cities, norm_cities
