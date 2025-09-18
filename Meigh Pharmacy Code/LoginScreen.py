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

import LoginScreen_Functions

def vp_start_system():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    LoginScreen_Functions.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    LoginScreen_Functions.init(w, top, *args, **kwargs)
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
        font11 = "-family {Segoe UI} -size 19 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("427x299+633+256")
        top.title("Login Screen")
        top.configure(background="#f0ffff")
        top.configure(highlightbackground="#f0ffff")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#f0ffff")
        self.Frame1.configure(highlightbackground="#f0ffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=125)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.14, rely=0.03, height=41, width=305)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#f0ffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#f0ffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Meigh Pharmacy''')

        self.Labelframe1 = LabelFrame(self.Frame1)
        self.Labelframe1.place(relx=0.02, rely=0.17, relheight=0.82
                , relwidth=0.96)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Please Enter Your Username and Password to Continue:''')
        self.Labelframe1.configure(background="#f0ffff")
        self.Labelframe1.configure(highlightbackground="#f0ffff")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=410)

        self.UsernameLabel = Label(self.Labelframe1)
        self.UsernameLabel.place(relx=0.04, rely=0.69, height=21, width=62)
        self.UsernameLabel.configure(activebackground="#f9f9f9")
        self.UsernameLabel.configure(activeforeground="black")
        self.UsernameLabel.configure(background="#f0ffff")
        self.UsernameLabel.configure(disabledforeground="#a3a3a3")
        self.UsernameLabel.configure(foreground="#000000")
        self.UsernameLabel.configure(highlightbackground="#f0ffff")
        self.UsernameLabel.configure(highlightcolor="black")
        self.UsernameLabel.configure(text='''Username:''')

        self.PasswordLabel = Label(self.Labelframe1)
        self.PasswordLabel.place(relx=0.05, rely=0.82, height=21, width=59)
        self.PasswordLabel.configure(activebackground="#f9f9f9")
        self.PasswordLabel.configure(activeforeground="black")
        self.PasswordLabel.configure(background="#f0ffff")
        self.PasswordLabel.configure(disabledforeground="#a3a3a3")
        self.PasswordLabel.configure(foreground="#000000")
        self.PasswordLabel.configure(highlightbackground="#f0ffff")
        self.PasswordLabel.configure(highlightcolor="black")
        self.PasswordLabel.configure(text='''Password:''')

        self.UsernameEntry = Entry(self.Labelframe1)
        self.UsernameEntry.place(relx=0.22, rely=0.69,height=20, relwidth=0.4)
        self.UsernameEntry.configure(background="white")
        self.UsernameEntry.configure(disabledforeground="#a3a3a3")
        self.UsernameEntry.configure(font=font10)
        self.UsernameEntry.configure(foreground="#000000")
        self.UsernameEntry.configure(highlightbackground="#f0ffff")
        self.UsernameEntry.configure(highlightcolor="black")
        self.UsernameEntry.configure(insertbackground="black")
        self.UsernameEntry.configure(selectbackground="#c4c4c4")
        self.UsernameEntry.configure(selectforeground="black")

        self.PasswordEntry = Entry(self.Labelframe1)
        self.PasswordEntry.place(relx=0.22, rely=0.82,height=20, relwidth=0.4)
        self.PasswordEntry.configure(background="white")
        self.PasswordEntry.configure(disabledforeground="#a3a3a3")
        self.PasswordEntry.configure(font=font10)
        self.PasswordEntry.configure(foreground="#000000")
        self.PasswordEntry.configure(highlightbackground="#f0ffff")
        self.PasswordEntry.configure(highlightcolor="black")
        self.PasswordEntry.configure(insertbackground="black")
        self.PasswordEntry.configure(selectbackground="#c4c4c4")
        self.PasswordEntry.configure(selectforeground="black")

        self.NewUserButton = Button(self.Labelframe1)
        self.NewUserButton.place(relx=0.8, rely=0.69, height=54, width=71)
        self.NewUserButton.configure(activebackground="#f0ffff")
        self.NewUserButton.configure(activeforeground="#000000")
        self.NewUserButton.configure(background="#f0ffff")
        self.NewUserButton.configure(command=LoginScreen_Functions.registeruser)
        self.NewUserButton.configure(disabledforeground="#a3a3a3")
        self.NewUserButton.configure(foreground="#000000")
        self.NewUserButton.configure(highlightbackground="#f0ffff")
        self.NewUserButton.configure(highlightcolor="black")
        self.NewUserButton.configure(pady="0")
        self.NewUserButton.configure(text='''New Users''')

        self.SubmitUserButton = Button(self.Labelframe1)
        self.SubmitUserButton.place(relx=0.63, rely=0.69, height=54, width=59)
        self.SubmitUserButton.configure(activebackground="#f0ffff")
        self.SubmitUserButton.configure(activeforeground="#000000")
        self.SubmitUserButton.configure(background="#f0ffff")
        self.SubmitUserButton.configure(command=LoginScreen_Functions.attemptlogin)
        self.SubmitUserButton.configure(disabledforeground="#a3a3a3")
        self.SubmitUserButton.configure(foreground="#000000")
        self.SubmitUserButton.configure(highlightbackground="#f0ffff")
        self.SubmitUserButton.configure(highlightcolor="black")
        self.SubmitUserButton.configure(pady="0")
        self.SubmitUserButton.configure(text='''Continue''')

        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0, rely=0, height=140, width=400)
        self.Label2.configure(background="#f0ffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self._img1 = PhotoImage(file="MPharmLogo.png")
        self.Label2.configure(image=self._img1)
        self.Label2.configure(text='''Label''')
        self.Label2.configure(width=159)


if __name__ == '__main__':
    vp_start_system()
