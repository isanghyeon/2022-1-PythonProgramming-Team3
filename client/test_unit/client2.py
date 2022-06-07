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
        try:
            send_data = bytes(input().encode())
            client_sock.send(send_data + b"key=cccccccccccccccccccccccccccccccccccc")

        except:
            client_sock.close()
            break


def Recv(client_sock):
    while True:
        try:
            recv_data = client_sock.recv(1024).decode()
            print(recv_data)
        except:
            client_sock.close()
            break



if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Host = 'localhost'
    Port = 9000

    client_sock.connect((Host, Port))
    print('Connecting to ', Host, Port)

    thread1 = threading.Thread(target=Send, args=(client_sock,))
    thread1.start()

    thread2 = threading.Thread(target=Recv, args=(client_sock,))
    thread2.start()

    thread1.join(10)
    thread2.join(10)
    client_sock.close()
