SERVER SIDE CODE:
import socket
import numpy as np
import cv2
cap=cv2.VideoCapture(0) #To connect my webcam with this python code.
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #For mentioning that we are using the IPv4 address and TCP protocol
ip="192.168.56.1" #IP of my server
port=1222   #port number 
s.bind((ip,port)) #binding the IP and port number.
s.listen()  #To keep it in a holding and accepting the connection, mode
session,add=s.accept() # Accepting the connection from the client we want 

while True:
    data=session.recv(90456)   # To receive the data and specifying the maximum byte size permissible for transfer. 
    arg=np.fromstring(data,dtype=np.uint8) #To convert the bytes into 1-D array format
    photo=cv2.imdecode(arg,cv2.IMREAD_COLOR) #Converting 1-D array to  numpy 3-D image 
    ret,frame=cap.read()    #Capturing the image from the local webcam
    fi=cv2.resize(frame,(200,150),3) #resizing it
    if type(photo) is type(None): #if no photo found in front of webcam
        pass
    else:
        photo[:150,:200]=fi  # slice the video received and then swapping the selected part with video on local webcam to give a proper feel of the video chat app.
        cv2.imshow('server',photo) #finally showing the photo
        if cv2.waitKey(1)==13:  #will exit the loop when “Enter” key is pressed
            break
    
    videosend=cv2.imencode('.jpg',frame)[1].tobytes()  #converting the photo into bytes format to send it to the client.
    session.sendall(videosend)  #To send images from our local webcam

cv2.destroyAllWindows()  #after the chat closing the video window.
cap.release() #disconnecting the webcam 
