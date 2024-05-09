# TCP/IP

import socket
import websockets 

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
puerto = 10000

servidor.bind((host, puerto))

servidor.listen(1)
print("Servidor escuchando en {}:{}".format(host, puerto))

cliente, direccion = servidor.accept()
print("Conexión establecida con {}".format(direccion))

while True:
    mensaje = cliente.recv(1024).decode()
    if not mensaje:
        break
    print("Cliente: {}".format(mensaje))
    servidor_mensaje = input("Servidor: ")
    cliente.send(servidor_mensaje.encode())

cliente.close()

