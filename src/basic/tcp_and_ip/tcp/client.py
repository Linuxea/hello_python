# coding=utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))
print(s.recv(1024).decode('utf-8'))
for x in [b'linuxea', b'bonnie', b'little red']:
    s.send(x)
    print(s.recv(1024).decode('utf-8'))
s.send(b"exit")
s.close()
