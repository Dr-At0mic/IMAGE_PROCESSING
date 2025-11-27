# Program 1: Histogram Equalization

## Question
Write Python code to perform histogram equalization on a grayscale image. Display the original and equalized images along with their histograms.

## Aim
To implement histogram equalization on a grayscale image to enhance image contrast by redistributing pixel intensities uniformly across the histogram.

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

