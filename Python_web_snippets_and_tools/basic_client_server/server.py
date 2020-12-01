#https://pysnakeblog.blogspot.com/2020/11/python-chat-application-client-server.html
#Start the server first
import socket, sys, time

x = socket.socket()
h_name = socket.gethostname()
print("Your host name is : ", h_name)
port = 8000
x.bind((h_name,port))
x.listen(1)
connection, address = x.accept()
print("Server is ONLINE ! ! !")

try:
     while 1:
          display_mess = input(str(">> "))
          display_mess = display_mess.encode()
          connection.send(display_mess)
          in_message = connection.recv(1024)
          in_message = in_message.decode()
          print()
          print("Client said: ",in_message)
          print()
except:
     print("Client went OFFLINE")