import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import json
from pathlib import Path
from API.api import User, ChatRoom

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, Frame, Listbox, Label, StringVar

global chat_rooms
chat_rooms=ChatRoom().ChatRoomGetAllData()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go to page one",
                  command=lambda: master.switch_frame(PageOne)).pack()
        Button(self, text="Go to page two",
                  command=lambda: master.switch_frame(PageTwo)).pack()

        # self.entry_id = None
        # self.entry_pw = None
        # self.UserUK = None
        #
        # canvas = Canvas(
        #     self,
        #     bg="#FFF5EB",
        #     height=700,
        #     width=450,
        #     bd=0,
        #     highlightthickness=0,
        #     relief="ridge"
        # )
        # canvas.place(x=0, y=0)
        #
        # logo = PhotoImage(file=relative_to_assets("image_0.png"))
        #
        # canvas.create_image(
        #     96.0,
        #     76.0,
        #     image=logo
        # )

        # Sign In Button
        si_button = Button(
            self,
            command=self.sign_in,
            bd=0,
            bg='#FFF5EB',
            activebackground='#FFF5EB',
            text='Sign In',
            font=("Arial " + str(16 * 1) + " underline"),
            anchor="nw"
        )
        si_button.place(x=263, y=625)

        # Sign Up Button
        su_button = Button(
            self,
            command=self.sign_up,
            bd=0,
            bg='#FFF5EB',
            activebackground='#FFF5EB',
            text='Sign Up',
            font=("Arial " + str(16 * 1) + " underline"),
            anchor="nw"
        )
        su_button.place(x=142, y=625)


        # canvas.create_text(
        #     103.8773193359375,
        #     466.90625,
        #     anchor="nw",
        #     text="ID",
        #     fill="#000000",
        #     font=("Arial", 17 * -1)
        # )
        #
        # canvas.create_text(
        #     99.0,
        #     553.125,
        #     anchor="nw",
        #     text="PW",
        #     fill="#000000",
        #     font=("Arial", 17 * -1)
        # )
        #
        # # ID & PW Underline
        # canvas.create_rectangle(
        #     145.0,
        #     492.9999809265137,
        #     352.0,
        #     493.0,
        #     fill="#000000",
        #     outline="")
        #
        # canvas.create_rectangle(
        #     145.0,
        #     577.9999847412109,
        #     352.0,
        #     578.0,
        #     fill="#000000",
        #     outline="")

        # ID & PW Entry
        self.entry_id = Entry(self, font=('Arial 12'), bd=0)
        self.entry_pw = Entry(self, font=('Arial 12'), bd=0, show='*')
        self.entry_id.place(x=145, y=462, width=207, height=30)
        self.entry_pw.place(x=145, y=547, width=207, height=30)


        # If login_Button State == 'Active'

    def sign_in(self):
        ID = self.entry_id.get()
        PW = self.entry_pw.get()

        if ID == '':
            messagebox.showerror("ID Error", "Please enter your ID.")
        elif PW == '':
            messagbox.showerror("PW Error", "Please enter your PW.")
        else:
            result = User().UserSignIn(uname=ID, upw=PW)
            self.UserUK = result["data"]

            if result["status"] == "200":
                messagebox.showinfo("Success", "Sign In Successful")
                master.switch_frame(chat)
            else:
                messagebox.showerror("Error", "Sign In Failed")

        # If su_button state == 'Active'

    def sign_up(self):
        ID = self.entry_id.get()
        PW = self.entry_pw.get()

        if ID == '':
            messagebox.showerror("ID Error", "Please enter your ID.")
        elif PW == '':
            messagebox.showerror("PW Error", "Please enter your PW.")
        else:
            data = {"UserName": ID, "UserAccountPW": PW}
            result = User().UserRegister(data=data)

            if result["status"] == "201":
                messagebox.showinfo("Success", "Sign Up Successful")
            else:
                messagebox.showerror("Error", "Sign Up Failed")


class PageOne(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=720,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        canvas.create_rectangle(
            351.0,
            0.0,
            1089.2000122070312,
            57.600006103515625,
            fill="#98DDCA",
            outline="black")

        canvas.create_rectangle(
            1089.0,
            0.0,
            1440.0,
            57.600006103515625,
            fill="#98DDCA",
            outline="black")

        canvas.create_rectangle(
            0.0,
            0.0,
            351.0,
            57.600006103515625,
            fill="#98DDCA",
            outline="black")

        canvas.create_text(
            657.0,
            14.0,
            anchor="nw",
            text="Chat Room",
            fill="#000000",
            font=("ArialMT", 25 * -1, "bold")
        )

        canvas.create_text(
            1212.0,
            14.0,
            anchor="nw",
            text="Members",
            fill="#000000",
            font=("ArialMT", 25 * -1, "bold")
        )

        canvas.create_text(
            126.0,
            14.0,
            anchor="nw",
            text="Chat List",
            fill="#000000",
            font=("ArialMT", 25 * -1, "bold")
        )

        clist_frame = Frame(self,
                            relief="solid",
                            bd=1,
                            width=352,
                            height=605)
        clist_frame.place(x=0, y=57.6)

        mlist_frame = Frame(self,
                            relief="solid",
                            bd=1,
                            width=352,
                            height=605.5)
        mlist_frame.place(x=1089, y=57.6)

        message_frame = Frame(self,
                              relief="solid",
                              bg="#FFFFFF",
                              bd=1,
                              width=739,
                              height=662)
        message_frame.place(x=351, y=58)

        entry_chat = Entry(message_frame, font=('Arial 16'), bd=1, relief='solid')
        entry_chat.place(x=-1, y=603.4, width=739, height=57.6)

        clist = []
        for i in chat_rooms["data"]:
            clist.append(i["ChatName"])

        clist = StringVar(value=clist)
        chat_list = Listbox(clist_frame,
                            font="Arial 20",
                            listvariable=clist,
                            bg="#FFD3B4",
                            bd=1,
                            relief="solid",
                            selectbackground="#BDE6F1",
                            selectforeground="#000000"
                            )
        chat_list.place(x=-2, y=-2, width=354, height=607)

        # mlist = []
        # chat_name = "6e7e711536c0220199c265d07168a8b6cbc01e759dbb5fb9974a28c89cfb76bb"
        # test = {"a":"bc", "c":"ba"}
        # for i in chat_rooms["data"]:
        #     mlist.append(i["ParticipantUserName"])

        clist = StringVar(value=clist)
        member_list = Listbox(mlist_frame,
                              bg="#FFAAA7",
                              bd=1,
                              font="Arial 20",
                              listvariable=clist,
                              relief="solid",
                              selectbackground="#FFE59D",
                              selectforeground="#000000"
                              )
        member_list.place(x=-2, y=-2, width=355, height=607)

        def creatchat():
            count = len(chat_rooms["data"])

            if (count > 100):
                messagebox.showerror("Error", "Mort than 100 chat rooms")
                return 0
            else:
                messagebox.showinfo("count", count)

            data = {"ParticipantUserName": "powerman",
                    "ParticipantUserUniqKey": "12f893bf4b52b98fc96f8d2fe318c272a6a4a8973854d86d20862ef63ee541d3"}
            result = ChatRoom().ChatRoomAdd(data=data)

            if result["status"] == "201":
                messagebox.showinfo("Success", "Create Chat Successful")
            else:
                messagebox.showerror("Error", "Create Chat Failed")

        creat_chat = Button(self, command=creatchat, text="Create", font="Arial 25", bg="#FFF5EB", bd=1,
                            activebackground="#FFF5EB", relief="solid")
        creat_chat.place(x=0, y=662.4, width=175.5, height=57.6)

        exit_chat = Button(self, command=None, text="Exit", font="Arial 25", bg="#FFF5EB", bd=1,
                           activebackground="#FFF5EB", relief="solid")
        exit_chat.place(x=175.4, y=662.4, width=177, height=57.6)

        canvas.create_rectangle(
            1089.0,
            662.0,
            1460.0,
            719.0,
            fill="#FFF5EB",
            outline="black")

        setting_photo = PhotoImage(file=relative_to_assets("image_1.png"))
        setting = Button(self, image=setting_photo, command=None, bg="#FFF5EB", bd=0, activebackground="#FFF5EB")
        setting.place(x=1133.77, y=673.2)

        logout_photo = PhotoImage(file=relative_to_assets("image_2.png"))
        logout = Button(self, image=logout_photo, command=None, bg="#FFF5EB", bd=0, activebackground="#FFF5EB")
        logout.place(x=1246.59, y=675)

        off_photo = PhotoImage(file=relative_to_assets("image_3.png"))
        off = Button(self, image=off_photo, command=None, bg="#FFF5EB", bd=0, activebackground="#FFF5EB")
        off.place(x=1355.83, y=673.2)

        refresh_photo = PhotoImage(file=relative_to_assets("image_4.png"))
        refresh = Button(self, image=refresh_photo, command=None, bg="#98DDCA", bd=0, activebackground="#98DDCA")
        refresh.place(x=290, y=10)




if __name__ == "__main__":
    app = SampleApp()
    app.iconbitmap(relative_to_assets(path="3_icon.ico"))
    app.title("UDA Chat")
    app.geometry("450x700")
    app.mainloop()