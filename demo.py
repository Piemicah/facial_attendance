import cv2
import face_recognition as fr

img=fr.load_image_file('jackie.jpg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

imgtest=fr.load_image_file('jackie2.jpg')
imgtest= cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)
cv2.imshow('Jackie',img)
cv2.imshow('Jackie test',imgtest)
cv2.waitKey(0)
