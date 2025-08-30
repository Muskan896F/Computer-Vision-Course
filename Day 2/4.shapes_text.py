import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
print(img.shape)
img[:] = 255,0,0

# Create a line
#cv2.line(img, (120,55), (300,300), (0,255,0), 3)



## Create a rectangle
#cv2.rectangle(img, (0,0), (250,350), (0,0,255), 7)


## Create a circle
#cv2.circle(img, (400,50), 50, (0,0,255), 5)


### Put texts
cv2.putText(img, "OPENCV", (200,440), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 1)

cv2.imshow('Image', img)
cv2.waitKey(0)

