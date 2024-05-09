import socket
import threading

HOST = '192.168.137.1' 
PORT = 20000           
SERVER_PORT = 20001    

clients = {}           

def broadcast(message, sender_socket, sender_name):
    """Envía un mensaje a todos los clientes conectados"""
    for client_socket, client_name in clients.items():
        if client_socket != sender_socket:
            try:
                client_socket.send(f'{sender_name}: {message}'.encode())
            except:
                client_socket.close()
                del clients[client_socket]

def handle_client(client_socket, addr):
    """Maneja las conexiones entrantes y recibe los mensajes de los clientes"""
    
    if addr[0] == '192.168.137.195':
        client_name = 'Pan'
    elif addr[0] == '192.168.137.165':
        client_name = 'Beto'
    elif addr[0] == '192.168.137.184':
        client_name = 'Xinol'
    elif addr[0] == '192.168.137.4':
        client_name = 'Fany' 
    elif addr[0] == '192.168.137.138':
        client_name = 'Core'
    elif addr[0] == '192.168.137.71':
        client_name = 'Fierro'
    else:
        client_name = 'Cliente desconocido'

    clients[client_socket] = client_name

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            if data:
                print(f'Recibido de {client_name}: {data.decode()}')
                broadcast(data.decode(), client_socket, client_name)
                # Responder al cliente
                response = b'Mensaje recibido correctamente'
                client_socket.send(response)
        except:
            del clients[client_socket]
            client_socket.close()
            break

def start_server():
    """Inicia el servidor y acepta las conexiones entrantes"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  # Escucha hasta 5 conexiones entrantes

    print(f'Servidor escuchando en {HOST}:{PORT}')

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Conexión entrante de {addr}')
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

def server_communication():
    """Hilo para la comunicación entre el servidor y el usuario"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, SERVER_PORT))
    server_socket.listen(1)

    print(f'Servidor de comunicación escuchando en {HOST}:{SERVER_PORT}')

    connection, _ = server_socket.accept()

    server_name = 'Servidor'
    while True:
        data = connection.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f'Recibido del usuario: {message}')
        broadcast(message, None, server_name)

if __name__ == '__main__':
    start_server()

    # Iniciar el hilo para la comunicación entre el servidor y el usuario
    communication_thread = threading.Thread(target=server_communication)
    communication_thread.start()