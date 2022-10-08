from tkinter import *;
import mysql.connector;

class window():
    root = None;
    info = [];
    def __init__(self, root):
        self.root = root;

#creating an account
    def create_acc(self):
        self.delete();

#delete
    def delete(self):
        for i in self.root.winfo_children():
            i.destroy();

#login
    def login_backend(self, username, password):
        login_permitted = True;
        if (login_permitted):
            self.info = [username, password];
        self.delete();

    def login(self):
        self.delete();

        l1 = Label(self.root, text="Enter username: ");
        l1.grid(row=0, column=0);

        l2 = Label(self.root, text="Enter password: ");
        l2.grid(row=1, column=0);

        name = Entry(self.root);
        name.grid(row=0, column=1)

        pass_ = Entry(self.root);
        pass_.grid(row=1,column=1);

        button = Button(self.root, text="Login", command=lambda: self.login_backend(username=name.get(), password=pass_.get()))
        button.grid(row=2, column=1)

# main function
    def main(self):
        self.root.geometry = "50x50";
        self.root.title("Chatplus");

        login_button = Button(self.root, text="Login", command=self.login)
        login_button.pack();

        create_acc_button = Button(self.root, text="Create Account", command=self.create_acc);
        create_acc_button.pack();

#returning info
    def getInfo(self):
        return self.info;