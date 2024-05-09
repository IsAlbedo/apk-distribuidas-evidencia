import socket

def obtener_puertos_en_uso():
    puertos_en_uso = []
    for puerto in range(1, 65536):
        try:
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).bind(('localhost', puerto))
        except OSError:
            puertos_en_uso.append(puerto)
    return puertos_en_uso


puertos = obtener_puertos_en_uso()
print("Puertos en uso:")
for puerto in puertos:
    print(puerto)
