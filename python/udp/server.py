

import socket

# Abrimos canal de comunicación
server_socket: socket.socket = socket.socket(
    family = socket.AF_INET, 
    type = socket.SOCK_DGRAM 
)

# Vinculamos canal a interficie y puerto
server_socket.bind(('0.0.0.0', 8000))

while True:
    # Recibimos petición
    message, client_addr = server_socket.recvfrom(1000)

    # Tratamos y respondemos la petición 
    print(message)
    server_socket.sendto(b"has dicho " + message, client_addr)