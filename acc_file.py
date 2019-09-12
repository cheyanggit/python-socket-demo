import socket

sk = socket.socket()

ip_port = ('127.0.0.1', 9999)

sk.bind(ip_port)

sk.listen(5)

# 进入循环接收数据
while True:
    conn, addtess = sk.accept()
    while True:
        # 一直使用当前连接进行数据接收，直到结束。
        # 打开文件等待数据写入
        with open ("acc_a.txt", 'ab') as f:
            data = conn.recv(1024)
            if data == b'quit':
                break
            f.write(data)
        # 接收完成标志
        conn.send('success'.encode())
    print("文件接受完成。")
# 关闭连接
sk.close()