## Sockets Cheat Sheet
### Creación del Socket
>  https://linux.die.net/man/3/socket

Crea y devuelve un descriptor del socket que apunta a un socket con las características definidas.

Estos son las constantes más habituales:

`AF_INET` 		-> IPv4\
`SOCK_DGRAM` 	-> Connectionless-mode\
`SOCK_STREAM`	-> Connection-mode\

**C**
```c
       int socket(int domain, int type, int protocol);
```
```c
	int sock = socket(AF_INET, SOCK_DGRAM, 0);	// UDP
	int sock = socket(AF_INTE, SOCK_STREAM, 0);	// TCP
```
Indicando 0 como protocolo, asignará automáticamente el protocolo en función del tipo de socket (UDP en caso de ser un socket de Datagramas, TCP en caso de ser un socket de STREAM)

**Python3**
```python
class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
```
```python
    socket: socket.socket = socket.socket(
        family = socket.AF_INET, 
        type = socket.SOCK_DGRAM            # UDP
    )
    socket: socket.socket = socket.socket(
        family = socket.AF_INET, 
        type = socket.SOCK_STREAM           # TCP
    )
```


### Struct de IPv4
La información sobre las direcciones IPv4 a las que nos conectamos se almacena en estructuras donde definiremos la dirección y el puerto.
- Podemos usar `0.0.0.0` como IP para indicar 'cualquier IP' (o `INADDR_ANY`)
- Podemos usar `0` en lugar de especificar un puerto en caso que queramos que se utilice uno aleatorio (útil, por ejemplo, al definir que puerto utilizará el cliente).

**C**
```c
	struct sockaddr_in addr_server;
	memset(&addr_server,0, sizeof(struct sockaddr_in));

	addr_server.sin_family=AF_INET; // IPv4
	addr_server.sin_addr.s_addr=htonl(INADDR_ANY); // 0.0.0.0
	addr_server.sin_port=htons(0); // Random port
```
**Python3**
```python
    addr = ('0.0.0.0', 0)
```
### Vincular el socket
Una vez creado el socket, debemos vincularlo a la interficie de nuestro equipo, indicando tanto la IP de la interficie como el puerto. 

**C**
```c
	bind(sock,(struct sockaddr *)&addr_server,sizeof(struct sockaddr_in));
```
**Python3**
```python
    socket.bind(addr)
```
En el caso del cliente, no es estríctamente necesario, ya que al enviar datos a una dirección, si no estaba vinculado, se vinculará en ese momento automáticamente. Pero no hace daño ponerlo igualmente.

## UDP (Connectionless)

### Enviar datos

**C**
```c
	char message[1000];
	sendto(sock, message,strlen(message)+1,0,(struct sockaddr*)&addr_cli,sizeof(struct sockaddr_in));
```
**Python3**
```python
    message : bytes = "".encode(encoding="utf-8") # o encoding="ascii", para evitar complicarnos la vida al gestionarlo en C.
    socket.sendto(message, server_addr)
```
### Recibir datos

**C**
```c
	struct sockaddr_in	addr_cli; // NO se inicializa
	int laddr_cli;
	laddr_cli=sizeof(struct sockaddr_in);
	
	char message[1000];
	recvfrom(sock,message,strlen(message),0,(struct sockaddr *)&addr_cli,&laddr_cli);
```
**Python3**
```python
    client_message: bytes
    client_ip: tuple
    client_message, client_ip = socket.recvfrom(1500) 
```

## TCP (Connection)
#TODO
### Conectar
Realizado por el lado del cliente hacia la IP y puerto utilizada por el servidor
**C**
```c
```
**Python3**
```python
socket.connect(("0.0.0.0", 8000))
```
### Escuchar y Aceptar conexiones
Realizado por el servidor: coloca la interficie de conexión (_el socket_) en modo escucha, y acepta las peticiones en espera.
**C**
```c
```
**Python3**
```python
socket.listen(1)
connected_socket, client_info = server_socket.accept()
```

### Enviar datos

**C**
```c
```
**Python3**
```python
msg_to_send : bytes = "message".encode()
socket.send(msg_to_send)
```
### Recibir datos

**C**
```c
```
**Python3**
```python
recv_buffer : bytes = socket.recv(1000)
```
