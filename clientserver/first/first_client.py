import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 5321))
client_sock.sendall(b'Hello, world')
data = client_sock.recv(1024)

print('Received', repr(data))
client_sock.close()