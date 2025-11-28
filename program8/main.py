"""
Question 8: Implement edge detection techniques (e.g., Sobel operator, Canny edge detector) to detect edges in an image.
Display the original image and edge-detected results.
"""

import cv2
import matplotlib.pyplot as plt

# Read image and convert to RGB
img = cv2.cvtColor(cv2.imread("../assets/cat.jpg"), cv2.COLOR_BGR2RGB)

# Convert to grayscale for edge detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel operator for edge detection
# Sobel X-direction (horizontal edges)
gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Sobel Y-direction (vertical edges)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Compute magnitude of gradient
sobel_edges = cv2.magnitude(gx, gy)

# Apply Canny edge detector
canny_edges = cv2.Canny(gray, 100, 200)

# Prepare images and titles for display
images = [img, sobel_edges, canny_edges]
titles = ["Original (Color)", "Sobel (Colored)", "Canny (Colored)"]
cmaps = [None, "hot", "hot"]  # No colormap for original image

# Display results
plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap=cmaps[i])
    plt.title(titles[i])
    plt.axis("off")
plt.show()

