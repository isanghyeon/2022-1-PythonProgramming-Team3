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

import sys, os, datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from . import MsgDB as MessageModel


class message(MessageModel.Model):
    __tablename__ = 'message'
    __bind_key__ = 'messages'

    id = MessageModel.Column(MessageModel.INTEGER, primary_key=True, autoincrement=True)
    UserUniqKey = MessageModel.Column(MessageModel.VARCHAR(100), nullable=False)
    ChatUniqKey = MessageModel.Column(MessageModel.VARCHAR(100), nullable=False)
    UserName = MessageModel.Column(MessageModel.VARCHAR(50), nullable=False)
    MessageType = MessageModel.Column(MessageModel.BOOLEAN, default=0, nullable=True)
    MessageData = MessageModel.Column(MessageModel.TEXT, default=0, nullable=True)
    MediaDataPath = MessageModel.Column(MessageModel.TEXT, default=0, nullable=True)
    MessageTimestamp = MessageModel.Column(MessageModel.TIMESTAMP, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __init__(self, UserUniqKey, ChatUniqKey, UserName, MessageType, MessageData, MediaDataPath, MessageTimestamp, **kwargs):
        self.UserUniqKey = UserUniqKey
        self.ChatUniqKey = ChatUniqKey
        self.UserName = UserName
        self.MessageType = MessageType
        self.MessageData = MessageData
        self.MediaDataPath = MediaDataPath
        self.MessageTimestamp = MessageTimestamp

    def __repr__(self):
        return f"<user('{self.UserUniqKey}', '{self.ChatUniqKey}', '{self.UserName}', '{self.MessageType}', '{self.MessageData}', '{self.MediaDataPath}', '{self.MessageTimestamp}')>"
