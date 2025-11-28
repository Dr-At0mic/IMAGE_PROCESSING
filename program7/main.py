"""
Question 7: Compare the performance of these filters on noisy images in terms of restoration quality.
"""

import cv2
import numpy as np
from scipy.signal import wiener
import matplotlib.pyplot as plt
import os

# Load image
img_color = cv2.imread('../assets/cat.jpg')
img_color_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0

# Add Gaussian noise
gaussian = np.clip(img + 0.05 * np.random.randn(*img.shape), 0, 1)

# Add salt-and-pepper noise
sp = img.copy()
prob = 0.05
rand = np.random.rand(*img.shape)
sp[rand < prob/2] = 0
sp[rand > 1 - prob/2] = 1

# Filters for Gaussian noise
mean_gauss = cv2.blur(gaussian, (3, 3))
median_gauss = cv2.medianBlur((gaussian*255).astype(np.uint8), 3) / 255.0
wiener_gauss = wiener(gaussian, (5, 5))

# Filters for Salt-and-Pepper noise
mean_sp = cv2.blur(sp, (3, 3))
median_sp = cv2.medianBlur((sp*255).astype(np.uint8), 3) / 255.0
wiener_sp = wiener(sp, (5, 5))

# Show Gaussian noise results
plt.figure(figsize=(12, 4))
titles = ["Original", "Gaussian", "Mean", "Median", "Wiener"]
images = [img_color_rgb, gaussian, mean_gauss, median_gauss, wiener_gauss]
for i in range(5):
    plt.subplot(1, 5, i+1)
    if i == 0:
        plt.imshow(images[i])
    else:
        plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()

# Show Salt-and-Pepper noise results
plt.figure(figsize=(12, 4))
titles2 = ["Original", "S&P", "Mean", "Median", "Wiener"]
images2 = [img_color_rgb, sp, mean_sp, median_sp, wiener_sp]
for i in range(5):
    plt.subplot(1, 5, i+1)
    if i == 0:
        plt.imshow(images2[i])
    else:
        plt.imshow(images2[i], cmap='gray')
    plt.title(titles2[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
