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

# # import modules
#
# from tkinter import *
# import os
#
#
# # Designing window for registration
#
# def register():
#     global register_screen
#     register_screen = Toplevel(main_screen)
#     register_screen.title("Register")
#     register_screen.geometry("300x250")
#
#     global username
#     global password
#     global username_entry
#     global password_entry
#     username = StringVar()
#     password = StringVar()
#
#     Label(register_screen, text="Please enter details below", bg="blue").pack()
#     Label(register_screen, text="").pack()
#     username_lable = Label(register_screen, text="Username * ")
#     username_lable.pack()
#     username_entry = Entry(register_screen, textvariable=username)
#     username_entry.pack()
#     password_lable = Label(register_screen, text="Password * ")
#     password_lable.pack()
#     password_entry = Entry(register_screen, textvariable=password, show='*')
#     password_entry.pack()
#     Label(register_screen, text="").pack()
#     Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()
#
#
# # Designing window for login
#
# def login():
#     global login_screen
#     login_screen = Toplevel(main_screen)
#     login_screen.title("Login")
#     login_screen.geometry("300x250")
#     Label(login_screen, text="Please enter details below to login").pack()
#     Label(login_screen, text="").pack()
#
#     global username_verify
#     global password_verify
#
#     username_verify = StringVar()
#     password_verify = StringVar()
#
#     global username_login_entry
#     global password_login_entry
#
#     Label(login_screen, text="Username * ").pack()
#     username_login_entry = Entry(login_screen, textvariable=username_verify)
#     username_login_entry.pack()
#     Label(login_screen, text="").pack()
#     Label(login_screen, text="Password * ").pack()
#     password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
#     password_login_entry.pack()
#     Label(login_screen, text="").pack()
#     Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
#
#
# # Implementing event on register button
#
# def register_user():
#     username_info = username.get()
#     password_info = password.get()
#
#     file = open(username_info, "w")
#     file.write(username_info + "\n")
#     file.write(password_info)
#     file.close()
#
#     username_entry.delete(0, END)
#     password_entry.delete(0, END)
#
#     Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
#
#
# # Implementing event on login button
#
# def login_verify():
#     username1 = username_verify.get()
#     password1 = password_verify.get()
#     username_login_entry.delete(0, END)
#     password_login_entry.delete(0, END)
#
#     list_of_files = os.listdir()
#     if username1 in list_of_files:
#         file1 = open(username1, "r")
#         verify = file1.read().splitlines()
#         if password1 in verify:
#             login_sucess()
#
#         else:
#             password_not_recognised()
#
#     else:
#         user_not_found()
#
#
# # Designing popup for login success
#
# def login_sucess():
#     global login_success_screen
#     login_success_screen = Toplevel(login_screen)
#     login_success_screen.title("Success")
#     login_success_screen.geometry("150x100")
#     Label(login_success_screen, text="Login Success").pack()
#     Button(login_success_screen, text="OK", command=delete_login_success).pack()
#
#
# # Designing popup for login invalid password
#
# def password_not_recognised():
#     global password_not_recog_screen
#     password_not_recog_screen = Toplevel(login_screen)
#     password_not_recog_screen.title("Success")
#     password_not_recog_screen.geometry("150x100")
#     Label(password_not_recog_screen, text="Invalid Password ").pack()
#     Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
#
#
# # Designing popup for user not found
#
# def user_not_found():
#     global user_not_found_screen
#     user_not_found_screen = Toplevel(login_screen)
#     user_not_found_screen.title("Success")
#     user_not_found_screen.geometry("150x100")
#     Label(user_not_found_screen, text="User Not Found").pack()
#     Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
#
#
# # Deleting popups
#
# def delete_login_success():
#     login_success_screen.destroy()
#
#
# def delete_password_not_recognised():
#     password_not_recog_screen.destroy()
#
#
# def delete_user_not_found_screen():
#     user_not_found_screen.destroy()
#
#
# # Designing Main(first) window
#
# def main_account_screen():
#     global main_screen
#     main_screen = Tk()
#     main_screen.geometry("300x250")
#     main_screen.title("Account Login")
#     Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
#     Label(text="").pack()
#     Button(text="Login", height="2", width="30", command=login).pack()
#     Label(text="").pack()
#     Button(text="Register", height="2", width="30", command=register).pack()
#
#     main_screen.mainloop()
#
#
# main_account_screen()
#
# try:
#     import Tkinter as tk
# except:
#     import tkinter as tk
#
#
# class SampleApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self._frame = None
#         self.switch_frame(StartPage)
#
#     def switch_frame(self, frame_class):
#         new_frame = frame_class(self)
#         if self._frame is not None:
#             self._frame.destroy()
#         self._frame = new_frame
#         self._frame.pack()
#
#
# class StartPage(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="Go to page one",
#                   command=lambda: master.switch_frame(PageOne)).pack()
#         tk.Button(self, text="Go to page two",
#                   command=lambda: master.switch_frame(PageTwo)).pack()
#
#
# class PageOne(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self, bg='blue')
#         tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
#
#
# class PageTwo(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self, bg='red')
#         tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
#
#
# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()
# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/
# https://pythonprogramming.net/change-show-new-frame-tkinter/?completed=/passing-functions-parameters-tkinter-using-lambda/

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "App Title")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.von_ueberall_erreichbar = 0
        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def getVUE(self):
        return self.von_ueberall_erreichbar

    def raiseVUE(self, targetFrame):
        self.von_ueberall_erreichbar += 1
        self.frames[targetFrame].label2.config(text=self.getVUE())

    def show_frame(self, targetFrame):
        frame = self.frames[targetFrame]
        self.frames[targetFrame].label2.config(text=self.getVUE())
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="+1",
                             command=lambda: controller.raiseVUE(StartPage))
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="+1",
                             command=lambda: controller.raiseVUE(PageOne))
        button3.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()

        button3 = ttk.Button(self, text="+1",
                             command=lambda: controller.raiseVUE(PageTwo))
        button3.pack()


if __name__ == '__main__':
    app = Application()

    # set window size
    app.geometry("210x180+30+30")

    # init menubar
    menubar = tk.Menu(app)

    # creating the menus
    menuManage = tk.Menu(menubar, tearoff=0)

    # list of menubar elements
    menubar.add_cascade(menu=menuManage, label="Frame")

    # menu: manage
    menuManage.add_command(label="P1", command=lambda: app.show_frame(PageOne))
    menuManage.add_command(label="P2", command=lambda: app.show_frame(PageTwo))
    menuManage.add_command(label="Start", command=lambda: app.show_frame(StartPage))

    # attach menubar
    app.config(menu=menubar)

    app.mainloop()
