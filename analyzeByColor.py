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


def analyze_by_color(surface):
    low_height_area = 0.0
    mid_height_area = 0.0
    high_height_area = 0.0
    for i in range(len(surface)):
        for j in range(len(surface[i])):
            # Calculate red zones
            if surface[i][j][0] > surface[i][j][1] and surface[i][j][0] > surface[i][j][2]:
                high_height_area += 1.0
            # Calculate green zones
            elif surface[i][j][1] > surface[i][j][0] and surface[i][j][1] > surface[i][j][2]:
                mid_height_area += 1.0
            # Calculate blue zones
            else:
                low_height_area += 1.0
    sum_of_areas = low_height_area + mid_height_area + high_height_area
    low_height_proportion = low_height_area / sum_of_areas
    mid_height_proportion = mid_height_area / sum_of_areas
    high_height_proportion = high_height_area / sum_of_areas
    return low_height_proportion, mid_height_proportion, high_height_proportion
