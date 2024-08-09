"""
Surface is a 2D array which contains surface height data
[
[[r11, g11, b11], [r12, g12, b12], [r11, g11, b13], ... , [r1m, g1m, b1m]],
[[r21, g21, b21], [r22, g22, b22], [r23, g23, b23], ... , [r2m, g2m, b2m]],
.
.
.
[[rn1, gn1, bn1], [rn2, gn2, bn2], [rn3, gn3, bn3], ... , [rnm, gnm, bnm]]
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
    return round(low_height_proportion, 3), round(mid_height_proportion, 3), round(high_height_proportion, 3)
