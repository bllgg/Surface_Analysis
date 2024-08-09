import random


def height_data(rows, cols, minimum, maximum):
    # Generate the 2D array with random height data
    surface_data = [[random.randint(minimum, maximum) for _ in range(cols)] for _ in range(rows)]
    return surface_data
