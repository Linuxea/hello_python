
''' a tcp socket server '''

from socket import *
import time

HOST = '127.0.0.1'
PORT = 9090
BUFSIZE = 1024

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

while True:

    try:

        client_socket, addr = server_socket.accept()

        while True:
            try:
                data = client_socket.recv(BUFSIZE)
                if not data:
                    break
                re = bytes("%si have receive:%s" % (time.ctime(), data), encoding = "utf8") 
                client_socket.send(re)
            except Exception as e:
                print("%s" % e)
                client_socket.close()
                time.sleep(5)

    except Exception as e :
        print("%s" % e)
        server_socket.close()
        time.sleep(5)