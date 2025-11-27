"""
Question 2: Implement a smoothing spatial filter (e.g., averaging filter) and a sharpening spatial filter (e.g., Laplacian filter) using convolution.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read and convert image to RGB
img = cv2.imread("../assets/flower.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define filters
# Smoothing filter: 3x3 averaging filter (all values are 1/9)
# Sharpening filter: Laplacian filter kernel
filter = {
    "Original": img,
    "smoothed": cv2.filter2D(img, -1, np.ones((3, 3), np.float32) / 9),
    "Sharpened": cv2.filter2D(img, -1, np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]))
}

# Display results
for i, (title, result) in enumerate(filter.items(), 1):
    plt.subplot(1, 3, i)
    plt.imshow(result)
    plt.title(title)
    plt.axis("off")
plt.show()

