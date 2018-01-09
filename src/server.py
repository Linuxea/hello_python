
''' a tcp socket server '''

from socket import *
import time

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(90)

while True:

    try:

        print("server socket blocking...")

        client_socket, addr = server_socket.accept()

        print("client_socket: %s" % (client_socket))

        while True:
            try:
                data = client_socket.recv(BUFSIZE)
                print("%s data:" %(data))
                if not data:
                    break
                # re = bytes("%si have receive:%s" % (time.ctime(), data), encoding = "utf8") 
                re = bytes('ok', encoding = "utf8")
                print("返回消息预览:%s" %(re))
                client_socket.send(re)
            except Exception as e:
                print("%s" % e)
                time.sleep(10)
            finally:
                client_socket.close()

    except Exception as e :
        print("%s" % e)
        server_socket.close()
        time.sleep(5)