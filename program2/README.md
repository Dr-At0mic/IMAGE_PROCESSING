# Program 2: Spatial Filters (Smoothing and Sharpening)

## Question
Implement a smoothing spatial filter (e.g., averaging filter) and a sharpening spatial filter (e.g., Laplacian filter) using convolution.

## Aim
To implement and apply spatial filters for image smoothing and sharpening using convolution operations.

## Algorithm

**Step 1**: Load image from file and convert from BGR to RGB color space

**Step 2**: Define smoothing filter kernel
   - Create 3×3 matrix filled with 1/9: `kernel_smooth = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]`

**Step 3**: Define sharpening filter kernel
   - Create Laplacian kernel: `kernel_sharpen = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]`

**Step 4**: Apply smoothing filter using convolution
   - For each pixel (i, j) in image, compute: `output[i,j] = sum(kernel_smooth * image[i-1:i+2, j-1:j+2])`
   - Use `cv2.filter2D()` to perform 2D convolution

**Step 5**: Apply sharpening filter using convolution
   - For each pixel (i, j) in image, compute: `output[i,j] = sum(kernel_sharpen * image[i-1:i+2, j-1:j+2])`
   - Use `cv2.filter2D()` to perform 2D convolution

**Step 6**: Display original, smoothed, and sharpened images in subplot layout

## Program Logic

1. **Image Loading**: Read an image and convert it from BGR to RGB color space for proper display.

2. **Filter Definition**:
   - **Smoothing Filter**: Creates a 3×3 averaging filter kernel where each element is 1/9. This filter averages pixel values in a 3×3 neighborhood, effectively blurring the image.
   - **Sharpening Filter**: Uses a Laplacian filter kernel `[[0, -1, 0], [-1, 4, -1], [0, -1, 0]]` which enhances edges and details by emphasizing intensity differences.

3. **Convolution**: Apply filters using OpenCV's `filter2D()` function which performs 2D convolution between the image and the filter kernel.

4. **Visualization**: Display original, smoothed, and sharpened images side-by-side using matplotlib subplots.

## Code

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read and convert image to RGB
img = cv2.imread("./assets/flower.jpg")
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
```

