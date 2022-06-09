#      -*- coding: utf-8 -*-
#
#
#      Python Programming Project - Team 3
#      ~~~~~~~~~~~~~~
#      A brief description goes here.
#      :copyright: (c) 2022 by isanghyeon.
#
#      The MIT License
#      Copyright (c) 2022 isanghyeon all rights reserved.
#
#      Permission is hereby granted, free of charge, to any person obtaining a copy
#      of this software and associated documentation files (the "Software"), to deal
#      in the Software without restriction, including without limitation the rights
#      to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#      copies of the Software, and to permit persons to whom the Software is
#      furnished to do so, subject to the following conditions:
#
#      The above copyright notice and this permission notice shall be included in
#      all copies or substantial portions of the Software.
#
#      THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#      IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#      FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#      AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#      LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#      OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#      THE SOFTWARE.
#

from api import ChatRoom
from api import User

import json

id = "isanghyeon"
pw = "isanghyeon"

a = User().UserRegister(data={
    "UserName": id,
    "UserAccountPW": pw
})
print(a)
# 사용자 회원가입 완료~~

b = User().UserSignIn(uname=id, upw=pw)
c = b.get('data')
userkey = c.get('UserUniqKey')  # 사용자 키
# 사용자 키 받기 완료~~

d = ChatRoom().ChatRoomAdd(data={  # 한명 있는 채팅방 완성?
    "ParticipantUserName": id,
    "ParticipantUserUniqKey": userkey
})

print(d)
