# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
# https://pythonprogramming.net/change-show-new-frame-tkinter/?completed=/passing-functions-parameters-tkinter-using-lambda/

import tkinter as tk
from tkinter import ttk
from pathlib import Path
import sys, os, json, socket, threading

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# from core.users.Account import Account

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

ACTIVATION = False

LARGE_FONT = ("Verdana", 12)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def LoginVerified():
    global ACTIVATION
    ID = UserName.get()
    PW = UserPassword.get()
    Result = Account().SignIn(UserName=ID, UserPassword=PW)

    ACTIVATION = True if Result else False
    ChatScreen()


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

        for F in (StartPage, PageOne, PageTwo):
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
        # self.frames[targetFrame].label2.config(text=self.getVUE())
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global UserName, UserPassword

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
        image_image_1 = tk.PhotoImage(
            file=relative_to_assets("image_1.png")
        )
        canvas.create_image(
            235.0,
            215.0,
            image=image_image_1
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
            command=lambda: controller.show_frame(PageOne),
            bd=0,
            bg='#FFF5EB',
            activebackground='#FFF5EB',
            text='Sign In',
            font=("Arial " + str(16 * 1) + " underline")
        ).place(x=263.0, y=625)

        tk.Button(
            self,
            #command=RegisterVerified,
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

        # label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        # label.pack(pady=10, padx=10)
        #
        # self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        # self.label2.pack(pady=10, padx=10)

        # button = ttk.Button(self, text="Visit Page 1",
        #                     command=lambda: controller.show_frame(PageOne))
        # button.pack()
        #
        # button2 = ttk.Button(self, text="Visit Page 2",
        #                      command=lambda: controller.show_frame(PageTwo))
        # button2.pack()
        #
        # button3 = ttk.Button(self, text="+1",
        #                      command=lambda: controller.raiseVUE(StartPage))
        # button3.pack()


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


app = Application()

# set window size
app.iconbitmap(relative_to_assets("3_icon.ico"))
app.geometry("450x700")
app.configure(bg="#FFF5EB")
app.resizable(False, False)

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
