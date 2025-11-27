# IMAGE_PROCESSING
PG SEM 3

This repository contains image processing programs covering various topics including histogram equalization, spatial and frequency domain filtering, noise reduction, and image compression.

## Programs Overview

---

## [Program 1: Histogram Equalization](./program1/README.md)

**Question**: Write Python code to perform histogram equalization on a grayscale image. Display the original and equalized images along with their histograms.

**Aim**: To implement histogram equalization on a grayscale image to enhance image contrast by redistributing pixel intensities uniformly across the histogram.

[View Program Details →](./program1/README.md)

---

## [Program 2: Spatial Filters (Smoothing and Sharpening)](./program2/README.md)

**Question**: Implement a smoothing spatial filter (e.g., averaging filter) and a sharpening spatial filter (e.g., Laplacian filter) using convolution.

**Aim**: To implement and apply spatial filters for image smoothing and sharpening using convolution operations.

[View Program Details →](./program2/README.md)

---

## [Program 3: Apply Filters to Grayscale Image](./program3/README.md)

**Question**: Apply the filters to a given grayscale image and display the results.

**Aim**: To apply smoothing and sharpening spatial filters to a grayscale image and visualize the effects of each filter.

[View Program Details →](./program3/README.md)

---

## [Program 4: Fourier Transform on Images](./program4/README.md)

**Question**: Utilize Python libraries (e.g., NumPy, OpenCV) to perform Fourier Transform on an input image.

**Aim**: To perform 2D Fast Fourier Transform (FFT) on an image and visualize the frequency domain representation (magnitude spectrum).

[View Program Details →](./program4/README.md)

---

## [Program 5: Frequency Domain Filters](./program5/README.md)

**Question**: Implement ideal, Butterworth, and Gaussian frequency domain filters for smoothing and sharpening. Apply these filters to a given image and visualize the effects.

**Aim**: To implement and compare three types of frequency domain filters (Ideal, Butterworth, and Gaussian) for both low-pass (smoothing) and high-pass (sharpening) operations.

[View Program Details →](./program5/README.md)

---

## [Program 6: Noise Models and Filtering](./program6/README.md)

**Question**: Generate synthetic noisy images using different noise models (e.g., Gaussian, salt-and-pepper). Implement mean filters, median filters, and adaptive filters for noise reduction.

**Aim**: To generate noisy images using different noise models and apply various filtering techniques to reduce noise and restore image quality.

[View Program Details →](./program6/README.md)

---

## [Program 9: Lossless Compression (Huffman Coding)](./program9/README.md)

**Question**: Implement lossless compression techniques (e.g., Huffman coding) and lossy compression techniques (e.g., JPEG compression) using Python.

**Aim**: To implement Huffman coding, a lossless compression algorithm that assigns variable-length binary codes to characters based on their frequency, ensuring more frequent characters have shorter codes.

[View Program Details →](./program9/README.md)

---

## [Program 10: Compression Ratio vs Image Quality Trade-offs](./program10/README.md)

**Question**: Evaluate the trade-offs between compression ratio and image quality for different compression standards.

**Aim**: To evaluate and compare different image compression formats (JPEG, PNG, WebP) by analyzing the trade-off between file size (compression ratio) and image quality (measured using PSNR).

[View Program Details →](./program10/README.md)

---

## Directory Structure

```
IMAGE_PROCESSING/
├── assets/              # Input images
│   ├── cat.jpg
│   ├── flower.jpg
│   └── parrot.jpg
├── output/              # Output images
├── program1/            # Histogram Equalization
│   ├── main.py
│   └── README.md
├── program2/            # Spatial Filters
│   ├── main.py
│   └── README.md
├── program3/            # Apply Filters to Grayscale
│   ├── main.py
│   └── README.md
├── program4/            # Fourier Transform
│   ├── main.py
│   └── README.md
├── program5/            # Frequency Domain Filters
│   ├── main.py
│   └── README.md
├── program6/            # Noise Models and Filtering
│   ├── main.py
│   └── README.md
├── program9/            # Huffman Coding
│   ├── main.py
│   └── README.md
├── program10/           # Compression Trade-offs
│   ├── main.py
│   └── README.md
└── README.md            # This file
```

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy
- Matplotlib
- Collections (for Huffman coding)

## Usage

Each program can be run independently by navigating to its directory and executing:

```bash
cd program1
python main.py
```

Make sure the required assets are in the `assets/` directory relative to the program folder.
