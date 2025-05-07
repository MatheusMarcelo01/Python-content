import cv2
import numpy as np
import potrace
from PIL import Image

# Caminho da imagem PNG
input_image_path = "pref.png"
output_svg_path = "imagem_vetorizada.svg"

image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

bitmap = potrace.Bitmap((binary_image // 255).astype(np.uint8))
path = bitmap.trace()

with open(output_svg_path, "w") as svg_file:
    svg_file.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n')
    for curve in path:
        svg_file.write('<path d="')
        start = curve.start_point
        svg_file.write(f'M {start[0]} {start[1]} ')
        for segment in curve:
            if segment.is_corner:
                c = segment.c
                end = segment.end_point
                svg_file.write(f'L {c[0]} {c[1]} L {end[0]} {end[1]} ')
            else:
                c1, c2 = segment.c1, segment.c2
                end = segment.end_point
                svg_file.write(f'C {c1[0]} {c1[1]}, {c2[0]} {c2[1]}, {end[0]} {end[1]} ')
        svg_file.write('" fill="black"/>\n')
    svg_file.write('</svg>')
