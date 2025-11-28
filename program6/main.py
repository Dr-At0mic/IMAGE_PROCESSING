import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../assets/cat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def add_gaussian_noise(image, mean=0, var=0.01):
    noise = np.random.normal(mean, var**0.5, image.shape)
    noisy_img = np.clip(image / 255 + noise, 0, 1)
    return np.uint8(noisy_img * 255)

def add_salt_pepper_noise(image, amount=0.02):
    noisy = np.copy(image)
    total_pixels = image.size // 3
    num_salt = int(amount * total_pixels / 2)
    num_pepper = num_salt
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = [255, 255, 255]
    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = [0, 0, 0]
    return noisy

def apply_filters(noisy_img):
    mean_filtered = cv2.blur(noisy_img, (3, 3))
    median_filtered = cv2.medianBlur(noisy_img, 3)
    adaptive_filtered = cv2.bilateralFilter(noisy_img, 9, 75, 75)
    return mean_filtered, median_filtered, adaptive_filtered

gaussian_noisy = add_gaussian_noise(img)
sp_noisy = add_salt_pepper_noise(img)
mean_g, median_g, adaptive_g = apply_filters(gaussian_noisy)
mean_sp, median_sp, adaptive_sp = apply_filters(sp_noisy)
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
