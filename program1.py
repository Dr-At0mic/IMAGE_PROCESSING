import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread("E:\S3 MSc CS\DIP LAB\cat.jpg",0)
equ=cv.equalizeHist(img)
res=np.hstack((img,equ))
cv.imwrite('res.png',res)
