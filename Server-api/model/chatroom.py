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

from . import ChatDB as ChattingModel


class chatroom(ChattingModel.Model):
    __tablename__ = 'chatroom'
    __bind_key__ = 'chatrooms'

    id = ChattingModel.Column(ChattingModel.INTEGER, primary_key=True, autoincrement=True)
    ChatUniqKey = ChattingModel.Column(ChattingModel.VARCHAR(100), nullable=False)
    ParticipantUName = ChattingModel.Column(ChattingModel.TEXT, default="none", nullable=False)
    ParticipantUniqKey = ChattingModel.Column(ChattingModel.TEXT, default="none", nullable=False)
    NewUserParicipatedTimestamp = ChattingModel.Column(ChattingModel.DATETIME, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    LastChatTimestamp = ChattingModel.Column(ChattingModel.DATETIME, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    CreateTimestamp = ChattingModel.Column(ChattingModel.DATETIME, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __init__(self, ChatUniqKey, ParticipantUName, ParticipantUniqKey, NewUserParicipatedTimestamp, LastChatTimestamp, CreateTimestamp, **kwargs):
        self.ChatUniqKey = ChatUniqKey
        self.ParticipantUName = ParticipantUName
        self.ParticipantUniqKey = ParticipantUniqKey
        self.NewUserParicipatedTimestamp = NewUserParicipatedTimestamp
        self.LastChatTimestamp = LastChatTimestamp
        self.CreateTimestamp = CreateTimestamp

    def __repr__(self):
        return f"<user('{self.ChatUniqKey}', '{self.ParticipantUName}', '{self.ParticipantUniqKey}', '{self.NewUserParicipatedTimestamp}', '{self.LastChatTimestamp}', '{self.CreateTimestamp}')>"
