import socket
import threading

HOST = socket.gethostbyname(socket.gethostname()) # get the ip address of PC
PORT = 5050

ADDRESS = (HOST, PORT)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind(ADDRESS)


socket_list = []

def client_handler(client_socket, address):
  while True:
    data = client_socket.recv(64)
    if len(data) == 0:
      break
    print(data.decode('utf-8'))
    for socket_item in socket_list:
      if socket_item != client_socket:
        socket_item.send(data)


while True:
  socket.listen()

  conn, addr = socket.accept()
  print(f"Connected by {addr}")
  socket_list.append(conn)
  t = threading.Thread(target=client_handler, args = [conn, addr])
  t.start()

  

