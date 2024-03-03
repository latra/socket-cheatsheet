## Sockets Cheat Sheet
### Creación del Socket
>  https://linux.die.net/man/3/socket

Crea y devuelve un descriptor de fichero que apunta a un socket con las características definidas

`AF_INET` 		-> IPv4\
`SOCK_DGRAM` 	-> Connectionless-mode\
`SOCK_STREAM`	-> Connection-mode\
`protocol`		-> 0 = default for type

```c
	int sock = socket(AF_INET, SOCK_DGRAM, 0);	// UDP
	int sock = socket(AF_INTE, SOCK_STREAM, 0);	// TCP
```

```python
    socket: socket.socket = socket.socket(
        family = socket.AF_INET, 
        type = socket.SOCK_DGRAM 
    )
    socket: socket.socket = socket.socket(
        family = socket.AF_INET, 
        type = socket.SOCK_STREAM 
    )
```

### Struct de IPv4

```c
	struct sockaddr_in addr_server;
	memset(&addr_server,0, sizeof(struct sockaddr_in));

	addr_server.sin_family=AF_INET; // IPv4
	addr_server.sin_addr.s_addr=htonl(INADDR_ANY); // 0.0.0.0
	addr_server.sin_port=htons(0); // Random port
```
```python
    addr = ('0.0.0.0', 0)
```
### Bindear el socket
```c
	bind(sock,(struct sockaddr *)&addr_server,sizeof(struct sockaddr_in));
```
```python
    socket.bind(addr)
```
En el caso del cliente, no es estríctamente necesario, ya que al enviar datos a una dirección, si no estaba vinculado, se vinculará en ese momento automáticamente. Pero no hace daño ponerlo igualmente.

## UDP (Connectionless)
### Enviar datos
```c
	char message[1000];
	sendto(sock, message,strlen(message)+1,0,(struct sockaddr*)&addr_cli,sizeof(struct sockaddr_in));
```
```python
    message : bytes = "".encode(encoding="utf-8")
    socket.sendto(message, server_addr)
```
### Recibir datos
```c
	struct sockaddr_in	addr_cli; // NO se inicializa
	int laddr_cli;
	laddr_cli=sizeof(struct sockaddr_in);
	
	char message[1000];
	recvfrom(sock,message,strlen(message),0,(struct sockaddr *)&addr_cli,&laddr_cli);
```
```python
    client_message: bytes
    client_ip: tuple
    client_message, client_ip = socket.recvfrom(1500) 
```

## TCP (Connection)
#TODO
### Conectar
```c
```
```python
```
### Escuchar y Aceptar conexiones
```c
```
```python
```

### Enviar datos
```c
```
```python
```
### Recibir datos
```c
```
```python
```