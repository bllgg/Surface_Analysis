"""
Surface is a 2D array which contains surface color data
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
    number_of_decimal_points = 2
    low_height_area = 0.0
    mid_height_area = 0.0
    high_height_area = 0.0

    for i in range(len(surface)):
        for j in range(len(surface[i])):
            r, g, b = surface[i][j]

            # Skip grey areas where RGB values are nearly equal
            if abs(r - g) <= 15 and abs(r - b) <= 15 and abs(g - b) <= 15:
                continue

            # Skip white areas where RGB values are close to 255
            if r > 235 and g > 235 and b > 235:
                continue

            # Calculate red zones
            if r > g and r > b:
                high_height_area += 1.0
            # Calculate green zones
            elif g > r and g > b:
                mid_height_area += 1.0
            # Calculate blue zones
            elif b > r and b > g:
                low_height_area += 1.0

    sum_of_areas = low_height_area + mid_height_area + high_height_area
    low_height_proportion = low_height_area / sum_of_areas
    mid_height_proportion = mid_height_area / sum_of_areas
    high_height_proportion = high_height_area / sum_of_areas

    return (
        round(low_height_proportion, number_of_decimal_points),
        round(mid_height_proportion, number_of_decimal_points),
        round(high_height_proportion, number_of_decimal_points)
    )
