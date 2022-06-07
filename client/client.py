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

import time, sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.messages import (
    CreateMessage, GetAllMessage, GetUserMessage
)

while True:
    Result = CreateMessage.CreateMessage()
    Result.AddMessage(data={
        "UserUniqKey": "b3d39b9aedbd4a3a6eb93c192890c1e47b11f209fe42f1e2eefeabdf2ef90a1c",
        "ChatUniqKey": "894906d45a8ddb9ee4b611a019f7bcef6c1dca7ed0b13bcb922dfbd87528c45c",
        "UserName": "isanghyeon",
        "MessageData": "heheheheheheheheheheheheh"
    })

    time.sleep(0.5)
