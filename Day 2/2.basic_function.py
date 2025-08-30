import cv2
import numpy as np  


### 1. Convert to grayscale

#img = cv2.imread(r"C:\Users\HP\Computer-Vision-Course\Day 2\resources\lena.png")
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print("Original Shape: ", img.shape)
#print("Grayscale Shape: ", img_gray.shape)
#cv2.imshow("Color_img", img)
#cv2.imshow("Gray_img", img_gray)
#cv2.waitKey(0)


### Convert to Blur

#img = cv2.imread(r"C:\Users\HP\Computer-Vision-Course\Day 2\resources\lena.png")
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img_blur = cv2.GaussianBlur(img_gray, (7,7),0)
#print("Color_img Shape:", img.shape)
#print("Gray_img Shape:", img_gray.shape)
#cv2.imshow("Color_img", img)
#cv2.imshow("Gray_img", img_gray)
#cv2.imshow("Blur_img", img_blur)
#cv2.waitKey(0)



### Convert to cannyImg
img = cv2.imread(r"C:\Users\HP\Computer-Vision-Course\Day 2\resources\lena.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7),0)
img_canny = cv2.Canny(img_blur, 100,100)
print("Color_img Shape:", img.shape)
print("Gray_img Shape:", img_gray.shape)
cv2.imshow("Color_img", img)
cv2.imshow("Gray_img", img_gray)    
cv2.imshow("Blur_img", img_blur)
cv2.imshow("Canny_img", img_canny)
cv2.waitKey(0)