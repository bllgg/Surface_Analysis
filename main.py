# Imports
from analyzeByHeight import analyze_by_height
from analyzeByColor import analyze_by_color
from Height.heightData import generate_height_data

import os
import cv2


def image_analyze(analyze_function, surface, lower_mid=0, upper_mid=0):
    if analyze_function == "color":
        return analyze_by_color(surface)
    else:
        return analyze_by_height(surface, lower_mid, upper_mid)


if __name__ == '__main__':
    function_color = "color"  # "color" or "height"
    function_height = "height"

    folder_path = 'Images/SurfaceData'
    file_path = 'results.txt'
    files = os.listdir(folder_path)
    # Filter out non-image files (optional)
    image_files = [file for file in files if file.endswith(('.PNG', 'png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    results = []
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        img = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        python_2d_rgb_array = image_rgb.tolist()
        result = (image_analyze(function_color, python_2d_rgb_array))
        results.append(result)

    # Open the file in append mode
    with open(file_path, 'a') as file:
        for result, file_name in zip(results, image_files):
            res = ' '.join(str(num) for num in result)
            file.write(file_name + ": " + res + '\n')  # Append each word to the file with a newline character

    print(f"Words have been appended to {file_path}")
