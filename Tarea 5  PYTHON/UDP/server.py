# Servidor
import socket

IP = "192.168.137.1"  
PUERTO = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PUERTO))

print("Servidor iniciado")

while True:
    data, addr = sock.recvfrom(1024)
    print("Dirección cliente: ", addr)
    print("Recibido: ", data.decode())
    
    msg = input("Mensaje a enviar: ")
    sock.sendto(msg.encode(), addr) 