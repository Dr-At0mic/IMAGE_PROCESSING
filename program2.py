import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("flower.jpeg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
filter={"Original":img,
        "smoothed":cv2.filter2D(img,-1,np.ones((3,3),np.float32)/9),
        "Sharpened":cv2.filter2D(img,-1,np.array([[0,-1,0],[-1,4,-1],[0,-1,0]]))
        }
for i,(title,result) in enumerate(filter.items(),1):
    plt.subplot(1,3,i)
    plt.imshow(result)
    plt.title(title)
    plt.axis("off")
plt.show()
