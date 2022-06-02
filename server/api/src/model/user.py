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

from . import UserDB as UserModel


class user(UserModel.Model):
    __tablename__ = 'user'
    __bind_key__ = 'users'

    id = UserModel.Column(UserModel.INTEGER, primary_key=True, autoincrement=True)
    UserUniqKey = UserModel.Column(UserModel.VARCHAR(100), unique=True, nullable=True)
    UserName = UserModel.Column(UserModel.VARCHAR(50), unique=True, nullable=True)
    UserAccountPW = UserModel.Column(UserModel.VARCHAR(88), nullable=False)
    LastLoginTimestamp = UserModel.Column(UserModel.TIMESTAMP, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    CreateTimestamp = UserModel.Column(UserModel.TIMESTAMP, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __init__(self, UserUniqKey, UserName, UserAccountPW, LastLoginTimestamp, CreateTimestamp, **kwargs):
        self.UserUniqKey = UserUniqKey
        self.UserName = UserName
        self.UserAccountPW = UserAccountPW
        self.LastLoginTimestamp = LastLoginTimestamp
        self.CreateTimestamp = CreateTimestamp

    def __repr__(self):
        return f"<user('{self.UserUniqKey}', '{self.UserName}', '{self.UserAccountPW}', '{self.LastLoginTimestamp}', '{self.CreateTimestamp}')>"
