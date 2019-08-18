import socket

client = socket.socket()


# 访问服务器端口
ip_port = ("127.0.0.1", 8888)

client.connect(ip_port)




# 定义一个循环，不断地发送消息
while True:
    # 接收数据
    data = client.recv(1024)
    print(data.decode())

    # 输入发送消息
    msg_input = input("请输入发送消息:")
    client.send(msg_input.encode())

    if msg_input == "exit":
        break


    data = client.recv(1024)  # 每次接收１０２４字节
    print(data.decode())





