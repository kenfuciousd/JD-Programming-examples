#https://pysnakeblog.blogspot.com/2020/11/python-chat-application-client-server.html
#Start the client second
import socket, sys, time

x = socket.socket()
h_name = input(str("Enter hostname:- "))
port = 8000
x.connect((h_name,port))
print("Server Connected...!")
print("Let the Server Type First")

try:
     while 1:
          incoming_message = x.recv(1024)
          incoming_message = incoming_message.decode()
          print()
          print("Server said: ",incoming_message)
          print()
          message = input(str(">>>> "))
          message = message.encode()
          x.send(message)
except:
     print("Server went OFFLINE")