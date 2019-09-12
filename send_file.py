import socket

sk = socket.socket()

# 定义IP和端口
ip_port = ('127.0.0.1', 9999)

sk.connect(ip_port)

# 文件上传和打开文件
with open('a.txt', 'rb') as f:
    for i in f:  # 文件打开就是byte类型，不需要字符串转bytes
        sk.send(i)
        # 等待接收完成标记
        data = sk.recv(1024)
        # 判断服务器是否真正接收完成
        if data != b'success':
            break

# 给服务器端发送结束信号
sk.send('quit'.encode())

