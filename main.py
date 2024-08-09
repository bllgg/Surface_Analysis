# Imports
from analyzeByHeight import analyze_by_height
from analyzeByColor import analyze_by_color
from Height.heightData import generate_height_data

import cv2


def image_analyze(analyze_function, surface, lower_mid=0, upper_mid=0):
    if analyze_function == "color":
        print(analyze_by_color(surface))
    else:
        print(analyze_by_height(surface, lower_mid, upper_mid))


if __name__ == '__main__':
    function_color = "color"  # "color" or "height"
    function_height = "height"

    # COLOR DATA
    # Test case 1
    image_multicolor = cv2.imread('Images/sample2.jpg')
    image_rgb = cv2.cvtColor(image_multicolor, cv2.COLOR_BGR2RGB)
    python_2d_rgb_array = image_rgb.tolist()
    image_analyze(function_color, python_2d_rgb_array)

    # Test case 2
    image_red = cv2.imread('Images/red.jpg')
    image_rgb = cv2.cvtColor(image_red, cv2.COLOR_BGR2RGB)
    python_2d_rgb_array = image_rgb.tolist()
    image_analyze(function_color, python_2d_rgb_array)

    # Test case 3
    image_green = cv2.imread('Images/green.jpg')
    image_rgb = cv2.cvtColor(image_green, cv2.COLOR_BGR2RGB)
    python_2d_rgb_array = image_rgb.tolist()
    image_analyze(function_color, python_2d_rgb_array)

    # Test case 4
    image_blue = cv2.imread('Images/blue.jpg')
    image_rgb = cv2.cvtColor(image_blue, cv2.COLOR_BGR2RGB)
    python_2d_rgb_array = image_rgb.tolist()
    image_analyze(function_color, python_2d_rgb_array)

    # HEIGHT DATA
    # Test case 5
    surface_height_data = generate_height_data(100, 100, 0, 100)
    image_analyze(function_height, surface_height_data, 40, 60)
