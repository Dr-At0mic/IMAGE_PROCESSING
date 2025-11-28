# Program 8: Edge Detection

## Question
Implement edge detection techniques (e.g., Sobel operator, Canny edge detector) to detect edges in an image. Display the original image and edge-detected results.

## Aim
To implement and compare different edge detection techniques (Sobel operator and Canny edge detector) to identify boundaries and edges in an image.

## Algorithm

**Step 1**: Load image and convert to grayscale
   - Read image: `img = cv2.imread(path)`
   - Convert BGR to RGB: `img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`
   - Convert to grayscale: `gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)`

**Step 2**: Apply Sobel operator in X-direction
   - Compute horizontal gradient: `gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)`
   - Uses kernel: `[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]`
   - Detects vertical edges (horizontal intensity changes)

**Step 3**: Apply Sobel operator in Y-direction
   - Compute vertical gradient: `gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)`
   - Uses kernel: `[[-1, -2, -1], [0, 0, 0], [1, 2, 1]]`
   - Detects horizontal edges (vertical intensity changes)

**Step 4**: Compute Sobel edge magnitude
   - Calculate magnitude: `sobel_edges = sqrt(gx² + gy²)`
   - Use `cv2.magnitude(gx, gy)` to combine gradients
   - Result shows edge strength at each pixel

**Step 5**: Apply Canny edge detector
   - Apply Gaussian blur to reduce noise
   - Compute gradient magnitude and direction
   - Apply non-maximum suppression to thin edges
   - Apply double threshold (low=100, high=200) to detect edges
   - Use hysteresis to connect edge segments
   - Result: `canny_edges = cv2.Canny(gray, 100, 200)`

**Step 6**: Display results
   - Create 1×3 subplot layout
   - Display original color image, Sobel edges (hot colormap), and Canny edges (hot colormap)

## Program Logic

1. **Image Preprocessing**: 
   - Read the input image and convert from BGR to RGB color space
   - Convert to grayscale as edge detection works on single-channel images

2. **Sobel Edge Detection**:
   - **Sobel Operator**: First-order derivative operator that computes gradient magnitude
   - Apply Sobel in X-direction to detect vertical edges (horizontal intensity changes)
   - Apply Sobel in Y-direction to detect horizontal edges (vertical intensity changes)
   - Combine gradients using magnitude calculation: `magnitude = sqrt(gx² + gy²)`
   - Result shows edge strength with higher values indicating stronger edges

3. **Canny Edge Detection**:
   - **Canny Algorithm**: Multi-stage edge detection algorithm
   - Applies Gaussian smoothing to reduce noise
   - Computes gradient magnitude and direction
   - Uses non-maximum suppression to thin edges
   - Applies double thresholding (low threshold = 100, high threshold = 200)
   - Uses edge tracking by hysteresis to connect edge segments
   - Produces binary edge map with thin, connected edges

4. **Visualization**:
   - Display original color image
   - Display Sobel edges using 'hot' colormap to visualize gradient magnitudes
   - Display Canny edges using 'hot' colormap for consistency
   - All images shown side-by-side for comparison

## Code

```python
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
```

