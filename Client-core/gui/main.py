# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
# https://pythonprogramming.net/change-show-new-frame-tkinter/?completed=/passing-functions-parameters-tkinter-using-lambda/
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import sys, os, json, socket, threading

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.api import ChatRoom, User
from core.messages.GetAllMessage import GetAllMessage
from core.messages.CreateMessage import CreateMessage
from core.chatroom.EnteredChatRooom import EnteredChatRooom

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
        global UserName_ID, UserPassword_PW

        def LoginVerified():
            global UserID, UserKey

            ID = UserName.get()
            PW = UserPassword.get()

            if ID == '':
                tk.messagbox.showerror("ID Error", "Please enter your ID.")
            elif PW == '':
                tk.messagbox.showerror("PW Error", "Please enter your PW.")
            else:
                result = User().UserSignIn(uname=ID, upw=PW)

                if result["status"] == "200":
                    tk.messagebox.showinfo("Success", "Sign In Successful")
                    UserKey = result["data"]["UserUniqKey"]
                    UserID = ID
                    app.show_frame(PageOne)
                else:
                    tk.messagebox.showerror("Error", "Sign In Failed")

        def RegisterVerified():
            ID = UserName.get()
            PW = UserPassword.get()
            if ID == '':
                tk.messagebox.showerror("ID Error", "Please enter your ID.")
            elif PW == '':
                tk.messagebox.showerror("PW Error", "Please enter your PW.")
            else:
                data = {"UserName": ID, "UserAccountPW": PW}
                result = User().UserRegister(data=data)

                if result["status"] == "201":
                    tk.messagebox.showinfo("Success", "Sign Up Successful")
                    UserPassword_PW.delete(0, 'end')
                    UserName_ID.delete(0, 'end')
                else:
                    tk.messagebox.showerror("Error", "Sign Up Failed")

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

        MainImage = tk.PhotoImage(file=relative_to_assets("MainImage.png"), master=self)
        image = tk.Label(self, image=MainImage, bg="#FFF5EB")
        image.image = MainImage
        image.place(x=96, y=76)

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
            command=LoginVerified,
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

        def RecvChatData(ChatKey):
            result = []
            data = [ChatList for ChatList in GetAllMessage().AllMessage(key=ChatKey)]
            if data:
                data2 = [data[idx]["UserName"] for idx in range(len(data))]
                data3 = [data[idx]["MessageData"] for idx in range(len(data))]

                for idx in range(len(data2)):
                    result.append(f"{data2[idx]}: {data3[idx]}")

                return result
            else:
                return ["There's no message."]

        def SendChatMessage(event):
            global ChatKey, UserID, UserKey
            CMsg = ChattingMSG.get()
            CreateMessage().AddMessage(data={
                "UserUniqKey": UserKey,
                "ChatUniqKey": ChatKey,
                "UserName": UserID,
                "MessageData": CMsg
            })

            load_Chat()

        def EnteredChatRoom():
            global ChatKey, UserID, UserKey

            EnteredChatRooom().AddUser(key=ChatKey, data={
                "ParticipantUserName": UserID,
                "ParticipantUserUniqKey": UserKey
            })

        def creatchat():
            global UserID, UserKey, ChatAllData, chat_list

            ChatAllData = ChatRoom().ChatRoomGetAllData()["data"]
            count = len(ChatAllData)

            if (count > 100):
                tk.messagebox.showerror("Error", "Mort than 100 chat rooms")
            else:
                data = {"ParticipantUserName": UserID, "ParticipantUserUniqKey": UserKey}
                result = ChatRoom().ChatRoomAdd(data=data)

                if result["status"] == "201":
                    tk.messagebox.showinfo("Success", "Create Chat Successful")
                    load_ChatRoom()
                else:
                    tk.messagebox.showerror("Error", "Create Chat Failed")


        def program_off():
            app.quit()

        def LogOut():
            global UserName_ID, UserPassword_PW

            UserPassword_PW.delete(0, 'end')
            UserName_ID.delete(0, 'end')
            controller.show_frame(StartPage)

        def click(event):
            global ChatAllData, chat_list, ChatKey

            mlist=[]
            ChatKey = ChatAllData[int(chat_list.curselection()[0])]["ChatUniqKey"]
            EnteredChatRoom()
            entry_chat.config(state="normal")

            for idx in ChatAllData[int(chat_list.curselection()[0])]["ParticipantUserName"].replace(" ", "").split(","):
                mlist.append(idx)

            mlist = tk.StringVar(value=mlist)
            member_list = tk.Listbox(mlist_frame,
                                     bg="#FFAAA7",
                                     bd=1,
                                     font="Arial 15",
                                     listvariable=mlist,
                                     relief="solid",
                                     selectbackground="#FFE59D",
                                     selectforeground="#000000"
                                     )
            member_list.place(x=-2, y=-2, width=355, height=607)

            load_Chat()

        def load_Chat():
            global ChatKey
            MessageListBox = tk.Listbox(message_frame,
                                        bg="#ffffff",
                                        bd=1,
                                        font="Arial 20",
                                        listvariable=tk.StringVar(value=RecvChatData(ChatKey=ChatKey)),
                                        relief="solid",
                                        selectbackground="#FFE59D",
                                        selectforeground="#000000"
                                        )
            MessageListBox.place(x=-2, y=-2, width=741, height=607)

        def load_ChatRoom():
            global ChatAllData, chat_list

            clist = []
            ChatAllData = ChatRoom().ChatRoomGetAllData()["data"]

            if ChatAllData != None:
                for i in ChatAllData:
                    clist.append(i["ChatName"])

            clist = tk.StringVar(value=clist)
            chat_list = tk.Listbox(clist_frame,
                                   font="Arial 15",
                                   listvariable=clist,
                                   bg="#FFD3B4",
                                   bd=1,
                                   relief="solid",
                                   selectbackground="#BDE6F1",
                                   selectforeground="#000000"
                                   )
            chat_list.bind('<Double-1>', click)
            chat_list.place(x=-2, y=-2, width=354, height=607)


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
                               bg="#FFAAA7",
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

        load_ChatRoom()

        ChattingMSG = tk.StringVar()

        entry_chat = tk.Entry(message_frame, font='Arial 16', bd=1, relief='solid', textvariable=ChattingMSG, state="disabled")
        entry_chat.place(x=-1, y=603.4, width=739, height=57.6)
        entry_chat.bind("<Return>", SendChatMessage)

        creat_chat = tk.Button(self, command=creatchat, text="Create", font="Arial 25", bg="#FFF5EB", bd=1, activebackground="#FFF5EB", relief="solid")
        creat_chat.place(x=0, y=662.4, width=352, height=57.6)

        canvas.create_rectangle(
            1089.0,
            662.0,
            1460.0,
            719.0,
            fill="#FFF5EB",
            outline="black")

        setting_photo = tk.PhotoImage(file=relative_to_assets("img.png"), master=self)
        setting = tk.Button(self, image=setting_photo, command=None, bg="#FFF5EB", bd=0, activebackground="#FFF5EB")
        setting.image = setting_photo
        setting.place(x=1133.77, y=673.2)

        logout_photo = tk.PhotoImage(file=relative_to_assets("img_1.png"), master=self)
        logout = tk.Button(self, image=logout_photo, command=LogOut, bg="#FFF5EB", bd=0, activebackground="#FFF5EB")
        logout.image = logout_photo
        logout.place(x=1246.59, y=675)

        off_photo = tk.PhotoImage(file=relative_to_assets("img_2.png"), master=self)
        off = tk.Button(self, image=off_photo, command=program_off, bg="#FFF5EB", bd=0, activebackground="#FFF5EB")
        off.image = off_photo
        off.place(x=1355.83, y=673.2)

        refresh_photo = tk.PhotoImage(file=relative_to_assets("img_3.png"), master=self)
        refresh = tk.Button(self, image=refresh_photo, command=load_ChatRoom, bg="#98DDCA", bd=0, activebackground="#98DDCA")
        refresh.image = refresh_photo
        refresh.place(x=290, y=10)



if __name__ == '__main__':
    app = Application()

    # set window size
    app.iconbitmap(relative_to_assets("favicon.ico"))
    app.mainloop()
