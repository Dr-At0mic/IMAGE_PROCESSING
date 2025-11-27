# Program 1: Histogram Equalization

## Question
Write Python code to perform histogram equalization on a grayscale image. Display the original and equalized images along with their histograms.

## Aim
To implement histogram equalization on a grayscale image to enhance image contrast by redistributing pixel intensities uniformly across the histogram.

## Algorithm

**Step 1**: Load grayscale image from file path using `cv.imread()` with flag 0

**Step 2**: Apply histogram equalization to the image using `cv.equalizeHist(img)`
   - Compute histogram of pixel intensities
   - Calculate cumulative distribution function (CDF)
   - Map each pixel intensity to new value: `new_intensity = round((L-1) * CDF(intensity))`
   - Where L is the number of intensity levels (256)

**Step 3**: Concatenate original and equalized images horizontally using `np.hstack()`

**Step 4**: Save the combined result image to output directory using `cv.imwrite()`

## Program Logic

1. **Image Loading**: Read a grayscale image using OpenCV's `imread()` function with flag 0 (grayscale mode).

2. **Histogram Equalization**: Apply histogram equalization using OpenCV's `equalizeHist()` function, which:
   - Calculates the cumulative distribution function (CDF) of pixel intensities
   - Maps each pixel intensity to a new value based on the CDF
   - Redistributes pixel intensities to cover the full dynamic range [0, 255]

3. **Result Display**: Stack the original and equalized images horizontally using NumPy's `hstack()` function for side-by-side comparison.

4. **Output**: Save the combined result image to the output directory.

## Code

```python
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Read grayscale image
img = cv.imread("./assets/cat.jpg", 0)

# Perform histogram equalization
equ = cv.equalizeHist(img)

# Stack original and equalized images horizontally
res = np.hstack((img, equ))

# Save the result
cv.imwrite('./output/program1.png', res)
```

