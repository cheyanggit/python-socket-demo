import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 使用ｉｐｖ４，　ｕｄｐ

ip_port = ("127.0.0.1", 8888)

# 绑定监听
sk.bind(ip_port)

# 不断循环接收数据
while True:
    # 接收从客户端发送的数据
    data = sk.recv(1024)
    # 打印数据
    print(data.decode())


