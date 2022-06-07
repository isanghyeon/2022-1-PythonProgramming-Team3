# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
# https://pythonprogramming.net/change-show-new-frame-tkinter/?completed=/passing-functions-parameters-tkinter-using-lambda/

import tkinter as tk
from tkinter import ttk
from pathlib import Path
import sys, os, json, socket, threading

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.users.Account import Account
from core.api import ChatRoom

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

LARGE_FONT = ("Verdana", 12)

global chat_rooms
chat_rooms = ChatRoom().ChatRoomGetAllData()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def LoginVerified():
    global ACTIVATION
    ID = UserName.get()
    PW = UserPassword.get()
    Result = Account().SignIn(UserName=ID, UserPassword=PW)

    ACTIVATION = True if Result else False


def RegisterVerified():
    global ACTIVATION
    ID = UserName.get()
    PW = UserPassword.get()
    Result = Account().SignUp(UserName=ID, UserPassword=PW)

    ACTIVATION = True if Result else False


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "UDA Chat")

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
        # self.frames[targetFrame].label2.config(text=self.getVUE())

    def show_frame(self, targetFrame):
        frame = self.frames[targetFrame]
        if str(frame) == ".!frame.!startpage":
            tk.Tk.wm_geometry(self, "450x700")
            tk.Tk.wm_resizable(self, False, False)
        else:
            tk.Tk.wm_geometry(self, "1440x720")
            tk.Tk.wm_resizable(self, False, False)

        # self.frames[targetFrame].label2.config(text=self.getVUE())
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global ACTIVATION, UserName, UserPassword

        ACTIVATION = False

        canvas = tk.Canvas(
            self,
            bg="#FFF5EB",
            height=700,
            width=450,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        canvas.create_image(
            235.0,
            215.0,
            image=tk.PhotoImage(file=relative_to_assets("MainImage.png"))
        )

        canvas.create_text(
            103.8773193359375,
            466.90625,
            anchor="nw",
            text="ID",
            fill="#000000",
            font=("Arial", 17 * -1)
        )

        canvas.create_text(
            99.0,
            553.125,
            anchor="nw",
            text="PW",
            fill="#000000",
            font=("Arial", 17 * -1)
        )

        UserName = tk.StringVar()
        UserPassword = tk.StringVar()

        UserName_ID = tk.Entry(self, font=("Arial " + str(16 * 1)), bd=0, textvariable=UserName)
        UserPassword_PW = tk.Entry(self, font=("Arial " + str(16 * 1)), bd=0, textvariable=UserPassword, show='*')
        UserName_ID.place(x=145, y=462, width=207, height=30)
        UserPassword_PW.place(x=145, y=547, width=207, height=30)

        tk.Button(
            self,
            command=lambda: controller.show_frame(PageOne),  # TODO: 로그인 구현
            bd=0,
            bg='#FFF5EB',
            activebackground='#FFF5EB',
            text='Sign In',
            font=("Arial " + str(16 * 1) + " underline")
        ).place(x=263.0, y=625)

        tk.Button(
            self,
            command=RegisterVerified,
            bd=0,
            bg='#FFF5EB',
            activebackground='#FFF5EB',
            text='Sign Up',
            font=("Arial " + str(16 * 1) + " underline")
        ).place(x=142.0, y=625)

        canvas.create_rectangle(
            145.0,
            492.9999809265137,
            352.0,
            493.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            145.0,
            577.9999847412109,
            352.0,
            578.0,
            fill="#000000",
            outline="")


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=720,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        image_image_1 = tk.PhotoImage(file=relative_to_assets("MainImage.png"), master=self)
        canvas.create_image(
            235.0,
            215.0,
            image=image_image_1
        )

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

        clist_frame = tk.Frame(self,
                               relief="solid",
                               bd=1,
                               width=352,
                               height=605)
        clist_frame.place(x=0, y=57.6)

        mlist_frame = tk.Frame(self,
                               relief="solid",
                               bd=1,
                               width=352,
                               height=605.5)
        mlist_frame.place(x=1089, y=57.6)

        message_frame = tk.Frame(self,
                                 relief="solid",
                                 bg="#FFFFFF",
                                 bd=1,
                                 width=739,
                                 height=662)
        message_frame.place(x=351, y=58)

        entry_chat = tk.Entry(message_frame, font=('Arial 16'), bd=1, relief='solid')
        entry_chat.place(x=-1, y=603.4, width=739, height=57.6)

        clist = []
        for i in chat_rooms["data"]:
            clist.append(i["ChatName"])

        clist = tk.StringVar(value=clist)
        chat_list = tk.Listbox(clist_frame,
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

        clist = tk.StringVar(value=clist)
        member_list = tk.Listbox(mlist_frame,
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
                tk.messagebox.showerror("Error", "Mort than 100 chat rooms")
                return 0
            else:
                tk.messagebox.showinfo("count", count)

            data = {"ParticipantUserName": "powerman", "ParticipantUserUniqKey": "12f893bf4b52b98fc96f8d2fe318c272a6a4a8973854d86d20862ef63ee541d3"}
            result = ChatRoom().ChatRoomAdd(data=data)

            if result["status"] == "201":
                tk.messagebox.showinfo("Success", "Create Chat Successful")
            else:
                tk.messagebox.showerror("Error", "Create Chat Failed")

        creat_chat = tk.Button(self, command=creatchat, text="Create", font="Arial 25", bg="#FFF5EB", bd=1, activebackground="#FFF5EB", relief="solid")
        creat_chat.place(x=0, y=662.4, width=175.5, height=57.6)

        exit_chat = tk.Button(self, command=None, text="Exit", font="Arial 25", bg="#FFF5EB", bd=1, activebackground="#FFF5EB", relief="solid")
        exit_chat.place(x=175.4, y=662.4, width=177, height=57.6)

        canvas.create_rectangle(
            1089.0,
            662.0,
            1460.0,
            719.0,
            fill="#FFF5EB",
            outline="black")

        setting_photo = tk.PhotoImage(file=relative_to_assets("img.png"), master=self)
        setting = tk.Button(self, image=setting_photo, command=None, bg="#FFF5EB", bd=0, activebackground="#FFF5EB")
        setting.place(x=1133.77, y=673.2)

        logout_photo = tk.PhotoImage(file=relative_to_assets("img_1.png"), master=self)
        logout = tk.Button(self, image=logout_photo, command=None, bg="#FFF5EB", bd=0, activebackground="#FFF5EB")
        logout.place(x=1246.59, y=675)

        off_photo = tk.PhotoImage(file=relative_to_assets("img_2.png"), master=self)
        off = tk.Button(self, image=off_photo, command=None, bg="#FFF5EB", bd=0, activebackground="#FFF5EB")
        off.place(x=1355.83, y=673.2)

        refresh_photo = tk.PhotoImage(file=relative_to_assets("img_3.png"), master=self)
        refresh = tk.Button(self, image=refresh_photo, command=None, bg="#98DDCA", bd=0, activebackground="#98DDCA")
        refresh.place(x=290, y=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


if __name__ == '__main__':
    app = Application()

    # set window size
    app.iconbitmap(relative_to_assets("favicon.ico"))
    app.configure(bg="#FFF5EB")

    # init menubar
    menubar = tk.Menu(app)

    # creating the menus
    menuManage = tk.Menu(menubar, tearoff=0)

    # list of menubar elements
    menubar.add_cascade(menu=menuManage, label="Frame")

    # menu: manage
    menuManage.add_command(label="P1", command=lambda: app.show_frame(PageOne))
    menuManage.add_command(label="Start", command=lambda: app.show_frame(StartPage))

    # attach menubar
    app.config(menu=menubar)

    app.mainloop()
