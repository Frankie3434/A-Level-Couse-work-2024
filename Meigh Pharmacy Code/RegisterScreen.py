import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import RegisterScreen_Functions

def vp_start_system():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    RegisterScreen_Functions.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    RegisterScreen_Functions.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#f0ffff'  # X11 color: 'azure1'
        _fgcolor = '#f0ffff'  # X11 color: 'azure1'
        _compcolor = '#f0ffff' # X11 color: 'azure1'
        _ana1color = '#f0ffff' # X11 color: 'azure1' 
        _ana2color = '#f0ffff' # X11 color: 'azure1' 
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("298x281+650+150")
        top.title("Register Screen")
        top.configure(background="#f0ffff")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#f0ffff")
        self.Frame1.configure(width=298)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.23, rely=0.04, height=29, width=163)
        self.Label1.configure(background="#f0ffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Register a New User:''')

        self.Labelframe1 = LabelFrame(self.Frame1)
        self.Labelframe1.place(relx=0.03, rely=0.14, relheight=0.84
                , relwidth=0.94)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Enter the  System Key to Create a New User:''')
        self.Labelframe1.configure(background="#f0ffff")
        self.Labelframe1.configure(width=280)

        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0.04, rely=0.17, height=21, width=76)
        self.Label2.configure(background="#f0ffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''System Key:''')

        self.Label3 = Label(self.Labelframe1)
        self.Label3.place(relx=0.04, rely=0.34, height=21, width=62)
        self.Label3.configure(background="#f0ffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Username:''')

        self.Label4 = Label(self.Labelframe1)
        self.Label4.place(relx=0.04, rely=0.51, height=21, width=59)
        self.Label4.configure(background="#f0ffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Password:''')

        self.SystemKeyEntry = Entry(self.Labelframe1)
        self.SystemKeyEntry.place(relx=0.36, rely=0.17,height=20, relwidth=0.3)
        self.SystemKeyEntry.configure(background="white")
        self.SystemKeyEntry.configure(disabledforeground="#a3a3a3")
        self.SystemKeyEntry.configure(font=font10)
        self.SystemKeyEntry.configure(foreground="#000000")
        self.SystemKeyEntry.configure(insertbackground="black")
        self.SystemKeyEntry.configure(width=84)

        self.UsernameRegisterEntry = Entry(self.Labelframe1)
        self.UsernameRegisterEntry.place(relx=0.36, rely=0.34, height=20
                , relwidth=0.59)
        self.UsernameRegisterEntry.configure(background="white")
        self.UsernameRegisterEntry.configure(disabledforeground="#a3a3a3")
        self.UsernameRegisterEntry.configure(font=font10)
        self.UsernameRegisterEntry.configure(foreground="#000000")
        self.UsernameRegisterEntry.configure(insertbackground="black")

        self.PasswordRegisterEntry = Entry(self.Labelframe1)
        self.PasswordRegisterEntry.place(relx=0.36, rely=0.51, height=20
                , relwidth=0.59)
        self.PasswordRegisterEntry.configure(background="white")
        self.PasswordRegisterEntry.configure(disabledforeground="#a3a3a3")
        self.PasswordRegisterEntry.configure(font=font10)
        self.PasswordRegisterEntry.configure(foreground="#000000")
        self.PasswordRegisterEntry.configure(insertbackground="black")

        self.CreateNewUserButton = Button(self.Labelframe1)
        self.CreateNewUserButton.place(relx=0.36, rely=0.64, height=34
                , width=167)
        self.CreateNewUserButton.configure(activebackground="#f0ffff")
        self.CreateNewUserButton.configure(activeforeground="#000000")
        self.CreateNewUserButton.configure(background="#f0ffff")
        self.CreateNewUserButton.configure(command=RegisterScreen_Functions.createnewuser)
        self.CreateNewUserButton.configure(disabledforeground="#a3a3a3")
        self.CreateNewUserButton.configure(foreground="#000000")
        self.CreateNewUserButton.configure(highlightbackground="#f0ffff")
        self.CreateNewUserButton.configure(highlightcolor="black")
        self.CreateNewUserButton.configure(pady="0")
        self.CreateNewUserButton.configure(text='''Create New User''')
        self.CreateNewUserButton.configure(width=167)

        self.MainMenuButton = Button(self.Labelframe1)
        self.MainMenuButton.place(relx=0.36, rely=0.81, height=34, width=167)
        self.MainMenuButton.configure(activebackground="#f0ffff")
        self.MainMenuButton.configure(activeforeground="#000000")
        self.MainMenuButton.configure(background="#f0ffff")
        self.MainMenuButton.configure(command=RegisterScreen_Functions.mainmenureturn)
        self.MainMenuButton.configure(disabledforeground="#a3a3a3")
        self.MainMenuButton.configure(foreground="#000000")
        self.MainMenuButton.configure(highlightbackground="#f0ffff")
        self.MainMenuButton.configure(highlightcolor="black")
        self.MainMenuButton.configure(pady="0")
        self.MainMenuButton.configure(text='''Return to Main Menu''')
        self.MainMenuButton.configure(width=167)






if __name__ == '__main__':
    vp_start_system()