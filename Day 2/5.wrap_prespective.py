import cv2
import numpy as np

img = cv2.imread(r"C:\Users\HP\Computer-Vision-Course\Day 2\resources\cards.jpg")
pts1 = np.float32([[752,118],[1120,265],[540,668],[871,830]])
width, height = 250, 350
pts2 = np.float32([[0,0], [width, 0], [0,height], [width, height]])

metrix = cv2.getPerspectiveTransform(pts1, pts2)
img_out = cv2.warpPerspective(img, metrix, (width, height))

cv2.imshow("cards", img)
cv2.imshow('cards_wrap',img_out)
cv2.waitKey(0)