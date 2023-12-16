import socket
from select import select

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is the Internet address family for IPv4.
# SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Ability to reuse port
server_socket.bind((HOST, PORT))
server_socket.listen(5)
# specifies the number of unaccepted connections that the system will allow before refusing new connections


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print("Connected:", addr)
    to_monitor.append(client_socket)


def exchange_messages(client_socket):
    data = client_socket.recv(4096)
    print("Got data:", data)
    if data:
        client_socket.send(data.upper())
    else:
        client_socket.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])  # read, write, errors
        for socket in ready_to_read:
            if socket is server_socket:
                accept_connection(socket)
            else:
                exchange_messages(socket)

# ---------------------------------------------


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()


# TRY: nc localhost 65432
