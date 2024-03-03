"""
Ejemplo MUY básico de servidor con socket TCP (orientado a conexión) en Python.

Al aceptar una conexión, envia un "Hola, te has conectado" al cliente.
Cuando recibe el mensaje del cliente, devuelve el mensaje que ha enviado el cliente.
"""
__author__ = "Paula 'Latra' Gallucci"
__email__ = "paula.gallucci@udl.cat"

import socket

# Abrimos canal de comunicaciones
server_socket: socket.socket = socket.socket(
    family = socket.AF_INET, 
    type = socket.SOCK_STREAM 
)

# Vinculamos canal a interficie y puerto
server_socket.bind(('0.0.0.0', 8000))

#Esperamos conexiones al servidor
server_socket.listen(4)
while True:
    # Aceptamos una conexión al servidor
    client_connected_socket, client_info = server_socket.accept()
    client_connected_socket.send(b"Hola, te has conectado")

    #Recibimos la petición
    client_message = client_connected_socket.recv(1000)
    client_connected_socket.send(b"has dicho "  + client_message)

    #Tratamos la conexión
    print(client_message)
    print(client_connected_socket.getpeername()[0])
    print(client_connected_socket.getpeername()[1])

    # Cerramos canal de comunicación
    client_connected_socket.close()

# Cerramos canal de comunicación
server_socket.close()