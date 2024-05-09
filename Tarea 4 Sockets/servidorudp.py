import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print("Servidor escuchando en {}:{}...".format(SERVER_IP, SERVER_PORT))

while True:
    message, client_address = server_socket.recvfrom(2048)
    print("Mensaje recibido: '{}' desde {}".format(message.decode(), client_address))
