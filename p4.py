import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("./assets/cat.jpeg")
img_rgb =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
f=np.fft.fft2(gray)
fshift= np.fft.fftshift(f)
magnitude_spectrum= 20* np.log(np.abs(fshift)+1)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original image (color)")
plt.imshow(img_rgb)
plt.axis("off")
plt.subplot(1,2,2)
plt.title("Magnitude spectrum(Grayscale)")
plt.imshow(magnitude_spectrum, cmap="gray")
plt.axis("off")
plt.show()
