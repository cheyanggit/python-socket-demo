import socket
import random

sk = socket.socket()


# 定义绑定的ｉｐ　和端口

ip_port = ("127.0.0.1", 8888)

#绑定监听
sk.bind(ip_port)

# 最大连接数
sk.listen(5)        # 可以处理五个通信，但是是一个个处理，如果有第六个，就拒绝。


while True:
    # 提示信息
    print("正在进行等待接收数据.......")

    # 接收数据
    conn, address = sk.accept()


    #　定义信息
    msg = "连接成功！"


    # python 3 以上，网络数据的发送   都是ｂｙｔｅ类型，如果发送的数据是ｓｔｒ类型，则需要进行编码。
    # 返回信息
    conn.send(msg.encode())

    #　不断接收客户端发来的消息
    while True:
        # 接收客户端消息
        data = conn.recv(1024)
        # 打印
        print(data.decode())

        # 如果从客户端接收到退出代码，就退出。
        if data==b'exit':
            break

        # 处理客户端数据
        conn.send(data)
        conn.send(str(random.randint(1,1000)).encode())


    # 主动关闭连接
    conn.close()

