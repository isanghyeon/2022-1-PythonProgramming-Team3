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


def Send(client_sock):
    while True:
        send_data = bytes(input().encode())
        client_sock.send(send_data + b"key=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


def Recv(client_sock):
    while True:
        recv_data = client_sock.recv(1024).decode()
        print(recv_data)

if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Host = '220.69.200.173'
    Port = 45100
    try:
        client_sock.connect((Host, Port))
        print('Connecting to ', Host, Port)

        thread1 = threading.Thread(target=Send, args=(client_sock,))
        thread1.start()

        thread2 = threading.Thread(target=Recv, args=(client_sock,))
        thread2.start()
    except Exception as e:
        print(e)
        thread1.join()
        thread2.join()
        client_sock.close()
