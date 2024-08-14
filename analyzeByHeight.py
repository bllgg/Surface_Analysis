"""
Surface is a 2D array which contains surface height data
[
[h11, h12, h13, ... , h1m],
[h21, h22, h23, ... , h2m],
.
.
.
[hn1, hn2, hn3, ... , hnm]
]
"""


def analyze_by_height(surface, lower_mid_val, upper_mid_val):
    number_of_decimal_points = 4
    low_height_area = 0.0
    mid_height_area = 0.0
    high_height_area = 0.0
    for i in range(len(surface)):
        for j in range(len(surface[i])):
            if surface[i][j] > upper_mid_val:
                high_height_area += 1.0
            elif surface[i][j] > lower_mid_val:
                mid_height_area += 1.0
            else:
                low_height_area += 1.0
    sum_of_areas = low_height_area + mid_height_area + high_height_area
    low_height_proportion = low_height_area / sum_of_areas
    mid_height_proportion = mid_height_area / sum_of_areas
    high_height_proportion = high_height_area / sum_of_areas
    return round(low_height_proportion, number_of_decimal_points), round(mid_height_proportion, number_of_decimal_points), round(high_height_proportion, number_of_decimal_points)
