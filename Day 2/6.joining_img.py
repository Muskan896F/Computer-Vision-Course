import cv2
import numpy as np

img = cv2.imread(r"C:\Users\HP\Computer-Vision-Course\Day 2\resources\lena.png")

img_hor = np.hstack((img,img))
img_ver = np.vstack((img,img))

cv2.imshow("Horizontal", img_hor)
cv2.imshow("Vertical", img_ver)
cv2.waitKey(0)