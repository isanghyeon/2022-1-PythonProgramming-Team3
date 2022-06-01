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
    furnished to do so, subject to the following conditio :

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

import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    """
        Flask Config
    """
    SECRET_KEY = os.urandom(16)
    SESSION_COOKIE_NAME = 'BWASP'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:30010/users?charset=utf8"
    SQLALCHEMY_BINDS = {
        "users": "mysql+pymysql://root:1234@localhost:30010/users?charset=utf8",
        "messages": "mysql+pymysql://root:1234@localhost:30020/messages?charset=utf8",
        "chatrooms": "mysql+pymysql://root:1234@localhost:30030/chatrooms?charset=utf8"
    }
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ERROR_404_HELP = False
    SWAGGER_UI_DOC_EXPANSION = 'list'

    def __init__(self):
        pass
        """
        environ_db = os.environ.get("SQLALCHEMY_DATABASE_URI")
        if environ_db:
            self.SQLALCHEMY_BINDS["BWASP"] = environ_db
        """


class Developments_config(Config):
    """
        Flask Config for Development
    """
    DEBUG = True


class Production_config(Config):
    """
        Flask Config for Production
    """
    pass
