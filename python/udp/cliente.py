"""
Ejemplo MUY básico de cliente con socket UDP (no-orientado a conexión) en Python.

Envía al servidor el mensaje indicado por parámetro, y recibe un mensaje de respuesta del servidor
"""
__author__ = "Paula 'Latra' Gallucci"
__email__ = "paula.gallucci@udl.cat"


import socket
import sys

SERVER_ADDR = ("localhost", 8000)

if len(sys.argv) < 2:
    print("Introduce el mensaje a enviar: python cliente.py <mensaje>")
    exit(-1)

msg_to_send = ' '.join(sys.argv[1:])

# Abrimos el canal de comunicaciones
client_socket: socket.socket = socket.socket(
    family = socket.AF_INET, 
    type = socket.SOCK_DGRAM 
)

# Vinculamos el canal a interficie y puerto
client_socket.bind(('0.0.0.0', 0))

# Enviamos petición al servidor
client_socket.sendto(msg_to_send.encode(encoding="utf-8"), SERVER_ADDR)

# Esperamos respuesta del servidor
server_response, server_ip = client_socket.recvfrom(1500)
print("Recibido desde el servidor {}: {}".format(server_ip, server_response.decode()))

# Cerramos canal de comunicaciones
client_socket.close()