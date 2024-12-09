import cv2

import face_recognition as fr
import os

import numpy as np
from datetime import datetime


imageDir='imageAttendance'


imageList= os.listdir(imageDir)

images=[]


names=[]

for image in imageList:

    img=cv2.imread(f'{imageDir}/{image}')
    images.append(img)

    name=image.split('.')[0]
    names.append(name)


def imageEncodings(images):

    encodings=[]

    print('Encoding.....')

    for image in images:

        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

        encode=fr.face_encodings(image)[0]
        encodings.append(encode)

    return encodings



def markAttendance(name):

    with open('Attendance.csv','r+') as f:

        myDataList = f.readlines()
        
        nameList=[]

        for line in myDataList:

            entry = line.split(',')

            nameList.append(entry[0])

        if name not in nameList:

            current_time=datetime.now()

            status=''

            today8am=datetime.now().replace(hour=8,minute=0,second=0,microsecond=0)   

            dtString=current_time.strftime('%I:%M:%p')

            if current_time<=today8am:

                status='Early'

            else:

                status='Late'

            f.writelines(f'\n{name},{dtString},{status}')



knownEncodings=imageEncodings(images)

print('Encoded successfully')


#webcam
captured=cv2.VideoCapture(0)

frame_color=(250,0,0)

unknown_color=(0,0,255)

while True:

    success,img=captured.read()

    imgSmall=cv2.resize(img,(0,0),None,0.25,0.25)

    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)


    facesLocations= fr.face_locations(imgSmall)

    facesEncodings= fr.face_encodings(imgSmall,facesLocations)


    for encodeFace,faceLoc in zip(facesEncodings,facesLocations):

        matches=fr.compare_faces(knownEncodings,encodeFace)

        faceDis = fr.face_distance(knownEncodings,encodeFace)


        matchindex = np.argmin(faceDis)

        y1,x2,y2,x1=faceLoc

        y1, x2, y2, x1=4*y1,4*x2,4*y2,4*x1


        if matches[matchindex]:

            name=names[matchindex].upper()

            cv2.rectangle(img,(x1,y1),(x2,y2),frame_color,2)

            cv2.rectangle(img,(x1,y2-35),(x2,y2),frame_color,cv2.FILLED)

            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

            markAttendance(name)

        else:

            cv2.rectangle(img,(x1,y1),(x2,y2),unknown_color,2)

            cv2.rectangle(img,(x1,y2-35),(x2,y2),unknown_color,cv2.FILLED)

            cv2.putText(img,'UNKNOWN',(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)



    cv2.imshow('staff',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break
captured.release()

cv2.destroyAllWindows()