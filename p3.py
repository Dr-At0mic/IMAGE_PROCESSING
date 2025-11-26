import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("./assets/cat.jpeg")
img_gray = cv2.imread("cat.jpeg",0)
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
smoothed = cv2.blur(img_gray, (3,3))   
sharpened = cv2.filter2D(img_gray, -1, np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]))
titles = ["Original", "Smoothed", "Sharpened"]
images = [img, smoothed, sharpened]
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")
plt.show()
