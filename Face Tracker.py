'''
curently trying to send the data to Arduino and have the motors move. 
'''
import cv2
import numpy as np
import time
import serial
#window demensions
window_list=[150]
width,height = 300 , 240
prev_error =0
offset_error = [-4,4]
#arduino = serial.Serial(port = 'COM5',baudrate = '9600' )


def detect_face(img):
    face_Cascade = cv2.CascadeClassifier("face_detection/haarcascade_frontalface_default.xml")
    gary_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_Cascade.detectMultiScale(gary_img,1.2,5)

    face_list=[]
    face_Area=[]

    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w ,y+h),(255,0,0),2)
        center_x = x + w // 2
        center_y = y + h // 2
        img_area = w + h
        img_cent = width // 2
        imgy_center = height // 2
        cv2.circle(img,(center_x,center_y),3,(0,0,255),cv2.FILLED)
        cv2.circle(img,(img_cent,imgy_center),2,(0,0,255),cv2.FILLED)
        face_list.append([center_x,center_y])
        face_Area.append(img_area)
        break


        # we want to get the closes face
    if len (face_Area) != 0:
        i = face_Area.index(max(face_Area))
        return img, [face_list[i],face_Area[i]]
    # if there is no face then we want to return nothing
    else:
        return img, [[0,0],0] # return 0 for x, y and for area

def tracker(info,w,h):  
    '''
    # x & y postion of the circle on face
    # x would be indicate the face postion
    # w is the width of the img which is divided by
    
    change the position value to an angle to pass to the motor
    '''
    x,y = info[0] 
    X_angle =round( x / (width/180))
    Y_angle =round( y / (height/180))
    datasend = "X:{0},Y:{1}".format(X_angle,Y_angle)
    #datasend_byte = bytes(datasend, 'utf-8')
    #arduino.write(datasend_byte)
    #time.sleep(.15)
    return datasend #datasend_byte


cap = cv2.VideoCapture(0)
while True:
    _,img = cap.read()
    img = cv2.resize(img,(width,height))
    img,info = detect_face(img)
    #print('center', info[0])
    tracker(info,width,height)  # print(tracker(info,width,height))

    cv2.imshow('Output',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
