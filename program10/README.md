# Program 10: Compression Ratio vs Image Quality Trade-offs

## Question
Evaluate the trade-offs between compression ratio and image quality for different compression standards.

## Aim
To evaluate and compare different image compression formats (JPEG, PNG, WebP) by analyzing the trade-off between file size (compression ratio) and image quality (measured using PSNR).

## Algorithm

**Step 1**: Load original image and convert BGR to RGB
   - Read image: `img = cv2.imread(path)`
   - Convert: `img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`

**Step 2**: Save original image for reference

**Step 3**: For each compression format (JPEG, PNG, WebP):
   - Save image in format: `cv2.imwrite(filename, image)`
   - Read compressed image back: `compressed = cv2.imread(filename)`
   - Convert compressed image to RGB

**Step 4**: Calculate Mean Squared Error (MSE)
   - Compute pixel-wise squared difference: `diff = (original - compressed)²`
   - Calculate mean: `MSE = mean(diff)`

**Step 5**: Calculate PSNR (Peak Signal-to-Noise Ratio)
   - If MSE = 0: return 100 (perfect match)
   - Otherwise: `PSNR = 20 * log10(255 / sqrt(MSE))`
   - Higher PSNR indicates better quality

**Step 6**: Calculate file size
   - Get file size in bytes: `size_bytes = os.path.getsize(filename)`
   - Convert to KB: `size_kb = size_bytes / 1024`

**Step 7**: Store results
   - Store compressed image, file size, and PSNR value
   - Print format, file size, and PSNR in table format

**Step 8**: Display comparison
   - Create subplot layout with original and all compressed versions
   - Show file size and PSNR in title for each image

## Program Logic

1. **Image Loading**: Read the input image and convert from BGR to RGB color space.

2. **PSNR Calculation**:
   - **PSNR (Peak Signal-to-Noise Ratio)**: Measures image quality by comparing original and compressed images
   - Formula: `PSNR = 20 * log10(255 / sqrt(MSE))`
   - Higher PSNR indicates better quality (less distortion)
   - MSE (Mean Squared Error) calculates average squared difference between pixels

3. **Compression Testing**:
   - Save the image in different formats: JPEG, PNG, and WebP
   - Each format uses different compression algorithms:
     - **JPEG**: Lossy compression, good for photographs
     - **PNG**: Lossless compression, preserves quality but larger files
     - **WebP**: Modern format with both lossy and lossless modes

4. **Metrics Calculation**:
   - **File Size**: Measure compressed file size in KB
   - **PSNR**: Calculate quality metric by comparing compressed image to original
   - **Compression Ratio**: Implicitly shown through file size comparison

5. **Trade-off Analysis**:
   - Compare file sizes across formats
   - Compare PSNR values (quality) across formats
   - Identify which format offers best balance of size and quality

6. **Visualization**: Display original and compressed images side-by-side with file size and PSNR metrics.

## Code

```python
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
img = cv2.imread("./assets/cat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Save original image
cv2.imwrite("original.png", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

# Test different compression formats
formats = ["jpg", "png", "webp"]

print("Format | File Size (KB) | PSNR (dB)")
print("-----------------------------------")

images = [img]
titles = ["Original"]

# Process each format
for f in formats:
    name = f"compressed.{f}"
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
```

