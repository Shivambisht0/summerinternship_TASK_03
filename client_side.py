# CLIENT SIDE CODE:-
import socket
import numpy
import cv2
cap=cv2.VideoCapture('https://192.168.43.1:8080/video') #connecting the camera of my mobile by using it’s IP.
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.56.1",1222)) #connecting to the server socket.
#AND THEN ALL THE SAME PROCESS AS WE PERFORMED FOR SERVER.

while True:
    ret,photo=cap.read()
    cimg=cv2.resize(photo,(540,430))
    simg=cv2.imencode(".jpg",cimg)[1].tobytes()
    s.sendall(simg)
    
    data=s.recv(90456)
    arg=numpy.fromstring(data,numpy.uint8)
    img=cv2.imdecode(arg,cv2.IMREAD_COLOR)
    fimg=cv2.resize(photo,(200,150),3)
    if type(img) is type(None):
        pass
    else:
        img[:150,:200]=fimg
        cv2.imshow('clien',img)
        if cv2.waitKey(1)==13:
            break
cv2.destroyAllWindows()
cap.release()
