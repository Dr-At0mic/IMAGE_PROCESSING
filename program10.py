import cv2, os, numpy as np
from math import log10, sqrt
import matplotlib.pyplot as plt
def psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return 100
    return 20 * log10(255.0 / sqrt(mse))
img = cv2.imread("./assets/cat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imwrite("./output/program10.png", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
formats = ["jpg", "png", "webp"]
print("Format | File Size (KB) | PSNR (dB)")
print("-----------------------------------")
images = [img]
titles = ["Original"]
for f in formats:
    name = f"compressed.{f}"
    cv2.imwrite(name, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    comp = cv2.imread(name)
    comp = cv2.cvtColor(comp, cv2.COLOR_BGR2RGB)
    size = os.path.getsize(name) / 1024
    quality = psnr(img, comp)
    print(f"{f.upper():<7}| {size:>10.2f} KB | {quality:>8.2f} dB")
    images.append(comp)
    titles.append(f"{f.upper()}\n{size:.1f}KB, {quality:.1f}dB")
plt.figure(figsize=(12, 4))
for i in range(len(images)):
    plt.subplot(1, len(images), i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis("off")
plt.show()
