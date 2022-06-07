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
from core.chatroom.CreateChatRoom import CreateChatRoom
from core.chatroom.GetAllChatRoom import GetAllChatRoom
from core.messages.GetAllMessage import GetAllMessage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

LARGE_FONT = ("Verdana", 12)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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

        # self.show_frame(StartPage)
        self.show_frame(PageOne)

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

        def LoginVerified():
            ID = UserName.get()
            PW = UserPassword.get()
            Result = Account().SignIn(UserName=ID, UserPassword=PW)

            print(Result)
            return True if Result else False

        def RegisterVerified():
            ID = UserName.get()
            PW = UserPassword.get()
            Result = Account().SignUp(UserName=ID, UserPassword=PW)

            return True if Result else False

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

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
            command=(lambda: controller.show_frame(PageOne)) if LoginVerified else (lambda: controller.show_frame(StartPage)),  # TODO: 로그인 구현
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
        def ClickChatListCallback():
            return [ChatList["ParticipantUserName"] for ChatList in GetAllChatRoom().ChatRoomGetAllData()]

        def ClickChatNameCallback():
            return [ChatList["ChatName"] for ChatList in GetAllChatRoom().ChatRoomGetAllData()]

        def RecvChatData():
            # return [ChatList for ChatList in GetAllMessage().AllMessage(key="29a738741e19eb4e9aeef2a5da80ee5506e34595960ffb33752bc5f7088de2e5")]
            data = [ChatList for ChatList in GetAllMessage().AllMessage(key="29a738741e19eb4e9aeef2a5da80ee5506e34595960ffb33752bc5f7088de2e5")]
            data2 = [data[idx]["UserName"] for idx in range(len(data))]
            data3 = [data[idx]["MessageData"] for idx in range(len(data))]

            result = []
            for idx in range(len(data2)):
                result.append(f"{data2[idx]} : {data3[idx]}")

            return result

        def SendChatMessage():
            pass

        def CreateChatRoom():
            pass

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

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
        # image_image_1 = tk.PhotoImage(file=relative_to_assets("MainImage.png"), master=self)
        # canvas.create_image(
        #     235.0,
        #     215.0,
        #     image=image_image_1
        # )

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

        ChatListFrame = tk.Frame(self,
                                 relief="solid",
                                 bd=1,
                                 width=352,
                                 height=605)
        ChatListFrame.place(x=0, y=57.6)

        ChatListBox = tk.Listbox(ChatListFrame,
                                 font="Arial 20",
                                 listvariable=tk.StringVar(value=ClickChatNameCallback()),
                                 bg="#FFD3B4",
                                 bd=1,
                                 relief="solid",
                                 selectbackground="#BDE6F1",
                                 selectforeground="#000000",
                                 )

        ChatListBox.place(x=-2, y=-2, width=450, height=607)

        MemberListFrame = tk.Frame(self,
                                   relief="solid",
                                   bd=1,
                                   width=352,
                                   height=605.5)
        MemberListFrame.place(x=1089, y=57.6)



        MessageListFrame = tk.Frame(self,
                                    relief="solid",
                                    bg="#FFFFFF",
                                    bd=1,
                                    width=739,
                                    height=662)
        MessageListFrame.place(x=351, y=58)

        MessageListBox = tk.Listbox(MessageListFrame,
                                   bg="#000000",
                                   bd=1,
                                   font="Arial 30",
                                   listvariable=tk.StringVar(value=RecvChatData()),
                                   relief="solid",
                                   selectbackground="#FFE59D",
                                   selectforeground="#000000"
                                   )
        MessageListBox.place(x=-2, y=-2, width=900, height=607)

        MemberListBox = tk.Listbox(MemberListFrame,
                                   bg="#FFAAA7",
                                   bd=1,
                                   font="Arial 20",
                                   listvariable=tk.StringVar(value=ClickChatListCallback()),
                                   relief="solid",
                                   selectbackground="#FFE59D",
                                   selectforeground="#000000"
                                   )
        MemberListBox.place(x=-2, y=-2, width=355, height=607)

        MessageEntry = tk.Entry(MessageListFrame, font='Arial 16', bd=1, relief='solid')
        MessageEntry.place(x=-1, y=603.4, width=739, height=57.6)

        CreateChat = tk.Button(self, command=None, text="Create", font="Arial 25", bg="#FFF5EB", bd=1, activebackground="#FFF5EB", relief="solid")
        CreateChat.place(x=0, y=662.4, width=175.5, height=57.6)

        ExistProgram = tk.Button(self, command=None, text="Exit", font="Arial 25", bg="#FFF5EB", bd=1, activebackground="#FFF5EB", relief="solid")
        ExistProgram.place(x=175.4, y=662.4, width=177, height=57.6)

        canvas.create_rectangle(
            1089.0,
            662.0,
            1460.0,
            719.0,
            fill="#FFF5EB",
            outline="black"
        )

        setting_photo = tk.PhotoImage(file="/Users/isanghyeon/Developments/Dept-DISE-2020_24/2022-1-PythonProgramming-Team3/client/gui/assets/img.png", master=self)
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
    app.iconbitmap("assets/favicon.ico")
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
