# Program 4: Fourier Transform on Images

## Question
Utilize Python libraries (e.g., NumPy, OpenCV) to perform Fourier Transform on an input image.

## Aim
To perform 2D Fast Fourier Transform (FFT) on an image and visualize the frequency domain representation (magnitude spectrum).

## Algorithm

**Step 1**: Load image and convert to grayscale
   - Read image using `cv2.imread()`
   - Convert BGR to RGB for display
   - Convert to grayscale: `gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`

**Step 2**: Apply 2D Fast Fourier Transform
   - Compute FFT: `F = fft2(gray)`
   - Result is complex-valued frequency domain representation

**Step 3**: Shift zero frequency to center
   - Apply `fftshift(F)` to move DC component from corner to center
   - This centers low frequencies and places high frequencies at edges

**Step 4**: Calculate magnitude spectrum
   - Compute magnitude: `magnitude = abs(F_shifted)`
   - Apply logarithmic scaling: `magnitude_spectrum = 20 * log(magnitude + 1)`
   - Adding 1 prevents log(0) errors

**Step 5**: Display results
   - Create figure with 1×2 subplot layout
   - Show original RGB image and magnitude spectrum side-by-side

## Program Logic

1. **Image Preprocessing**:
   - Read the input image
   - Convert from BGR to RGB for display
   - Convert to grayscale for Fourier Transform (FFT works on single-channel images)

2. **Fourier Transform**:
   - Apply 2D FFT using NumPy's `fft2()` function
   - This converts the image from spatial domain to frequency domain

3. **Frequency Shifting**:
   - Use `fftshift()` to move the zero-frequency component (DC component) to the center of the spectrum
   - This makes the frequency domain representation more intuitive to visualize

4. **Magnitude Spectrum Calculation**:
   - Calculate the magnitude of the complex FFT result using `np.abs()`
   - Apply logarithmic scaling (20 * log) to enhance visualization of frequency components
   - Add 1 to avoid log(0) errors

5. **Visualization**: Display the original image and its magnitude spectrum side-by-side.

## Code

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image and convert to RGB
img = cv2.imread("./assets/cat.jpg")
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
```

