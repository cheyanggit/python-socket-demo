import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # ip v4, udp

ip_port = ("127.0.0.1", 8888)

while True:
    msg_input = input("请输入要发送的信息：")


    # 退出条件
    if msg_input == "exit":
        break
    client.sendto(msg_input.encode(), ip_port)     # 在这里定义端口和ｕｒｌ

# 发送关闭信息
client.close()


