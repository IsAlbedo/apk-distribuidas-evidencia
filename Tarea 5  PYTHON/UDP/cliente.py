# Cliente

import socket

SERVER_IP = "192.168.137.1"
SERVER_PORT = 5000 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Mensaje a enviar: ") 
    sock.sendto(msg.encode(), (SERVER_IP, SERVER_PORT))
    
    data, addr = sock.recvfrom(1024)
    print("Recibido: ", data.decode())