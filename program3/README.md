# Program 3: Apply Filters to Grayscale Image

## Question
Apply the filters to a given grayscale image and display the results.

## Aim
To apply smoothing and sharpening spatial filters to a grayscale image and visualize the effects of each filter.

## Algorithm

**Step 1**: Load image in both color and grayscale formats
   - Load color image: `img = cv2.imread(path)`
   - Load grayscale image: `img_gray = cv2.imread(path, 0)`
   - Convert color image from BGR to RGB

**Step 2**: Apply smoothing filter to grayscale image
   - Use `cv2.blur(img_gray, (3, 3))` which computes average of 3×3 neighborhood
   - For each pixel, replace with mean of surrounding 9 pixels

**Step 3**: Apply sharpening filter to grayscale image
   - Define kernel: `[[0, -1, 0], [-1, 5, -1], [0, -1, 0]]`
   - Use `cv2.filter2D()` to apply convolution
   - Formula: `output = original + (original - blurred)`

**Step 4**: Prepare display arrays
   - Create titles list: ["Original", "Smoothed", "Sharpened"]
   - Create images list: [original_color, smoothed_gray, sharpened_gray]

**Step 5**: Display results in subplot layout
   - Create 1×3 subplot grid
   - Display each image with grayscale colormap

## Program Logic

1. **Image Loading**: 
   - Read the image in both color and grayscale formats
   - Convert color image from BGR to RGB for display purposes

2. **Smoothing Filter Application**:
   - Use `cv2.blur()` with a 3×3 kernel to apply an averaging filter
   - This reduces noise and smooths out fine details

3. **Sharpening Filter Application**:
   - Apply a sharpening kernel `[[0, -1, 0], [-1, 5, -1], [0, -1, 0]]` using `cv2.filter2D()`
   - This kernel enhances edges and increases local contrast

4. **Result Display**: 
   - Create a subplot layout with three images side-by-side
   - Display original, smoothed, and sharpened versions
   - Use grayscale colormap for proper visualization

## Code

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in both color and grayscale
img = cv2.imread("./assets/cat.jpg")
img_gray = cv2.imread("./assets/cat.jpg", 0)
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
```

## Output

![Filters Applied to Grayscale Image](../output/program3.png)

