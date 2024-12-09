import cv2
import face_recognition as fr
import numpy as np

img=fr.load_image_file('jackie.jpg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

imgtest=fr.load_image_file('jackie2.jpg')
imgtest= cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)
imgloc=fr.face_locations(img)[0]
imgEncode=fr.face_encodings(img)[0]
cv2.rectangle(img,(imgloc[3],imgloc[0]),(imgloc[1],imgloc[2]),(255,0,255),2)

imgloctest=fr.face_locations(imgtest)[0]
imgtestEncode=fr.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(imgloctest[3],imgloctest[0]),(imgloctest[1],imgloctest[2]),(255,0,255),2)


results=fr.compare_faces([imgEncode],imgtestEncode)
faceDis=fr.face_distance([imgEncode],imgtestEncode)
print(results,faceDis)
cv2.putText(imgtest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

cv2.imshow('Jackie',img)
cv2.imshow('Jackie test',imgtest)
cv2.waitKey(0)