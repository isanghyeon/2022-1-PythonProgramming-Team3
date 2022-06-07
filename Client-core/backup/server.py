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


def Send(group, send_queue):
    print('Thread Send Start')
    while True:
        try:
            recv = send_queue.get()
            print(recv)
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


if __name__ == '__main__':
    send_queue = Queue()
    HOST = 'localhost'
    PORT = 9000

    # 소켓 생성
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 바인딩(소켓을 포트에 맵핑) - 호스트 이름, 포트번호 튜플로 전달
    server_sock.bind((HOST, PORT))
    # 클라이언트가 바인드된 포트로 연결을 할 때까지 기다림
    # 연결 요청이 들어오면 (소켓, 주소 정보)로 구성되는 튜플 리턴
    server_sock.listen(10)

    count = 0
    client_group = []

    while True:
        count = count + 1
        print(server_sock)
        conn, addr = server_sock.accept()
        client_group.append(conn)
        print('Connected ' + str(addr))
        if count > 1:
            send_queue.put('Group Changed')
            thread1 = threading.Thread(target=Send, args=(client_group, send_queue,))
            thread1.start()
            pass
        else:
            thread1 = threading.Thread(target=Send, args=(client_group, send_queue,))
            thread1.start()

        thread2 = threading.Thread(target=Recv, args=(conn, count, send_queue,))
        thread2.start()
