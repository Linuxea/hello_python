# coding=utf-8

# 参考自
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004374523e495f640612f4b08975398796939ec3c000
import socket

# 创建一个socket:
# 创建Socket时，AF_INET 指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
# SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
# 注(无关信息):端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
s.connect(('www.sina.com.cn', 80))

# TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

print(data)

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

s.close()
