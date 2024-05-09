import socket

HOST = '192.168.137.1' 
PORT = 20000          

def start_client():
    """Inicia el cliente y se conecta al servidor"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    while True:
        message = input('Escribe tu mensaje: ')
        client_socket.send(message.encode())
        data = client_socket.recv(1024)
        print(f'Recibido: {data.decode()}')

if __name__ == '__main__':
    start_client() 