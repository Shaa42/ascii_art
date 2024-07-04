import cv2
import numpy as np

def imgToAscii(image, file_name):
    ascii_char = " .:-=+*#%@@"
    ascii_file = open(f"ascii_txt/{file_name}.txt", "w")
    for i in range(len(image)):
        for j in range(len(image[0])):
                index = round(np.mean(image[i][j]) / 255, 2)
                ascii_file.write(ascii_char[int(index * 10)])
        ascii_file.write("\n")



image_url = "images/Homer.png"
image = cv2.imread(image_url)
imgToAscii(image, "ascii_homer")

