import sys
import sqlite3

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
import Validationfunctions as validate

def createnewuser():
    newuser = True
    Entry = (w.UsernameRegisterEntry.get(),w.PasswordRegisterEntry.get(),w.SystemKeyEntry.get())
    if validate.lengthcheck("Username",Entry[0],5,50) and validate.validatepassword(Entry[1]):
        with sqlite3.connect("MPharm.db") as db:
            cursor = db.cursor()
            sql = "SELECT * FROM login_details"
            cursor.execute(sql)
            records = cursor.fetchall()
            db.commit
        for record in records:
            if record[0] == Entry[0]:
                newuser = False
                messagebox.showerror("Error", "Username already taken, please try a different one.")
        
        if newuser:
            hashed = validate.hashpasswordencryption(Entry[1])
            toinsert = (Entry[0],hashed,Entry[2])
            with sqlite3.connect("MPharm.db") as db:
                cursor = db.cursor()
                sql ="insert into login_details(Username,Password,UserType) values(?,?,?)"
                cursor.execute(sql,toinsert)
                db.commit
            messagebox.showinfo("Success!","New User : %s has been created. You will now return to the Login Screen." % (Entry[0]))
            mainmenureturn()
            print('RegisterScreenFunctions.createnewuser')
    sys.stdout.flush()

def mainmenureturn():
    destroy_window()
    import LoginScreen
    LoginScreen.vp_start_system()
    print('RegisterScreen_Functions.mainmenureturn')
    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import RegisterScreen
    RegisterScreen.vp_start_system()