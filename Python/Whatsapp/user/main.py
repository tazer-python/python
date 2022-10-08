import socket;
from login import window;
from tkinter import *;
""" PORT = 5050;
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
client.connect(ADDR);
"""

def checker(info):
    print(info)

root = Tk()
x = window(root = root);
x.main()


root.mainloop();