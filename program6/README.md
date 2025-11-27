# Program 6: Noise Models and Filtering

## Question
Generate synthetic noisy images using different noise models (e.g., Gaussian, salt-and-pepper). Implement mean filters, median filters, and adaptive filters for noise reduction.

## Aim
To generate noisy images using different noise models and apply various filtering techniques to reduce noise and restore image quality.

## Algorithm

**Step 1**: Load original image and convert BGR to RGB

**Step 2**: Add Gaussian noise
   - Generate noise matrix: `noise = normal(mean=0, std=sqrt(variance), size=image_shape)`
   - Normalize image to [0,1]: `normalized = image / 255`
   - Add noise: `noisy = normalized + noise`
   - Clip to [0,1] and convert back: `noisy_image = uint8(clip(noisy, 0, 1) * 255)`

**Step 3**: Add salt-and-pepper noise
   - Calculate number of pixels to corrupt: `num_pixels = amount * total_pixels / 2`
   - Generate random coordinates for salt noise (white pixels = 255)
   - Generate random coordinates for pepper noise (black pixels = 0)
   - Set pixels at coordinates to extreme values

**Step 4**: Apply mean filter
   - For each pixel, replace with average of 3×3 neighborhood
   - Use `cv2.blur(image, (3, 3))`

**Step 5**: Apply median filter
   - For each pixel, replace with median of 3×3 neighborhood
   - Use `cv2.medianBlur(image, 3)`

**Step 6**: Apply adaptive (bilateral) filter
   - Consider both spatial distance and intensity difference
   - Use `cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)`
   - Preserves edges while smoothing

**Step 7**: Process both noisy images
   - Apply all three filters to Gaussian noisy image
   - Apply all three filters to salt-and-pepper noisy image

**Step 8**: Display results in 3×3 grid layout

## Program Logic

1. **Image Loading**: Read and convert image from BGR to RGB color space.

2. **Gaussian Noise Generation**:
   - Generate random noise from a Gaussian distribution with specified mean and variance
   - Add noise to normalized image (0-1 range)
   - Clip values to valid range and convert back to uint8

3. **Salt-and-Pepper Noise Generation**:
   - Randomly select pixels to corrupt
   - Set some pixels to maximum intensity (255) - "salt" noise
   - Set some pixels to minimum intensity (0) - "pepper" noise
   - Equal number of salt and pepper pixels

4. **Noise Reduction Filters**:
   - **Mean Filter**: Uses `cv2.blur()` with 3×3 kernel to average neighboring pixels
   - **Median Filter**: Uses `cv2.medianBlur()` to replace each pixel with median of neighborhood (effective for salt-and-pepper noise)
   - **Adaptive Filter**: Uses `cv2.bilateralFilter()` which preserves edges while reducing noise by considering both spatial and intensity differences

5. **Processing Pipeline**:
   - Generate Gaussian noisy image and apply all three filters
   - Generate salt-and-pepper noisy image and apply all three filters

6. **Visualization**: Display original, noisy images, and filtered results in a 3×3 grid for comparison.

## Code

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read and convert image to RGB
img = cv2.imread("./assets/cat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ---------- Step 2: Add Gaussian Noise ----------
def add_gaussian_noise(image, mean=0, var=0.01):
    """
    Add Gaussian noise to an image.
    Args:
        image: Input image
        mean: Mean of Gaussian distribution (default: 0)
        var: Variance of Gaussian distribution (default: 0.01)
    Returns:
        Noisy image
    """
    noise = np.random.normal(mean, var**0.5, image.shape)
    noisy_img = np.clip(image / 255 + noise, 0, 1)
    return np.uint8(noisy_img * 255)

# ---------- Step 3: Add Salt-and-Pepper Noise ----------
def add_salt_pepper_noise(image, amount=0.02):
    """
    Add salt-and-pepper noise to an image.
    Args:
        image: Input image
        amount: Proportion of pixels to corrupt (default: 0.02)
    Returns:
        Noisy image
    """
    noisy = np.copy(image)
    total_pixels = image.size // 3
    num_salt = int(amount * total_pixels / 2)
    num_pepper = num_salt

    # Salt noise (white pixels)
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = [255, 255, 255]

    # Pepper noise (black pixels)
    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = [0, 0, 0]
    return noisy

# ---------- Step 4: Filtering ----------
def apply_filters(noisy_img):
    """
    Apply different filters to reduce noise.
    Args:
        noisy_img: Noisy input image
    Returns:
        Tuple of filtered images (mean, median, adaptive)
    """
    mean_filtered = cv2.blur(noisy_img, (3, 3))  # Mean filter
    median_filtered = cv2.medianBlur(noisy_img, 3)  # Median filter
    adaptive_filtered = cv2.bilateralFilter(noisy_img, 9, 75, 75)  # Adaptive (bilateral)
    return mean_filtered, median_filtered, adaptive_filtered

# ---------- Step 5: Process ----------
gaussian_noisy = add_gaussian_noise(img)
sp_noisy = add_salt_pepper_noise(img)

mean_g, median_g, adaptive_g = apply_filters(gaussian_noisy)
mean_sp, median_sp, adaptive_sp = apply_filters(sp_noisy)

# ---------- Step 6: Display ----------
titles = ['Original', 'Gaussian Noise', 'Mean', 'Median', 'Adaptive',
          'Salt & Pepper Noise', 'Mean', 'Median', 'Adaptive']
images = [img, gaussian_noisy, mean_g, median_g, adaptive_g,
          sp_noisy, mean_sp, median_sp, adaptive_sp]

plt.figure(figsize=(10, 8))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
```

