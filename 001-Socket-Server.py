import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is the Internet address family for IPv4.
# SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Ability to reuse port
server_socket.bind((HOST, PORT))
server_socket.listen(5)
# specifies the number of unaccepted connections that the system will allow before refusing new connections

while True:  # Loop for different connections

    print("Start waiting new connection")
    client_socket, addr = server_socket.accept()  # Accept a connection
    print("Connected:", addr)

    while True:  # Loop for different pieces of data

        print("Start waiting new data")
        data = client_socket.recv(1024)
        print("Got data:", data)
        if not data:
            break
        client_socket.send(data.upper())

    print("Close connection")
    client_socket.close()



