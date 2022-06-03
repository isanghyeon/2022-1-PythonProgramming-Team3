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
from tkinter import messagebox

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.api import User


class AccountValidator:
    def __init__(self):
        pass


class Account:
    def __init__(self):
        self.UserObj = User()
        self.UserName = None
        self.UserPassword = None
        self.ResultObject = None

    def SignIn(self, UserName, UserPassword):
        self.ResultObject = self.UserObj.UserSignIn(uname=UserName, upw=UserPassword)

        if self.ResultObject["status"] == "200":
            messagebox.showinfo("Success", "Sign in successful")
            return True
        else:
            messagebox.showinfo("Success", "Sign in failed")
            return False

        # TODO: if status code is 400, response data checking

    def SignUp(self, UserName, UserPassword):
        self.ResultObject = self.UserObj.UserRegister(data={
            "UserName": UserName,
            "UserAccountPW": UserPassword
        })

        if self.ResultObject["status"] == "201":
            messagebox.showinfo("Success", "Register successful")
        else:
            messagebox.showerror("Error", "Register Failed")
