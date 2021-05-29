import socket
import threading
import select

HOST = socket.gethostbyname(socket.gethostname()) # get the ip address of PC
PORT = 5050

ADDRESS = (HOST, PORT)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect(ADDRESS)

def client_handler():
  name = input("What is your name? ")
  # socket.send(name.encode('utf-8'))
  while True:
    msg = input(name + "> ")
    msg = "\n" + name + "> " + msg
    socket.send(msg.encode('utf-8'))
    

def receive_data():
  while True:
    data = socket.recv(64)
    print(data.decode('utf-8'))

t1 = threading.Thread(target=client_handler)
t1.start()
t2 = threading.Thread(target=receive_data)
t2.start()


