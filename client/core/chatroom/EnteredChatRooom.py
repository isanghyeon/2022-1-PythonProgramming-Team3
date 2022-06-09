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

import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.api import ChatRoom


class EnteredChatRooom:
    def __init__(self):
        self.MessageObj = ChatRoom()
        self.ChatUniqKey = None
        self.ResultObject = None

    def AddUser(self, key: str, data: dict):
        self.ResultObject = self.MessageObj.ChatRoomAddUser(key=key, data=data)

        if self.ResultObject["status"] == "200":
            print(f"{self.ResultObject['message']}")
        else:
            print(f"{self.ResultObject['message']}")
