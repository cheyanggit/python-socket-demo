# 导入模块
import socketserver
import random


# 练习socket非阻塞模块

class MyServer(socketserver.BaseRequestHandler):
    # 首先执行setup， 之后handle， 之后 finsh方法。
    # 如果handle方法出现了报错，则会跳过handle， setup和finsh方法无论如何都会执行

    def setup(self):
        pass

    def handle(self):
        # 定义连接变量
        conn = self.request
        msg = "hello world!"
        # 消息发送
        conn.send(msg.encode())

        # 进入循环不断接受客户端消息
        while True:
            data = conn.recv(1024)
            print(data.decode())

            # exit 退出
            if data == b'exit':
                break
            conn.send(str(data).encode())
            conn.send(str(random.randint(1, 100)).encode())
        conn.close()

    def finish(self):
        pass


if __name__ == "__main__":
    server = socketserver.TCPServer(("127.0.0.1", 8888), MyServer)
    # 开启异步多线程，等待连接

    server.serve_forever()
