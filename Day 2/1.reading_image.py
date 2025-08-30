import cv2

#img = cv2.imread(r"C:\Users\HP\Computer-Vision-Course\Day 2\resources\lena.png")


#print(img.shape)
#cv2.imshow("Output", img)
#cv2.waitKey(0)

# reading videos

#cap  = cv2.VideoCapture(r"C:\Users\HP\Computer-Vision-Course\Day 2\resources\elon.mp4")
#while True:
 #   success, img = cap.read()
  #  print(img.shape)
   # cv2.imshow("Output", img)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break



# reading webcam
cap  = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img = cap.read()
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break