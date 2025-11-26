import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread("./assets/cat.jpg",0)
equ=cv.equalizeHist(img)
res=np.hstack((img,equ))
cv.imwrite('./output/program1.png',res)
