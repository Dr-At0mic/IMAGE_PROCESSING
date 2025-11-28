import cv2
import matplotlib.pyplot as plt

img = cv2.cvtColor(cv2.imread("../assets/cat.jpg"), cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = cv2.magnitude(gx, gy)
canny_edges = cv2.Canny(gray, 100, 200)
images = [img, sobel_edges, canny_edges]
titles = ["Original (Color)", "Sobel (Colored)", "Canny (Colored)"]
cmaps = [None, "hot", "hot"]
plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap=cmaps[i])
    plt.title(titles[i])
    plt.axis("off")
plt.show()
