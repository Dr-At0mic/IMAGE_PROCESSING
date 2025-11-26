import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.cvtColor(cv2.imread('parrot.jpg'), cv2.COLOR_BGR2RGB)
r, c = img.shape[:2]; crow, ccol = r//2, c//2
U, V = np.meshgrid(np.arange(c), np.arange(r)); D = np.sqrt((V-crow)**2 + (U-ccol)**2)
filters = {
    'Ideal': lambda D, D0, n=2: (D <= D0).astype(float),
    'Butterworth': lambda D, D0, n=2: 1 / (1 + (D/D0)**(2*n)),
    'Gaussian': lambda D, D0, n=2: np.exp(-(D**2)/(2*(D0**2)))
}
def apply(img, H, hp=False):
    if hp: H = 1 - H
    return cv2.merge([np.abs(np.fft.ifft2(np.fft.ifftshift(np.fft.fftshift(np.fft.fft2(img[:,:,i])) * H))) for i in range(3)]).astype(np.uint8)
results = {'Original': img}
for name, func in filters.items():
    H = func(D, 30)
    results[f'{name} LPF'] = apply(img, H)
    results[f'{name} HPF'] = apply(img, H, hp=True)
plt.figure(figsize=(14, 8))
for i, (k, v) in enumerate(results.items()):
    plt.subplot(2, 4, i+1);
    plt.imshow(v);
    plt.title(k);
    plt.axis('off')
plt.tight_layout();
plt.show()
