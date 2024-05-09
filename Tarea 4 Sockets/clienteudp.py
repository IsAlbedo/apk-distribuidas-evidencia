import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Ingrese el mensaje a enviar: ")
    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
