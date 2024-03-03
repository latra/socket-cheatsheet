import socket
import time
import sys
# Abrimos el canal de comunicaciones
client_socket: socket.socket = socket.socket(
    family = socket.AF_INET, 
    type = socket.SOCK_STREAM 
)
if len(sys.argv) < 2:
    print("Introduce el mensaje a enviar: python cliente.py <mensaje>")
    exit(-1)

msg_to_send = ' '.join(sys.argv[1:])

# Vinculamos el canal a la interficie y puerto
client_socket.bind(('0.0.0.0', 0))

# Conectamos el canal al servidor
client_socket.connect(("0.0.0.0", 8000))

# El cliente recibe un mensaje al conectarse
server_response = client_socket.recv(1000)
print(server_response)

# Enviamos petición al servidor
client_socket.send(msg_to_send.encode())

# Esperamos respuesta del servidor
server_response = client_socket.recv(1000)
print(server_response)

print(client_socket.getpeername()[1])

# Cerramos canal de comunicaciones
client_socket.close()