# Program 5: Frequency Domain Filters

## Question
Implement ideal, Butterworth, and Gaussian frequency domain filters for smoothing and sharpening. Apply these filters to a given image and visualize the effects.

## Aim
To implement and compare three types of frequency domain filters (Ideal, Butterworth, and Gaussian) for both low-pass (smoothing) and high-pass (sharpening) operations.

## Algorithm

**Step 1**: Load image and get dimensions
   - Read image and convert BGR to RGB
   - Get image dimensions: `rows, cols = img.shape[:2]`
   - Calculate center: `center_row = rows // 2`, `center_col = cols // 2`

**Step 2**: Create distance matrix
   - Generate coordinate meshgrid: `U, V = meshgrid([0..cols-1], [0..rows-1])`
   - Calculate Euclidean distance from center: `D = sqrt((V - center_row)² + (U - center_col)²)`

**Step 3**: Define filter transfer functions (cutoff D0 = 30)
   - Ideal Low-Pass: `H(u,v) = 1 if D(u,v) ≤ D0, else 0`
   - Butterworth Low-Pass: `H(u,v) = 1 / (1 + (D(u,v)/D0)^(2n))` where n=2
   - Gaussian Low-Pass: `H(u,v) = exp(-D(u,v)² / (2*D0²))`

**Step 4**: Apply filters to each color channel
   - For each channel i in [R, G, B]:
     - Compute FFT: `F = fftshift(fft2(channel_i))`
     - Multiply with filter: `F_filtered = F * H`
     - Compute inverse FFT: `channel_filtered = abs(ifft2(ifftshift(F_filtered)))`
   - Merge channels: `result = merge([R_filtered, G_filtered, B_filtered])`

**Step 5**: Generate high-pass filters
   - For each filter H: `H_highpass = 1 - H`
   - Apply same process as Step 4 with high-pass filter

**Step 6**: Display all results in 2×4 grid (original + 7 filtered versions)

## Program Logic

1. **Image Preprocessing**:
   - Read the input image and convert to RGB
   - Calculate image center coordinates for frequency domain operations

2. **Distance Matrix Creation**:
   - Create a meshgrid representing pixel coordinates
   - Calculate Euclidean distance from each pixel to the center (D)
   - This distance represents frequency in the frequency domain

3. **Filter Definitions**:
   - **Ideal Filter**: Binary filter that passes frequencies below cutoff (D ≤ D0) and blocks others
   - **Butterworth Filter**: Smooth transition filter with order n: `1 / (1 + (D/D0)^(2n))`
   - **Gaussian Filter**: Smooth exponential filter: `exp(-D²/(2D0²))`

4. **Filter Application**:
   - Convert image to frequency domain using FFT
   - Multiply frequency domain image with filter transfer function
   - Convert back to spatial domain using inverse FFT
   - Apply to each color channel separately

5. **Low-Pass vs High-Pass**:
   - Low-Pass Filter (LPF): Uses filter H directly (smoothing/blurring)
   - High-Pass Filter (HPF): Uses 1 - H (sharpening/edge enhancement)

6. **Visualization**: Display original image and all filtered versions in a 2×4 grid layout.

## Code

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read and convert image to RGB
img = cv2.cvtColor(cv2.imread('./assets/parrot.jpg'), cv2.COLOR_BGR2RGB)
r, c = img.shape[:2]
crow, ccol = r//2, c//2

# Create distance matrix from center
U, V = np.meshgrid(np.arange(c), np.arange(r))
D = np.sqrt((V-crow)**2 + (U-ccol)**2)

# Define filter functions
filters = {
    'Ideal': lambda D, D0, n=2: (D <= D0).astype(float),
    'Butterworth': lambda D, D0, n=2: 1 / (1 + (D/D0)**(2*n)),
    'Gaussian': lambda D, D0, n=2: np.exp(-(D**2)/(2*(D0**2)))
}

# Function to apply frequency domain filter
def apply(img, H, hp=False):
    if hp:  # High-pass filter
        H = 1 - H
    return cv2.merge([np.abs(np.fft.ifft2(np.fft.ifftshift(np.fft.fftshift(np.fft.fft2(img[:,:,i])) * H))) for i in range(3)]).astype(np.uint8)

# Apply filters
results = {'Original': img}
for name, func in filters.items():
    H = func(D, 30)  # Cutoff frequency D0 = 30
    results[f'{name} LPF'] = apply(img, H)  # Low-pass filter
    results[f'{name} HPF'] = apply(img, H, hp=True)  # High-pass filter

# Display results
plt.figure(figsize=(14, 8))
for i, (k, v) in enumerate(results.items()):
    plt.subplot(2, 4, i+1)
    plt.imshow(v)
    plt.title(k)
    plt.axis('off')
plt.tight_layout()
plt.show()
```

