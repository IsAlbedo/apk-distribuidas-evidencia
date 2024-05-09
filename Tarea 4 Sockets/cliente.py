import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
puerto = 10000

cliente.connect((host, puerto))

while True:
    cliente_mensaje = input("Cliente: ")
    cliente.send(cliente_mensaje.encode())
    mensaje = cliente.recv(1024).decode()
    print("Servidor: {}".format(mensaje))

cliente.close()
