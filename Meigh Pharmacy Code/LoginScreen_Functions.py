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

global loginattempts
loginattempts = 3
global CurrentUser
CurrentUser = "User"

def getcurrentuser():
    global CurrentUser
    string = ('''Welcome %s''' % (CurrentUser))
    return string

def attemptlogin(): #login function
    global loginattempts #user has three attempts to login.
    global CurrentUser
    CurrentUser = w.UsernameEntry.get()
    Entry = (w.UsernameEntry.get(),w.PasswordEntry.get())
    with sqlite3.connect("MPharm.db") as db:
        cursor = db.cursor()
        sql = ("""Select * from login_details Where Username = "%s" """ % (Entry[0]))
        cursor.execute(sql)
        record = cursor.fetchall()
        db.commit
    import Validationfunctions as validate
    hashedpasswordentry = validate.hashpasswordencryption(Entry[1])
    
    if len(record)==0:#checks if username exists in login_details Table
        messagebox.showerror("Error","""User : "%s" not found, please try again.""" % (Entry[0]) )
    elif hashedpasswordentry == record[0][1]:#compares hashed password entry to password in database
        messagebox.showinfo("Success!","Login attempt successful. Main Menu will now open.")
        
        destroy_window()
        import MeighPharmacyGUI
        MeighPharmacyGUI.vp_start_system()
    else:
        messagebox.showerror("Error", "The username and password entered is incorrect, please try again.")
        loginattempts = loginattempts - 1
        messagebox.showinfo("Login Attempt","Number of login attempts left : %s" % (loginattempts))
        if loginattempts == 0:
            messagebox.showerror("Error","You have ran out of login attempts. System will now close")
            destroy_window()
    print('LoginScreen_Functions.attemptlogin')
    
    
    

def registeruser():
    print('LoginScreenFunctions.registeruser')
    destroy_window()
    import RegisterScreen
    RegisterScreen.vp_start_system()
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
    import LoginScreen
    LoginScreen.vp_start_system()