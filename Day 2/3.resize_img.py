import cv2
import numpy as np

#img = cv2.imread(r"C:\Users\HP\Computer-Vision-Course\Day 2\resources\lambo.png")
#print(img.shape)
#resized_img = cv2.resize(img, (300,200))
#print(resized_img.shape)
#cv2.imshow("Output", img)
#cv2.imshow('Resized Image', resized_img)
#cv2.waitKey(0)


### Cropping Images
img = cv2.imread(r"C:\Users\HP\Computer-Vision-Course\Day 2\resources\lambo.png")
crop_img = img[0:200, 200:500]
cv2.imshow("Output", img)
cv2.imshow('Cropped Image', crop_img)
cv2.waitKey(0)