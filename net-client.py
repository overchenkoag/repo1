import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.1'
port = 80
s.connect((host, port))
s.send(b'GET / HTTP/1.1\n\n')
data = s.recv(1000000)
print ('received', data, len(data), 'bytes')
s.close()