"""
Question 1: Write Python code to perform histogram equalization on a grayscale image.
Display the original and equalized images along with their histograms.
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Read grayscale image
img = cv.imread("../assets/cat.jpg", 0)

# Perform histogram equalization
equ = cv.equalizeHist(img)

# Stack original and equalized images horizontally
res = np.hstack((img, equ))

# Save the result
cv.imwrite('../output/program1.png', res)

