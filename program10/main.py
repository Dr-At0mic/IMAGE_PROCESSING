"""
Question 10: Evaluate the trade-offs between compression ratio and image quality for different compression standards.
"""

import cv2
import os
import numpy as np
from math import log10, sqrt
import matplotlib.pyplot as plt

def psnr(original, compressed):
    """
    Calculate Peak Signal-to-Noise Ratio (PSNR) between two images.
    Args:
        original: Original image array
        compressed: Compressed image array
    Returns:
        PSNR value in decibels (dB)
    """
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return 100  # Perfect match
    return 20 * log10(255.0 / sqrt(mse))

# Read and convert image to RGB
img = cv2.imread("../assets/cat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Save original image
cv2.imwrite("../output/program10/original.png", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

# Test different compression formats
formats = ["jpg", "png", "webp"]

print("Format | File Size (KB) | PSNR (dB)")
print("-----------------------------------")

images = [img]
titles = ["Original"]

# Process each format
for f in formats:
    name = f"../output/program10/compressed.{f}"
    cv2.imwrite(name, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    comp = cv2.imread(name)
    comp = cv2.cvtColor(comp, cv2.COLOR_BGR2RGB)
    
    # Calculate file size and quality metrics
    size = os.path.getsize(name) / 1024  # Size in KB
    quality = psnr(img, comp)  # PSNR in dB
    
    print(f"{f.upper():<7}| {size:>10.2f} KB | {quality:>8.2f} dB")
    
    images.append(comp)
    titles.append(f"{f.upper()}\n{size:.1f}KB, {quality:.1f}dB")

# Display results
plt.figure(figsize=(12, 4))
for i in range(len(images)):
    plt.subplot(1, len(images), i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis("off")
plt.show()

