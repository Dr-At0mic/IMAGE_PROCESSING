"""
Question 4: Utilize Python libraries (e.g., NumPy, OpenCV) to perform Fourier Transform on an input image.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image and convert to RGB
img = cv2.imread("../assets/cat.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale for Fourier Transform
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform 2D Fast Fourier Transform
f = np.fft.fft2(gray)

# Shift zero frequency component to center
fshift = np.fft.fftshift(f)

# Calculate magnitude spectrum (log scale for better visualization)
magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

# Display original image and magnitude spectrum
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original image (color)")
plt.imshow(img_rgb)
plt.axis("off")
plt.subplot(1, 2, 2)
plt.title("Magnitude spectrum (Grayscale)")
plt.imshow(magnitude_spectrum, cmap="gray")
plt.axis("off")
plt.show()

