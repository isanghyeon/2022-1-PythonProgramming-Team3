# import modules

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, StringVar, Toplevel, Label
from pathlib import Path
import sys, os, json, socket, threading

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.users.Account import Account

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

ACTIVATION = False


class SocketStart:
    def __init__(self):
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Host = "logos.sch.ac.kr"
        self.Port = 45100
        self.sock_conn = self.client_sock.connect((self.Host, self.Port))

    def ThreadStart(self):
        SendThread = threading.Thread(target=self.Send, args=(self.sock_conn,))
        SendThread.start()

        RecvThread = threading.Thread(target=self.Recv, args=(self.sock_conn,))
        RecvThread.start()

    def Send(self):
        while True:
            send_data = bytes(input().encode())
            self.sock_conn.send(send_data)

    def Recv(self):
        while True:
            recv_data = self.sock_conn.recv(1024).decode()
            print(recv_data)


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


def ChatScreen():
    global ACTIVATION
    if ACTIVATION:
        global ChatScreen
        ChatScreen = Toplevel(WindowScreen)
        ChatScreen.title("Chat Screen")
        ChatScreen.geometry("700x700")

        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()

        Label(ChatScreen, text="Please enter details below", bg="blue").pack()
        Label(ChatScreen, text="").pack()
        username_lable = Label(ChatScreen, text="Username * ")
        username_lable.pack()
        username_entry = Entry(ChatScreen, textvariable=username)
        username_entry.pack()
        password_lable = Label(ChatScreen, text="Password * ")
        password_lable.pack()
        password_entry = Entry(ChatScreen, textvariable=password, show='*')
        password_entry.pack()
        Label(ChatScreen, text="").pack()
        Button(ChatScreen, text="Register", width=10, height=1, bg="blue").pack()

    ACTIVATION = False


# Designing Main(first) window
def MainScreen():
    global WindowScreen
    global UserName, UserPassword
    WindowScreen = Tk()

    WindowScreen.iconbitmap(relative_to_assets("3_icon.ico"))
    WindowScreen.title("UDA Chat")
    WindowScreen.geometry("450x700")
    WindowScreen.configure(bg="#FFF5EB")
    WindowScreen.resizable(False, False)

    canvas = Canvas(
        WindowScreen,
        bg="#FFF5EB",
        height=700,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
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

    UserName = StringVar()
    UserPassword = StringVar()

    UserName_ID = Entry(WindowScreen, font=("Arial " + str(16 * 1)), bd=0, textvariable=UserName)
    UserPassword_PW = Entry(WindowScreen, font=("Arial " + str(16 * 1)), bd=0, textvariable=UserPassword, show='*')
    UserName_ID.place(x=145, y=462, width=207, height=30)
    UserPassword_PW.place(x=145, y=547, width=207, height=30)

    Button(
        WindowScreen,
        command=LoginVerified,
        bd=0,
        bg='#FFF5EB',
        activebackground='#FFF5EB',
        text='Sign In',
        font=("Arial " + str(16 * 1) + " underline")
    ).place(x=263.0, y=625)

    Button(
        WindowScreen,
        command=RegisterVerified,
        bd=0,
        bg='#FFF5EB',
        activebackground='#FFF5EB',
        text='Sign Up',
        font=("Arial " + str(16 * 1) + " underline")
    ).place(x=142.0, y=625)

    # ID & PW Underline
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

    WindowScreen.mainloop()


MainScreen()
