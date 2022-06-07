# -*- coding: utf-8 -*-

"""
    Python Programming Project - Team 3
    ~~~~~~~~~~~~~~
    A brief description goes here.
    :copyright: (c) 2022 by isanghyeon.

    The MIT License
    Copyright (c) 2022 isanghyeon all rights reserved.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""
import socket
import threading
from queue import Queue


class AppSocketMiddleware:
    def __init__(self):
        self.Host = ''
        self.Port = 45999

        self.socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketSendQueue = Queue()

        self.count = 0
        self.socketEnteredGroup = []

        self.ReceviedData = None
        self.SendData = None
        self.Message = None

    def SocketInitialized(self):
        self.socketServer.bind((self.Host, self.Port))
        self.socketServer.listen(10)

    def SocketSender(self):
        while True:
            try:
                self.ReceviedData = self.socketSendQueue.get()

                if self.ReceviedData == "Group Changed":
                    print("Group Changed")
                    break

                for ConnObj in self.socketEnteredGroup:
                    self.Message = 'Client' + str(self.ReceviedData[2]) + ' >> ' + str(self.ReceviedData[0])

                    if self.ReceviedData[1] != ConnObj:
                        ConnObj.send(bytes(self.Message.encode()))
                    else:
                        pass
            except:
                pass

    def socketReceiver(self):
        while True:
            pass


def Send(group, send_queue):
    print('Thread Send Start')
    while True:
        try:

            recv = send_queue.get()
            if recv == 'Group Changed':
                print('Group Changed')
                break

            for conn in group:
                msg = 'Client' + str(recv[2]) + ' >> ' + str(recv[0])
                if recv[1] != conn:
                    conn.send(bytes(msg.encode()))
                else:
                    pass
        except:
            pass


def Recv(conn, count, send_queue):
    print('Thread Recv' + str(count) + ' Start')
    while True:
        data = conn.recv(1024).decode()
        send_queue.put([data, conn, count])


def Recv(conn, count, send_queue):
    print('Thread Recv' + str(count) + ' Start')
    while True:
        data = conn.recv(1024).decode()
        send_queue.put([data, conn, count])


if __name__ == '__main__':
    send_queue = Queue()
    HOST = ''
    PORT = 45100
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((HOST, PORT))
    server_sock.listen(10)
    count = 0
    group = []

    while True:
        count = count + 1
        conn, addr = server_sock.accept()
        group.append(conn)
        print('Connected ' + str(addr))

        if count > 1:
            send_queue.put('Group Changed')
            thread1 = threading.Thread(target=Send, args=(group, send_queue,))
            thread1.start()
            pass
        else:
            thread1 = threading.Thread(target=Send, args=(group, send_queue,))
            thread1.start()

        thread2 = threading.Thread(target=Recv, args=(conn, count, send_queue,))
        thread2.start()
