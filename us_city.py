import numpy as np


def load_us_cities():
    return np.array(
        list(
            map(
                lambda line: list(map(int, line.split())),
                open("att48_xy.txt").readlines(),
            )
        )
    )
