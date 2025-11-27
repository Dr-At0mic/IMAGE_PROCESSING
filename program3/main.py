"""
Question 3: Apply the filters to a given grayscale image and display the results.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in both color and grayscale
img = cv2.imread("../assets/cat.jpg")
img_gray = cv2.imread("../assets/cat.jpg", 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply smoothing filter (averaging filter)
smoothed = cv2.blur(img_gray, (3, 3))

# Apply sharpening filter (Laplacian-based)
sharpened = cv2.filter2D(img_gray, -1, np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]))

# Prepare titles and images for display
titles = ["Original", "Smoothed", "Sharpened"]
images = [img, smoothed, sharpened]

# Display results
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")
plt.show()

