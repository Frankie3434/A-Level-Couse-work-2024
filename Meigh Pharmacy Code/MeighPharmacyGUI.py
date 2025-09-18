import sys
import sqlite3
import Validationfunctions
import LoginScreen_Functions


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

# this imports functions from MeighPharmacyGUI for later buttons
import MeighPharmacyGUI_Functions
from MeighPharmacyGUI_Functions import export_patient_data_to_text
from MeighPharmacyGUI_Functions import export_pharmacist_data_to_text
from MeighPharmacyGUI_Functions import export_booking_data_to_text
#Creates Functions for buttons later
def bookingdata():
        export_booking_data_to_text("MPharm.db", "Bookings.txt")
    

def pharmacistdata():
    export_pharmacist_data_to_text("MPharm.db", "Pharmacist.txt")

def patientdata():
        export_patient_data_to_text("Mpharm.db", "PatientList.txt")
    
    
#function for starting the system
def vp_start_system():
    '''Beginning point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Meigh_Pharmacy (root)
    MeighPharmacyGUI_Functions.init(root, top)
    root.mainloop()

w = None
def create_Meigh_Pharmacy(root, *args, **kwargs):
    '''Beginning point when module is imported.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Meigh_Pharmacy (w)
    MeighPharmacyGUI_Functions.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Meigh_Pharmacy():
    global w
    w.destroy()
    w = None

#This is the python class for the main menu window
class Meigh_Pharmacy:
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
        font13 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font=font13)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("750x650")
        top.title("Meigh Pharmacy")
        top.configure(background="#f0ffff")
        top.configure(highlightbackground="#f0ffff")
        top.configure(highlightcolor="black")
        
        #This is the creation of the tab system useing TNotebook
        
        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.0, rely=0.11, relheight=0.89, relwidth=1.0)
        self.TNotebook1.configure(width=750)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Patient",compound="left",underline="-1",)
        self.TNotebook1_t0.configure(background="#f0ffff")
        self.TNotebook1_t0.configure(highlightbackground="#f0ffff")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Pharmacist",compound="left",underline="-1",)
        self.TNotebook1_t1.configure(background="#f0ffff")
        self.TNotebook1_t1.configure(highlightbackground="#f0ffff")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="Bookings", compound="none"
                ,underline="-1", )
        self.TNotebook1_t2.configure(background="#f0ffff")
        self.TNotebook1_t2.configure(highlightbackground="#f0ffff")
        self.TNotebook1_t2.configure(highlightcolor="black")
        self.TNotebook1_t3 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(3, text="Nurse", compound="none"
                ,underline="-1", )
        self.TNotebook1_t3.configure(background="#f0ffff")
        self.TNotebook1_t3.configure(highlightbackground="#f0ffff")
        self.TNotebook1_t3.configure(highlightcolor="black")
        self.TNotebook1_t4 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t4, padding=3)
        self.TNotebook1.tab(4, text="PatientRecords", compound="none"
                ,underline="-1", )
        self.TNotebook1_t4.configure(background="#f0ffff")
        self.TNotebook1_t4.configure(highlightbackground="#f0ffff")
        self.TNotebook1_t4.configure(highlightcolor="black")
        self.TNotebook1_t5 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t5, padding=3)
        self.TNotebook1.tab(5, text="Outputs", compound="none"
                ,underline="-1", )
        self.TNotebook1_t5.configure(background="#f0ffff")
        self.TNotebook1_t5.configure(highlightbackground="#f0ffff")
        self.TNotebook1_t5.configure(highlightcolor="black")
        

        self.Labelframe1 = LabelFrame(self.TNotebook1_t0)
        self.Labelframe1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font13)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Welcome, Please Add, Edit, Search and Delete patient details here:''')
        self.Labelframe1.configure(background="#f0ffff")
        self.Labelframe1.configure(highlightbackground="#f0ffff")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=150)

        self.Frame1 = Frame(self.Labelframe1)
        self.Frame1.place(relx=0.35, rely=0.04, relheight=0.95, relwidth=0.58)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#7ccd7c")
        self.Frame1.configure(highlightbackground="#7ccd7c")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=435)

# PFirstname stands for Patient firstname.This is needed as Other tables will have more firstnames
        self.PFirstnameEntry = Entry(self.Frame1)
        self.PFirstnameEntry.place(relx=0.34, rely=0.16, height=20
                , relwidth=0.38)
        self.PFirstnameEntry.configure(background="white")
        self.PFirstnameEntry.configure(disabledforeground="#a3a3a3")
        self.PFirstnameEntry.configure(font="TkFixedFont")
        self.PFirstnameEntry.configure(foreground="#000000")
        self.PFirstnameEntry.configure(highlightbackground="#7ccd7c")
        self.PFirstnameEntry.configure(highlightcolor="black")
        self.PFirstnameEntry.configure(insertbackground="black")
        self.PFirstnameEntry.configure(selectbackground="#c4c4c4")
        self.PFirstnameEntry.configure(selectforeground="black")

        self.PSurnameEntry = Entry(self.Frame1)
        self.PSurnameEntry.place(relx=0.34, rely=0.22,height=20, relwidth=0.38)
        self.PSurnameEntry.configure(background="white")
        self.PSurnameEntry.configure(disabledforeground="#a3a3a3")
        self.PSurnameEntry.configure(font=font10)
        self.PSurnameEntry.configure(foreground="#000000")
        self.PSurnameEntry.configure(highlightbackground="#7ccd7c")
        self.PSurnameEntry.configure(highlightcolor="black")
        self.PSurnameEntry.configure(insertbackground="black")
        self.PSurnameEntry.configure(selectbackground="#c4c4c4")
        self.PSurnameEntry.configure(selectforeground="black")

        self.PDateEntry = Entry(self.Frame1)
        self.PDateEntry.place(relx=0.34, rely=0.27,height=20, relwidth=0.08)
        self.PDateEntry.configure(background="white")
        self.PDateEntry.configure(disabledforeground="#a3a3a3")
        self.PDateEntry.configure(font="TkFixedFont")
        self.PDateEntry.configure(foreground="#000000")
        self.PDateEntry.configure(highlightbackground="#7ccd7c")
        self.PDateEntry.configure(highlightcolor="black")
        self.PDateEntry.configure(insertbackground="black")
        self.PDateEntry.configure(selectbackground="#c4c4c4")
        self.PDateEntry.configure(selectforeground="black")
        self.PDateEntry.configure(width=34)

        self.PMonthEntry = Entry(self.Frame1)
        self.PMonthEntry.place(relx=0.46, rely=0.27,height=20, relwidth=0.08)
        self.PMonthEntry.configure(background="white")
        self.PMonthEntry.configure(disabledforeground="#a3a3a3")
        self.PMonthEntry.configure(font="TkFixedFont")
        self.PMonthEntry.configure(foreground="#000000")
        self.PMonthEntry.configure(highlightbackground="#7ccd7c")
        self.PMonthEntry.configure(highlightcolor="black")
        self.PMonthEntry.configure(insertbackground="black")
        self.PMonthEntry.configure(selectbackground="#c4c4c4")
        self.PMonthEntry.configure(selectforeground="black")
        self.PMonthEntry.configure(width=34)

        self.PYearEntry = Entry(self.Frame1)
        self.PYearEntry.place(relx=0.57, rely=0.27,height=20, relwidth=0.15)
        self.PYearEntry.configure(background="white")
        self.PYearEntry.configure(disabledforeground="#a3a3a3")
        self.PYearEntry.configure(font="TkFixedFont")
        self.PYearEntry.configure(foreground="#000000")
        self.PYearEntry.configure(highlightbackground="#7ccd7c")
        self.PYearEntry.configure(highlightcolor="black")
        self.PYearEntry.configure(insertbackground="black")
        self.PYearEntry.configure(selectbackground="#c4c4c4")
        self.PYearEntry.configure(selectforeground="black")
        self.PYearEntry.configure(width=64)

        self.PAddressEntry = Entry(self.Frame1)
        self.PAddressEntry.place(relx=0.34, rely=0.317, height=20, relwidth=0.38)
        self.PAddressEntry.configure(background="white")
        self.PAddressEntry.configure(disabledforeground="#a3a3a3")
        self.PAddressEntry.configure(font="TkFixedFont")
        self.PAddressEntry.configure(foreground="#000000")
        self.PAddressEntry.configure(highlightbackground="#7ccd7c")
        self.PAddressEntry.configure(highlightcolor="black")
        self.PAddressEntry.configure(insertbackground="black")
        self.PAddressEntry.configure(selectbackground="#c4c4c4")
        self.PAddressEntry.configure(selectforeground="black")

        self.PPostcodeEntry = Entry(self.Frame1)
        self.PPostcodeEntry.place(relx=0.34, rely=0.37, height=20, relwidth=0.38)

        self.PPostcodeEntry.configure(background="white")
        self.PPostcodeEntry.configure(disabledforeground="#a3a3a3")
        self.PPostcodeEntry.configure(font="TkFixedFont")
        self.PPostcodeEntry.configure(foreground="#000000")
        self.PPostcodeEntry.configure(highlightbackground="#7ccd7c")
        self.PPostcodeEntry.configure(highlightcolor="black")
        self.PPostcodeEntry.configure(insertbackground="black")
        self.PPostcodeEntry.configure(selectbackground="#c4c4c4")
        self.PPostcodeEntry.configure(selectforeground="black")

        self.PMobileEntry = Entry(self.Frame1)
        self.PMobileEntry.place(relx=0.34, rely=0.425,height=20, relwidth=0.38)
        self.PMobileEntry.configure(background="white")
        self.PMobileEntry.configure(disabledforeground="#a3a3a3")
        self.PMobileEntry.configure(font="TkFixedFont")
        self.PMobileEntry.configure(foreground="#000000")
        self.PMobileEntry.configure(highlightbackground="#7ccd7c")
        self.PMobileEntry.configure(highlightcolor="black")
        self.PMobileEntry.configure(insertbackground="black")
        self.PMobileEntry.configure(selectbackground="#c4c4c4")
        self.PMobileEntry.configure(selectforeground="black")

        self.PTelephoneEntry = Entry(self.Frame1)
        self.PTelephoneEntry.place(relx=0.34, rely=0.475, height=20
                , relwidth=0.38)
        self.PTelephoneEntry.configure(background="white")
        self.PTelephoneEntry.configure(disabledforeground="#a3a3a3")
        self.PTelephoneEntry.configure(font="TkFixedFont")
        self.PTelephoneEntry.configure(foreground="#000000")
        self.PTelephoneEntry.configure(highlightbackground="#7ccd7c")
        self.PTelephoneEntry.configure(highlightcolor="black")
        self.PTelephoneEntry.configure(insertbackground="black")
        self.PTelephoneEntry.configure(selectbackground="#c4c4c4")
        self.PTelephoneEntry.configure(selectforeground="black")

        self.PEmailEntry = Entry(self.Frame1)
        self.PEmailEntry.place(relx=0.34, rely=0.52,height=20, relwidth=0.38)
        self.PEmailEntry.configure(background="white")
        self.PEmailEntry.configure(disabledforeground="#a3a3a3")
        self.PEmailEntry.configure(font="TkFixedFont")
        self.PEmailEntry.configure(foreground="#000000")
        self.PEmailEntry.configure(highlightbackground="#7ccd7c")
        self.PEmailEntry.configure(highlightcolor="black")
        self.PEmailEntry.configure(insertbackground="black")
        self.PEmailEntry.configure(selectbackground="#c4c4c4")
        self.PEmailEntry.configure(selectforeground="black")

        self.PrevPatientButton = Button(self.Frame1)
        self.PrevPatientButton.place(relx=0.18, rely=0.8, height=40, width=130)
        self.PrevPatientButton.configure(activebackground="#7ccd7c")
        self.PrevPatientButton.configure(activeforeground="#000000")
        self.PrevPatientButton.configure(background="#7ccd7c")
        self.PrevPatientButton.configure(disabledforeground="#a3a3a3")
        self.PrevPatientButton.configure(font=font13)
        self.PrevPatientButton.configure(foreground="#000000")
        self.PrevPatientButton.configure(highlightbackground="#7ccd7c")
        self.PrevPatientButton.configure(highlightcolor="black")
        self.PrevPatientButton.configure(pady="0")
        self.PrevPatientButton.configure(text='''Previous Patient''')
        self.PrevPatientButton.configure(width=130)

        self.NextPatientButton = Button(self.Frame1)
        self.NextPatientButton.place(relx=0.51, rely=0.8, height=40, width=115)
        self.NextPatientButton.configure(activebackground="#7ccd7c")
        self.NextPatientButton.configure(activeforeground="#000000")
        self.NextPatientButton.configure(background="#7ccd7c")
        self.NextPatientButton.configure(disabledforeground="#a3a3a3")
        self.NextPatientButton.configure(font=font13)
        self.NextPatientButton.configure(foreground="#000000")
        self.NextPatientButton.configure(highlightbackground="#7ccd7c")
        self.NextPatientButton.configure(highlightcolor="black")
        self.NextPatientButton.configure(pady="0")
        self.NextPatientButton.configure(text='''Next Patient''')
        self.NextPatientButton.configure(width=115)

        self.AddPatientButton = Button(self.Frame1)
        self.AddPatientButton.place(relx=0.05, rely=0.7, height=40, width=113)
        self.AddPatientButton.configure(activebackground="#7ccd7c")
        self.AddPatientButton.configure(activeforeground="#000000")
        self.AddPatientButton.configure(background="#fff5ee")
        self.AddPatientButton.configure(disabledforeground="#a3a3a3")
        self.AddPatientButton.configure(font=font13)
        self.AddPatientButton.configure(foreground="#000000")
        self.AddPatientButton.configure(highlightbackground="#7ccd7c")
        self.AddPatientButton.configure(highlightcolor="black")
        self.AddPatientButton.configure(pady="0")
        self.AddPatientButton.configure(text='''Add Patient Details''')
        self.AddPatientButton.configure(width=113,command=MeighPharmacyGUI_Functions.insertpatient)

        self.UpdatePatientButton = Button(self.Frame1,command=MeighPharmacyGUI_Functions.updatepatient)
        self.UpdatePatientButton.place(relx=0.32, rely=0.7, height=40, width=118)

        self.UpdatePatientButton.configure(activebackground="#7ccd7c")
        self.UpdatePatientButton.configure(activeforeground="#000000")
        self.UpdatePatientButton.configure(background="#7ccd7c")
        self.UpdatePatientButton.configure(disabledforeground="#a3a3a3")
        self.UpdatePatientButton.configure(font=font13)
        self.UpdatePatientButton.configure(foreground="#000000")
        self.UpdatePatientButton.configure(highlightbackground="#7ccd7c")
        self.UpdatePatientButton.configure(highlightcolor="black")
        self.UpdatePatientButton.configure(pady="0")
        self.UpdatePatientButton.configure(text='''Edit Patient Details''')
        self.UpdatePatientButton.configure(width=118)

        self.DeletePatientButton = Button(self.Frame1,command=MeighPharmacyGUI_Functions.deletepatient)
        self.DeletePatientButton.place(relx=0.62, rely=0.7, height=40, width=117)

        self.DeletePatientButton.configure(activebackground="#7ccd7c")
        self.DeletePatientButton.configure(activeforeground="#000000")
        self.DeletePatientButton.configure(background="#7ccd7c")
        self.DeletePatientButton.configure(disabledforeground="#a3a3a3")
        self.DeletePatientButton.configure(font=font13)
        self.DeletePatientButton.configure(foreground="#000000")
        self.DeletePatientButton.configure(highlightbackground="#7ccd7c")
        self.DeletePatientButton.configure(highlightcolor="black")
        self.DeletePatientButton.configure(pady="0")
        self.DeletePatientButton.configure(text='''Delete Patient Details''')
        self.DeletePatientButton.configure(width=117)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.05, rely=0.04, height=300, width=116)
        self.Label1.configure(background="#7ccd7c")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=("Segoe UI",10))
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Firstname:

Surname:

Date of Birth:

Address Line :

Postcode:

Mobile Number:

Telephone:

Email:''')
        
        #This is creating a widget for searching the patients
        self.Labelframe2 = LabelFrame(self.Labelframe1)
        self.Labelframe2.place(relx=0.01, rely=0.04, relheight=0.23
                , relwidth=0.34)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(font=font13)
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Enter the PatientID to in order to search''')
        self.Labelframe2.configure(background="#7ccd7c")
        self.Labelframe2.configure(highlightbackground="#7ccd7c")
        self.Labelframe2.configure(highlightcolor="black")
        self.Labelframe2.configure(width=250)

        self.PatientSearchEntry = Entry(self.Labelframe2)
        self.PatientSearchEntry.place(relx=0.16, rely=0.4, height=20
                , relwidth=0.66)
        self.PatientSearchEntry.configure(background="white")
        self.PatientSearchEntry.configure(disabledforeground="#a3a3a3")
        self.PatientSearchEntry.configure(font="TkFixedFont")
        self.PatientSearchEntry.configure(foreground="#000000")
        self.PatientSearchEntry.configure(highlightbackground="#7ccd7c")
        self.PatientSearchEntry.configure(highlightcolor="black")
        self.PatientSearchEntry.configure(insertbackground="black")
        self.PatientSearchEntry.configure(selectbackground="#c4c4c4")
        self.PatientSearchEntry.configure(selectforeground="black")

        self.SearchPatient = Button(self.Labelframe2,command=MeighPharmacyGUI_Functions.searchpatient)
        self.SearchPatient.place(relx=0.4, rely=0.64, height=30, width=63)
        self.SearchPatient.configure(activebackground="#7ccd7c")
        self.SearchPatient.configure(activeforeground="#000000")
        self.SearchPatient.configure(background="#7ccd7c")
        self.SearchPatient.configure(disabledforeground="#a3a3a3")
        self.SearchPatient.configure(font=font13)
        self.SearchPatient.configure(foreground="#000000")
        self.SearchPatient.configure(highlightbackground="#7ccd7c")
        self.SearchPatient.configure(highlightcolor="black")
        self.SearchPatient.configure(pady="0")
        self.SearchPatient.configure(text='''Submit''')

        self.Label21 = Label(self.Labelframe1)
        self.Label21.place(relx=0.01, rely=0.3, height=200, width=233)
        self.Label21.configure(background="#7ccd7c")
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        self._img1 = PhotoImage(file="Heart.png")
        self.Label21.configure(image=self._img1)
        self.Label21.configure(text='''Label''')
        self.Label21.configure(width=159)
        # code for Pharmacist tab
        self.Labelframe3 = LabelFrame(self.TNotebook1_t1)
        self.Labelframe3.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Labelframe3.configure(relief=GROOVE)
        self.Labelframe3.configure(font=font13)
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''Add, Edit, Search and Delete Pharmacist Details here''')
        self.Labelframe3.configure(background="#f0ffff")
        self.Labelframe3.configure(highlightbackground="#f0ffff")
        self.Labelframe3.configure(highlightcolor="black")
        self.Labelframe3.configure(width=150)

        self.Frame2 = Frame(self.Labelframe3)
        self.Frame2.place(relx=0.035, rely=0.04, relheight=0.95, relwidth=0.58)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#7ccd7c")
        self.Frame2.configure(highlightbackground="#7ccd7c")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=385)

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.05, rely=0.04, height=310, width=120)
        self.Label2.configure(activebackground="#7ccd7c")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#7ccd7c")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font13)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#7ccd7c")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Pharmacist Firstname:

Pharmacist Surname:

Address:

Postcode:

University:

Bachelors or Masters:''')
        
        self.PHFirstnameEntry = Entry(self.Frame2)
        self.PHFirstnameEntry.place(relx=0.36, rely=0.24, height=17
                , relwidth=0.35)
        self.PHFirstnameEntry.configure(background="white")
        self.PHFirstnameEntry.configure(disabledforeground="#a3a3a3")
        self.PHFirstnameEntry.configure(font="TkFixedFont")
        self.PHFirstnameEntry.configure(foreground="#000000")
        self.PHFirstnameEntry.configure(highlightbackground="#7ccd7c")
        self.PHFirstnameEntry.configure(highlightcolor="black")
        self.PHFirstnameEntry.configure(insertbackground="black")
        self.PHFirstnameEntry.configure(selectbackground="#c4c4c4")
        self.PHFirstnameEntry.configure(selectforeground="black")

        self.PHSurnameEntry = Entry(self.Frame2)
        self.PHSurnameEntry.place(relx=0.36, rely=0.28,height=17, relwidth=0.35)
        self.PHSurnameEntry.configure(background="white")
        self.PHSurnameEntry.configure(disabledforeground="#a3a3a3")
        self.PHSurnameEntry.configure(font="TkFixedFont")
        self.PHSurnameEntry.configure(foreground="#000000")
        self.PHSurnameEntry.configure(highlightbackground="#7ccd7c")
        self.PHSurnameEntry.configure(highlightcolor="black")
        self.PHSurnameEntry.configure(insertbackground="black")
        self.PHSurnameEntry.configure(selectbackground="#c4c4c4")
        self.PHSurnameEntry.configure(selectforeground="black")

        self.PHAddressEntry = Entry(self.Frame2)
        self.PHAddressEntry.place(relx=0.36, rely=0.33, height=17
                , relwidth=0.35)
        self.PHAddressEntry.configure(background="white")
        self.PHAddressEntry.configure(disabledforeground="#a3a3a3")
        self.PHAddressEntry.configure(font="TkFixedFont")
        self.PHAddressEntry.configure(foreground="#000000")
        self.PHAddressEntry.configure(highlightbackground="#7ccd7c")
        self.PHAddressEntry.configure(highlightcolor="black")
        self.PHAddressEntry.configure(insertbackground="black")
        self.PHAddressEntry.configure(selectbackground="#c4c4c4")
        self.PHAddressEntry.configure(selectforeground="black")

        self.PHPostcodeEntry = Entry(self.Frame2)
        self.PHPostcodeEntry.place(relx=0.36, rely=0.382, height=17
                , relwidth=0.35)
        self.PHPostcodeEntry.configure(background="white")
        self.PHPostcodeEntry.configure(disabledforeground="#a3a3a3")
        self.PHPostcodeEntry.configure(font="TkFixedFont")
        self.PHPostcodeEntry.configure(foreground="#000000")
        self.PHPostcodeEntry.configure(highlightbackground="#7ccd7c")
        self.PHPostcodeEntry.configure(highlightcolor="black")
        self.PHPostcodeEntry.configure(insertbackground="black")
        self.PHPostcodeEntry.configure(selectbackground="#c4c4c4")
        self.PHPostcodeEntry.configure(selectforeground="black")

        self.PHUniversityEntry = Entry(self.Frame2)
        self.PHUniversityEntry.place(relx=0.36, rely=0.425, height=17
                , relwidth=0.35)
        self.PHUniversityEntry.configure(background="white")
        self.PHUniversityEntry.configure(disabledforeground="#a3a3a3")
        self.PHUniversityEntry.configure(font="TkFixedFont")
        self.PHUniversityEntry.configure(foreground="#000000")
        self.PHUniversityEntry.configure(highlightbackground="#7ccd7c")
        self.PHUniversityEntry.configure(highlightcolor="black")
        self.PHUniversityEntry.configure(insertbackground="black")
        self.PHUniversityEntry.configure(selectbackground="#c4c4c4")
        self.PHUniversityEntry.configure(selectforeground="black")

        self.PHBorMEntry = Entry(self.Frame2)
        self.PHBorMEntry.place(relx=0.36, rely=0.475, height=17
                , relwidth=0.35)
        self.PHBorMEntry.configure(background="white")
        self.PHBorMEntry.configure(disabledforeground="#a3a3a3")
        self.PHBorMEntry.configure(font="TkFixedFont")
        self.PHBorMEntry.configure(foreground="#000000")
        self.PHBorMEntry.configure(highlightbackground="#7ccd7c")
        self.PHBorMEntry.configure(highlightcolor="black")
        self.PHBorMEntry.configure(insertbackground="black")
        self.PHBorMEntry.configure(selectbackground="#c4c4c4")
        self.PHBorMEntry.configure(selectforeground="black")

        self.PreviousPharmacistButton = Button(self.Frame2)
        self.PreviousPharmacistButton.place(relx=0.13, rely=0.85, height=30
                , width=130)
        self.PreviousPharmacistButton.configure(activebackground="#7ccd7c")
        self.PreviousPharmacistButton.configure(activeforeground="#000000")
        self.PreviousPharmacistButton.configure(background="#7ccd7c")
        self.PreviousPharmacistButton.configure(disabledforeground="#a3a3a3")
        self.PreviousPharmacistButton.configure(font=font13)
        self.PreviousPharmacistButton.configure(foreground="#000000")
        self.PreviousPharmacistButton.configure(highlightbackground="#7ccd7c")
        self.PreviousPharmacistButton.configure(highlightcolor="black")
        self.PreviousPharmacistButton.configure(pady="0")
        self.PreviousPharmacistButton.configure(text='''Previous Pharmacist''')
        self.PreviousPharmacistButton.configure(width=130)

        self.NextPharmacistButton = Button(self.Frame2)
        self.NextPharmacistButton.place(relx=0.49, rely=0.85, height=30, width=135)
        self.NextPharmacistButton.configure(activebackground="#7ccd7c")
        self.NextPharmacistButton.configure(activeforeground="#000000")
        self.NextPharmacistButton.configure(background="#7ccd7c")
        self.NextPharmacistButton.configure(disabledforeground="#a3a3a3")
        self.NextPharmacistButton.configure(font=font13)
        self.NextPharmacistButton.configure(foreground="#000000")
        self.NextPharmacistButton.configure(highlightbackground="#7ccd7c")
        self.NextPharmacistButton.configure(highlightcolor="black")
        self.NextPharmacistButton.configure(pady="0")
        self.NextPharmacistButton.configure(text='''Next Pharmacist''')
        self.NextPharmacistButton.configure(width=135)

        self.AddPharmacistButton = Button(self.Frame2,command=MeighPharmacyGUI_Functions.insertpharmacist)
        self.AddPharmacistButton.place(relx=0.05, rely=0.74, height=40, width=96)
        self.AddPharmacistButton.configure(activebackground="#7ccd7c")
        self.AddPharmacistButton.configure(activeforeground="#000000")
        self.AddPharmacistButton.configure(background="#7ccd7c")
        self.AddPharmacistButton.configure(disabledforeground="#a3a3a3")
        self.AddPharmacistButton.configure(font=font13)
        self.AddPharmacistButton.configure(foreground="#000000")
        self.AddPharmacistButton.configure(highlightbackground="#7ccd7c")
        self.AddPharmacistButton.configure(highlightcolor="black")
        self.AddPharmacistButton.configure(pady="0")
        self.AddPharmacistButton.configure(text='''Add pharmacist''')
        self.AddPharmacistButton.configure(width=96)

        self.UpdatePharmacistButton = Button(self.Frame2,command=MeighPharmacyGUI_Functions.editpharmacist)
        self.UpdatePharmacistButton.place(relx=0.31, rely=0.74, height=40
                , width=118)
        self.UpdatePharmacistButton.configure(activebackground="#7ccd7c")
        self.UpdatePharmacistButton.configure(activeforeground="#000000")
        self.UpdatePharmacistButton.configure(background="#7ccd7c")
        self.UpdatePharmacistButton.configure(disabledforeground="#a3a3a3")
        self.UpdatePharmacistButton.configure(font=font13)
        self.UpdatePharmacistButton.configure(foreground="#000000")
        self.UpdatePharmacistButton.configure(highlightbackground="#7ccd7c")
        self.UpdatePharmacistButton.configure(highlightcolor="black")
        self.UpdatePharmacistButton.configure(pady="0")
        self.UpdatePharmacistButton.configure(text='''Edit Pharmacist''')
        self.UpdatePharmacistButton.configure(width=118)

        self.DeletePharmacistButton = Button(self.Frame2,command=MeighPharmacyGUI_Functions.deletepharmacist)
        self.DeletePharmacistButton.place(relx=0.65, rely=0.74, height=40
                , width=113)
        self.DeletePharmacistButton.configure(activebackground="#7ccd7c")
        self.DeletePharmacistButton.configure(activeforeground="#000000")
        self.DeletePharmacistButton.configure(background="#7ccd7c")
        self.DeletePharmacistButton.configure(disabledforeground="#a3a3a3")
        self.DeletePharmacistButton.configure(font=font13)
        self.DeletePharmacistButton.configure(foreground="#000000")
        self.DeletePharmacistButton.configure(highlightbackground="#7ccd7c")
        self.DeletePharmacistButton.configure(highlightcolor="black")
        self.DeletePharmacistButton.configure(pady="0")
        self.DeletePharmacistButton.configure(text='''Delete Pharmacist''')
        self.DeletePharmacistButton.configure(width=113)

        self.Labelframe4 = LabelFrame(self.Labelframe3)
        self.Labelframe4.place(relx=0.62, rely=0.33, relheight=0.19
                , relwidth=0.38)
        self.Labelframe4.configure(relief=GROOVE)
        self.Labelframe4.configure(font=font13)
        self.Labelframe4.configure(foreground="black")
        self.Labelframe4.configure(text='''Enter the ID of the Pharmacist you wish to search:''')
        self.Labelframe4.configure(background="#7ccd7c")
        self.Labelframe4.configure(highlightbackground="#7ccd7c")
        self.Labelframe4.configure(highlightcolor="black")
        self.Labelframe4.configure(width=280)

        self.SearchPharmacistEntry = Entry(self.Labelframe4)
        self.SearchPharmacistEntry.place(relx=0.18, rely=0.29, height=20
                , relwidth=0.59)
        self.SearchPharmacistEntry.configure(background="white")
        self.SearchPharmacistEntry.configure(disabledforeground="#a3a3a3")
        self.SearchPharmacistEntry.configure(font="TkFixedFont")
        self.SearchPharmacistEntry.configure(foreground="#000000")
        self.SearchPharmacistEntry.configure(highlightbackground="#7ccd7c")
        self.SearchPharmacistEntry.configure(highlightcolor="black")
        self.SearchPharmacistEntry.configure(insertbackground="black")
        self.SearchPharmacistEntry.configure(selectbackground="#c4c4c4")
        self.SearchPharmacistEntry.configure(selectforeground="black")

        self.SearchPharmacistButton = Button(self.Labelframe4,command=MeighPharmacyGUI_Functions.searchpharmacist)
        self.SearchPharmacistButton.place(relx=0.39, rely=0.57, height=30, width=64)

        self.SearchPharmacistButton.configure(activebackground="#7ccd7c")
        self.SearchPharmacistButton.configure(activeforeground="#000000")
        self.SearchPharmacistButton.configure(background="#7ccd7c")
        self.SearchPharmacistButton.configure(disabledforeground="#a3a3a3")
        self.SearchPharmacistButton.configure(font=font13)
        self.SearchPharmacistButton.configure(foreground="#000000")
        self.SearchPharmacistButton.configure(highlightbackground="#7ccd7c")
        self.SearchPharmacistButton.configure(highlightcolor="black")
        self.SearchPharmacistButton.configure(pady="0")
        self.SearchPharmacistButton.configure(text='''Search''')
        #Code for Bookings Tab
        self.Labelframe5 = LabelFrame(self.TNotebook1_t2)
        self.Labelframe5.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Labelframe5.configure(relief=GROOVE)
        self.Labelframe5.configure(font=font13)
        self.Labelframe5.configure(foreground="black")
        self.Labelframe5.configure(text='''Add, Edit, Search and Delete Bookings here:''')
        self.Labelframe5.configure(background="#f0ffff")
        self.Labelframe5.configure(width=150)

        self.Frame3 = Frame(self.Labelframe5)
        self.Frame3.place(relx=0.01, rely=0.07, relheight=0.9, relwidth=0.49)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="#7ccd7c")
        self.Frame3.configure(width=365)

        self.Label3 = Label(self.Frame3)
        self.Label3.place(relx=0.03, rely=0.14, height=168, width=151)
        self.Label3.configure(background="#7ccd7c")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font13)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Patient ID:

Pharmacist ID:

Nurse ID:

Date:

Time:
                              
Booking Type''')

        self.BPatientIDEntry = Entry(self.Frame3)
        self.BPatientIDEntry.place(relx=0.47, rely=0.195, height=15
                , relwidth=0.45)
        self.BPatientIDEntry.configure(background="white")
        self.BPatientIDEntry.configure(disabledforeground="#a3a3a3")
        self.BPatientIDEntry.configure(font=font10)
        self.BPatientIDEntry.configure(foreground="#000000")
        self.BPatientIDEntry.configure(insertbackground="black")

        self.BPharmacistIDEntry = Entry(self.Frame3)
        self.BPharmacistIDEntry.place(relx=0.47, rely=0.2355, height=15, relwidth=0.45)
        self.BPharmacistIDEntry.configure(background="white")
        self.BPharmacistIDEntry.configure(disabledforeground="#a3a3a3")
        self.BPharmacistIDEntry.configure(font=font10)
        self.BPharmacistIDEntry.configure(foreground="#000000")
        self.BPharmacistIDEntry.configure(insertbackground="black")

        self.BNurseIDEntry = Entry(self.Frame3)
        self.BNurseIDEntry.place(relx=0.47, rely=0.29, height=15
                , relwidth=0.45)
        self.BNurseIDEntry.configure(background="white")
        self.BNurseIDEntry.configure(disabledforeground="#a3a3a3")
        self.BNurseIDEntry.configure(font=font10)
        self.BNurseIDEntry.configure(foreground="#000000")
        self.BNurseIDEntry.configure(insertbackground="black")

        self.BDateEntry = Entry(self.Frame3)
        self.BDateEntry.place(relx=0.47, rely=0.335,height=15, relwidth=0.09)
        self.BDateEntry.configure(background="white")
        self.BDateEntry.configure(disabledforeground="#a3a3a3")
        self.BDateEntry.configure(font=font10)
        self.BDateEntry.configure(foreground="#000000")
        self.BDateEntry.configure(insertbackground="black")
        self.BDateEntry.configure(width=34)

        self.BMonthEntry = Entry(self.Frame3)
        self.BMonthEntry.place(relx=0.58, rely=0.335,height=15, relwidth=0.09)
        self.BMonthEntry.configure(background="white")
        self.BMonthEntry.configure(disabledforeground="#a3a3a3")
        self.BMonthEntry.configure(font=font10)
        self.BMonthEntry.configure(foreground="#000000")
        self.BMonthEntry.configure(insertbackground="black")
        self.BMonthEntry.configure(width=34)

        self.BYearEntry = Entry(self.Frame3)
        self.BYearEntry.place(relx=0.68, rely=0.335,height=15, relwidth=0.18)
        self.BYearEntry.configure(background="white")
        self.BYearEntry.configure(disabledforeground="#a3a3a3")
        self.BYearEntry.configure(font=font10)
        self.BYearEntry.configure(foreground="#000000")
        self.BYearEntry.configure(insertbackground="black")
        self.BYearEntry.configure(width=64)

        self.BHourEntry = Entry(self.Frame3)
        self.BHourEntry.place(relx=0.47, rely=0.385,height=15, relwidth=0.15)
        self.BHourEntry.configure(background="white")
        self.BHourEntry.configure(disabledforeground="#a3a3a3")
        self.BHourEntry.configure(font=font10)
        self.BHourEntry.configure(foreground="#000000")
        self.BHourEntry.configure(insertbackground="black")
        self.BHourEntry.configure(width=54)

        self.BMinuteEntry = Entry(self.Frame3)
        self.BMinuteEntry.place(relx=0.63, rely=0.385,height=15, relwidth=0.18)
        self.BMinuteEntry.configure(background="white")
        self.BMinuteEntry.configure(disabledforeground="#a3a3a3")
        self.BMinuteEntry.configure(font=font10)
        self.BMinuteEntry.configure(foreground="#000000")
        self.BMinuteEntry.configure(insertbackground="black")
        self.BMinuteEntry.configure(width=64)

        self.BookingTypeEntry = Entry(self.Frame3)
        self.BookingTypeEntry.place(relx=0.47, rely=0.44,height=15, relwidth=0.18)
        self.BookingTypeEntry.configure(background="white")
        self.BookingTypeEntry.configure(disabledforeground="#a3a3a3")
        self.BookingTypeEntry.configure(font=font10)
        self.BookingTypeEntry.configure(foreground="#000000")
        self.BookingTypeEntry.configure(insertbackground="black")
        self.BookingTypeEntry.configure(width=64)

        self.PreviousBookingButton = Button(self.Frame3)
        self.PreviousBookingButton.place(relx=0.05, rely=0.83, height=30
                , width=130)
        self.PreviousBookingButton.configure(activebackground="#7ccd7c")
        self.PreviousBookingButton.configure(activeforeground="#000000")
        self.PreviousBookingButton.configure(background="#7ccd7c")
        self.PreviousBookingButton.configure(disabledforeground="#a3a3a3")
        self.PreviousBookingButton.configure(font=font13)
        self.PreviousBookingButton.configure(foreground="#000000")
        self.PreviousBookingButton.configure(highlightbackground="#7ccd7c")
        self.PreviousBookingButton.configure(highlightcolor="black")
        self.PreviousBookingButton.configure(pady="0")
        self.PreviousBookingButton.configure(text='''Previous Booking''')

        self.NextBookingButton = Button(self.Frame3)
        self.NextBookingButton.place(relx=0.55, rely=0.83, height=30
                , width=100)
        self.NextBookingButton.configure(activebackground="#7ccd7c")
        self.NextBookingButton.configure(activeforeground="#000000")
        self.NextBookingButton.configure(background="#7ccd7c")
        self.NextBookingButton.configure(disabledforeground="#a3a3a3")
        self.NextBookingButton.configure(font=font13)
        self.NextBookingButton.configure(foreground="#000000")
        self.NextBookingButton.configure(highlightbackground="#7ccd7c")
        self.NextBookingButton.configure(highlightcolor="black")
        self.NextBookingButton.configure(pady="0")
        self.NextBookingButton.configure(text='''Next Booking''')

        self.AddBookingButton = Button(self.Frame3,command=MeighPharmacyGUI_Functions.addbooking)
        self.AddBookingButton.place(relx=0.05, rely=0.51, height=30
                , width=135)
        self.AddBookingButton.configure(activebackground="#7ccd7c")
        self.AddBookingButton.configure(activeforeground="#000000")
        self.AddBookingButton.configure(background="#7ccd7c")
        self.AddBookingButton.configure(disabledforeground="#a3a3a3")
        self.AddBookingButton.configure(font=font13)
        self.AddBookingButton.configure(foreground="#000000")
        self.AddBookingButton.configure(highlightbackground="#7ccd7c")
        self.AddBookingButton.configure(highlightcolor="black")
        self.AddBookingButton.configure(pady="0")
        self.AddBookingButton.configure(text='''Add Booking''')

        self.UpdateBookingButton = Button(self.Frame3,command=MeighPharmacyGUI_Functions.editbooking)
        self.UpdateBookingButton.place(relx=0.05, rely=0.59, height=30
                , width=157)
        self.UpdateBookingButton.configure(activebackground="#7ccd7c")
        self.UpdateBookingButton.configure(activeforeground="#000000")
        self.UpdateBookingButton.configure(background="#7ccd7c")
        self.UpdateBookingButton.configure(disabledforeground="#a3a3a3")
        self.UpdateBookingButton.configure(font=font13)
        self.UpdateBookingButton.configure(foreground="#000000")
        self.UpdateBookingButton.configure(highlightbackground="#7ccd7c")
        self.UpdateBookingButton.configure(highlightcolor="black")
        self.UpdateBookingButton.configure(pady="0")
        self.UpdateBookingButton.configure(text='''Update Booking''')

        self.DeleteBookingButton = Button(self.Frame3,command=MeighPharmacyGUI_Functions.deletebooking)
        self.DeleteBookingButton.place(relx=0.05, rely=0.67, height=30
                , width=152)
        self.DeleteBookingButton.configure(activebackground="#7ccd7c")
        self.DeleteBookingButton.configure(activeforeground="#000000")
        self.DeleteBookingButton.configure(background="#7ccd7c")
        self.DeleteBookingButton.configure(disabledforeground="#a3a3a3")
        self.DeleteBookingButton.configure(font=font13)
        self.DeleteBookingButton.configure(foreground="#000000")
        self.DeleteBookingButton.configure(highlightbackground="#7ccd7c")
        self.DeleteBookingButton.configure(highlightcolor="black")
        self.DeleteBookingButton.configure(pady="0")
        self.DeleteBookingButton.configure(text='''Delete Booking''')

        self.Labelframe6 = LabelFrame(self.Labelframe5)
        self.Labelframe6.place(relx=0.54, rely=0.31, relheight=0.19
                , relwidth=0.4)
        self.Labelframe6.configure(relief=GROOVE)
        self.Labelframe6.configure(font=font13)
        self.Labelframe6.configure(foreground="black")
        self.Labelframe6.configure(text='''Enter the ID of the Booking to search''')
        self.Labelframe6.configure(background="#7ccd7c")
        self.Labelframe6.configure(width=300)

        self.BookingSearchEntry = Entry(self.Labelframe6)
        self.BookingSearchEntry.place(relx=0.23, rely=0.29, height=20
                , relwidth=0.55)
        self.BookingSearchEntry.configure(background="white")
        self.BookingSearchEntry.configure(disabledforeground="#a3a3a3")
        self.BookingSearchEntry.configure(font=font10)
        self.BookingSearchEntry.configure(foreground="#000000")
        self.BookingSearchEntry.configure(insertbackground="black")

        self.BookingSearchButton = Button(self.Labelframe6,command=MeighPharmacyGUI_Functions.searchbooking)
        self.BookingSearchButton.place(relx=0.4, rely=0.57, height=30
                , width=68)
        self.BookingSearchButton.configure(activebackground="#7ccd7c")
        self.BookingSearchButton.configure(activeforeground="#000000")
        self.BookingSearchButton.configure(background="#7ccd7c")
        self.BookingSearchButton.configure(disabledforeground="#a3a3a3")
        self.BookingSearchButton.configure(font=font13)
        self.BookingSearchButton.configure(foreground="#000000")
        self.BookingSearchButton.configure(highlightbackground="#7ccd7c")
        self.BookingSearchButton.configure(highlightcolor="black")
        self.BookingSearchButton.configure(pady="0")
        self.BookingSearchButton.configure(text='''Search''')
        self.BookingSearchButton.configure(width=68)
        #Code for Nurse Tab
        self.Labelframe7 = LabelFrame(self.TNotebook1_t3)
        self.Labelframe7.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Labelframe7.configure(relief=GROOVE)
        self.Labelframe7.configure(font=font13)
        self.Labelframe7.configure(foreground="black")
        self.Labelframe7.configure(text='''Add, Edit, Search and Delete Nurse Details here:''')
        self.Labelframe7.configure(background="#f0ffff")
        self.Labelframe7.configure(width=150)

        self.Frame4 = Frame(self.Labelframe7)
        self.Frame4.place(relx=0.01, rely=0.05, relheight=0.92, relwidth=0.5)
        self.Frame4.configure(relief=GROOVE)
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief=GROOVE)
        self.Frame4.configure(background="#7ccd7c")
        self.Frame4.configure(width=375)

        self.Label4 = Label(self.Frame4)
        self.Label4.place(relx=0.03, rely=0.06, height=170, width=136)
        self.Label4.configure(background="#7ccd7c")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font13)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Firstname:

Surname:

Address:

Postcode:
                              
Mobile
                              
Start Date
                              
Medical School''')
        
        self.NFirstnameEntry = Entry(self.Frame4)
        self.NFirstnameEntry.place(relx=0.43, rely=0.085, height=15
                , relwidth=0.44)
        self.NFirstnameEntry.configure(background="white")
        self.NFirstnameEntry.configure(disabledforeground="#a3a3a3")
        self.NFirstnameEntry.configure(font=font10)
        self.NFirstnameEntry.configure(foreground="#000000")
        self.NFirstnameEntry.configure(insertbackground="black")

        self.NSurnameEntry = Entry(self.Frame4)
        self.NSurnameEntry.place(relx=0.43, rely=0.135, height=15
                , relwidth=0.44)
        self.NSurnameEntry.configure(background="white")
        self.NSurnameEntry.configure(disabledforeground="#a3a3a3")
        self.NSurnameEntry.configure(font=font10)
        self.NSurnameEntry.configure(foreground="#000000")
        self.NSurnameEntry.configure(insertbackground="black")

        self.NAddressEntry = Entry(self.Frame4)
        self.NAddressEntry.place(relx=0.43, rely=0.185,height=15, relwidth=0.44)
        self.NAddressEntry.configure(background="white")
        self.NAddressEntry.configure(disabledforeground="#a3a3a3")
        self.NAddressEntry.configure(font=font10)
        self.NAddressEntry.configure(foreground="#000000")
        self.NAddressEntry.configure(insertbackground="black")

        self.NPostcodeEntry = Entry(self.Frame4)
        self.NPostcodeEntry.place(relx=0.43, rely=0.236,height=15, relwidth=0.44)
        self.NPostcodeEntry.configure(background="white")
        self.NPostcodeEntry.configure(disabledforeground="#a3a3a3")
        self.NPostcodeEntry.configure(font=font10)
        self.NPostcodeEntry.configure(foreground="#000000")
        self.NPostcodeEntry.configure(insertbackground="black")

        self.NMobileEntry = Entry(self.Frame4)
        self.NMobileEntry.place(relx=0.43, rely=0.28,height=15, relwidth=0.44)
        self.NMobileEntry.configure(background="white")
        self.NMobileEntry.configure(disabledforeground="#a3a3a3")
        self.NMobileEntry.configure(font=font10)
        self.NMobileEntry.configure(foreground="#000000")
        self.NMobileEntry.configure(insertbackground="black")

        self.NStartDateEntry = Entry(self.Frame4)
        self.NStartDateEntry.place(relx=0.43, rely=0.33,height=15, relwidth=0.08)
        self.NStartDateEntry.configure(background="white")
        self.NStartDateEntry.configure(disabledforeground="#a3a3a3")
        self.NStartDateEntry.configure(font=font10)
        self.NStartDateEntry.configure(foreground="#000000")
        self.NStartDateEntry.configure(insertbackground="black")

        self.NStartMonthEntry = Entry(self.Frame4)
        self.NStartMonthEntry.place(relx=0.55, rely=0.33,height=15, relwidth=0.08)
        self.NStartMonthEntry.configure(background="white")
        self.NStartMonthEntry.configure(disabledforeground="#a3a3a3")
        self.NStartMonthEntry.configure(font=font10)
        self.NStartMonthEntry.configure(foreground="#000000")
        self.NStartMonthEntry.configure(insertbackground="black")

        self.NStartYearEntry = Entry(self.Frame4)
        self.NStartYearEntry.place(relx=0.67, rely=0.33,height=15, relwidth=0.18)
        self.NStartYearEntry.configure(background="white")
        self.NStartYearEntry.configure(disabledforeground="#a3a3a3")
        self.NStartYearEntry.configure(font=font10)
        self.NStartYearEntry.configure(foreground="#000000")
        self.NStartYearEntry.configure(insertbackground="black")

        self.NMedicalSchoolEntry = Entry(self.Frame4)
        self.NMedicalSchoolEntry.place(relx=0.43, rely=0.38,height=15, relwidth=0.44)
        self.NMedicalSchoolEntry.configure(background="white")
        self.NMedicalSchoolEntry.configure(disabledforeground="#a3a3a3")
        self.NMedicalSchoolEntry.configure(font=font10)
        self.NMedicalSchoolEntry.configure(foreground="#000000")
        self.NMedicalSchoolEntry.configure(insertbackground="black")

        self.PreviousNurseButton = Button(self.Frame4)
        self.PreviousNurseButton.place(relx=0.03, rely=0.83, height=30
                , width=130)
        self.PreviousNurseButton.configure(activebackground="#7ccd7c")
        self.PreviousNurseButton.configure(activeforeground="#000000")
        self.PreviousNurseButton.configure(background="#7ccd7c")
        self.PreviousNurseButton.configure(disabledforeground="#a3a3a3")
        self.PreviousNurseButton.configure(font=font13)
        self.PreviousNurseButton.configure(foreground="#000000")
        self.PreviousNurseButton.configure(highlightbackground="#7ccd7c")
        self.PreviousNurseButton.configure(highlightcolor="black")
        self.PreviousNurseButton.configure(pady="0")
        self.PreviousNurseButton.configure(text='''Previous Nurse''')

        self.NextNurseButton = Button(self.Frame4)
        self.NextNurseButton.place(relx=0.43, rely=0.83, height=30
                , width=100)
        self.NextNurseButton.configure(activebackground="#7ccd7c")
        self.NextNurseButton.configure(activeforeground="#000000")
        self.NextNurseButton.configure(background="#7ccd7c")
        self.NextNurseButton.configure(disabledforeground="#a3a3a3")
        self.NextNurseButton.configure(font=font13)
        self.NextNurseButton.configure(foreground="#000000")
        self.NextNurseButton.configure(highlightbackground="#7ccd7c")
        self.NextNurseButton.configure(highlightcolor="black")
        self.NextNurseButton.configure(pady="0")
        self.NextNurseButton.configure(text='''Next Nurse''')

        self.AddNurseButton = Button(self.Frame4,command=MeighPharmacyGUI_Functions.addnurse)
        self.AddNurseButton.place(relx=0.03, rely=0.58, height=30
                , width=195)
        self.AddNurseButton.configure(activebackground="#7ccd7c")
        self.AddNurseButton.configure(activeforeground="#000000")
        self.AddNurseButton.configure(background="#7ccd7c")
        self.AddNurseButton.configure(disabledforeground="#a3a3a3")
        self.AddNurseButton.configure(font=font13)
        self.AddNurseButton.configure(foreground="#000000")
        self.AddNurseButton.configure(highlightbackground="#7ccd7c")
        self.AddNurseButton.configure(highlightcolor="black")
        self.AddNurseButton.configure(pady="0")
        self.AddNurseButton.configure(text='''Add Nurse''')

        self.EditNurseButton = Button(self.Frame4,command=MeighPharmacyGUI_Functions.editnurse)
        self.EditNurseButton.place(relx=0.03, rely=0.66, height=30
                , width=195)
        self.EditNurseButton.configure(activebackground="#7ccd7c")
        self.EditNurseButton.configure(activeforeground="#000000")
        self.EditNurseButton.configure(background="#7ccd7c")
        self.EditNurseButton.configure(disabledforeground="#a3a3a3")
        self.EditNurseButton.configure(font=font13)
        self.EditNurseButton.configure(foreground="#000000")
        self.EditNurseButton.configure(highlightbackground="#7ccd7c")
        self.EditNurseButton.configure(highlightcolor="black")
        self.EditNurseButton.configure(pady="0")
        self.EditNurseButton.configure(text='''Edit Nurse''')

        self.DeleteNurseButton = Button(self.Frame4,command=MeighPharmacyGUI_Functions.deletenurse)
        self.DeleteNurseButton.place(relx=0.03, rely=0.74, height=30
                , width=195)
        self.DeleteNurseButton.configure(activebackground="#7ccd7c")
        self.DeleteNurseButton.configure(activeforeground="#000000")
        self.DeleteNurseButton.configure(background="#7ccd7c")
        self.DeleteNurseButton.configure(disabledforeground="#a3a3a3")
        self.DeleteNurseButton.configure(font=font13)
        self.DeleteNurseButton.configure(foreground="#000000")
        self.DeleteNurseButton.configure(highlightbackground="#7ccd7c")
        self.DeleteNurseButton.configure(highlightcolor="black")
        self.DeleteNurseButton.configure(pady="0")
        self.DeleteNurseButton.configure(text='''Delete Nurse''')

        self.Labelframe8 = LabelFrame(self.Labelframe7)
        self.Labelframe8.place(relx=0.56, rely=0.31, relheight=0.21
                , relwidth=0.34)
        self.Labelframe8.configure(relief=GROOVE)
        self.Labelframe8.configure(font=font13)
        self.Labelframe8.configure(foreground="black")
        self.Labelframe8.configure(text='''Enter the ID of the Nurse to search:''')
        self.Labelframe8.configure(background="#7ccd7c")
        self.Labelframe8.configure(width=250)

        self.SearchNurseEntry = Entry(self.Labelframe8)
        self.SearchNurseEntry.place(relx=0.16, rely=0.35, height=20
                , relwidth=0.66)
        self.SearchNurseEntry.configure(background="white")
        self.SearchNurseEntry.configure(disabledforeground="#a3a3a3")
        self.SearchNurseEntry.configure(font=font10)
        self.SearchNurseEntry.configure(foreground="#000000")
        self.SearchNurseEntry.configure(insertbackground="black")

        self.SearchNurseButton = Button(self.Labelframe8,command=MeighPharmacyGUI_Functions.searchnurse)
        self.SearchNurseButton.place(relx=0.36, rely=0.61, height=30
                , width=64)
        self.SearchNurseButton.configure(activebackground="#7ccd7c")
        self.SearchNurseButton.configure(activeforeground="#000000")
        self.SearchNurseButton.configure(background="#7ccd7c")
        self.SearchNurseButton.configure(disabledforeground="#a3a3a3")
        self.SearchNurseButton.configure(font=font13)
        self.SearchNurseButton.configure(foreground="#000000")
        self.SearchNurseButton.configure(highlightbackground="#7ccd7c")
        self.SearchNurseButton.configure(highlightcolor="black")
        self.SearchNurseButton.configure(pady="0")
        self.SearchNurseButton.configure(text='''Search''')
        #Code for Patient Records
        self.Labelframe9 = LabelFrame(self.TNotebook1_t4)
        self.Labelframe9.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Labelframe9.configure(relief=GROOVE)
        self.Labelframe9.configure(font=font13)
        self.Labelframe9.configure(foreground="black")
        self.Labelframe9.configure(text='''Add, Edit, Search and Delete Patient Records here:''')
        self.Labelframe9.configure(background="#f0ffff")
        self.Labelframe9.configure(width=150)

        self.Frame5 = Frame(self.Labelframe9)
        self.Frame5.place(relx=0.01, rely=0.05, relheight=0.92, relwidth=0.54)
        self.Frame5.configure(relief=GROOVE)
        self.Frame5.configure(borderwidth="2")
        self.Frame5.configure(relief=GROOVE)
        self.Frame5.configure(background="#7ccd7c")
        self.Frame5.configure(width=405)

        self.Label5 = Label(self.Frame5)
        self.Label5.place(relx=0, rely=0.02, height=204, width=220)
        self.Label5.configure(background="#7ccd7c")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font13)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(justify=LEFT)
        self.Label5.configure(text='''Record ID:

Patient ID:

Date of Record:

Diagnosis:

Severity:

Date of Last Appointment:''')
        
        self.RecordIDEntry = Entry(self.Frame5)
        self.RecordIDEntry.place(relx=0.5, rely=0.11,height=15, relwidth=0.4)
        self.RecordIDEntry.configure(background="white")
        self.RecordIDEntry.configure(disabledforeground="#a3a3a3")
        self.RecordIDEntry.configure(font=font10)
        self.RecordIDEntry.configure(foreground="#000000")
        self.RecordIDEntry.configure(insertbackground="black")

        self.RPatientIDEntry = Entry(self.Frame5)
        self.RPatientIDEntry.place(relx=0.5, rely=0.155, height=15, relwidth=0.4)
        self.RPatientIDEntry.configure(background="white")
        self.RPatientIDEntry.configure(disabledforeground="#a3a3a3")
        self.RPatientIDEntry.configure(font=font10)
        self.RPatientIDEntry.configure(foreground="#000000")
        self.RPatientIDEntry.configure(insertbackground="black")

        self.RDateEntry = Entry(self.Frame5)
        self.RDateEntry.place(relx=0.5, rely=0.2,height=15, relwidth=0.11)
        self.RDateEntry.configure(background="white")
        self.RDateEntry.configure(disabledforeground="#a3a3a3")
        self.RDateEntry.configure(font=font10)
        self.RDateEntry.configure(foreground="#000000")
        self.RDateEntry.configure(insertbackground="black")
        self.RDateEntry.configure(width=44)

        self.RMonthEntry = Entry(self.Frame5)
        self.RMonthEntry.place(relx=0.65, rely=0.2,height=15, relwidth=0.11)
        self.RMonthEntry.configure(background="white")
        self.RMonthEntry.configure(disabledforeground="#a3a3a3")
        self.RMonthEntry.configure(font=font10)
        self.RMonthEntry.configure(foreground="#000000")
        self.RMonthEntry.configure(insertbackground="black")
        self.RMonthEntry.configure(width=44)

        self.RYearEntry = Entry(self.Frame5)
        self.RYearEntry.place(relx=0.78, rely=0.2,height=15, relwidth=0.16)
        self.RYearEntry.configure(background="white")
        self.RYearEntry.configure(disabledforeground="#a3a3a3")
        self.RYearEntry.configure(font=font10)
        self.RYearEntry.configure(foreground="#000000")
        self.RYearEntry.configure(insertbackground="black")
        self.RYearEntry.configure(width=64)

        self.DiagnosisEntry = Entry(self.Frame5)
        self.DiagnosisEntry.place(relx=0.5, rely=0.25,height=15, relwidth=0.44)
        self.DiagnosisEntry.configure(background="white")
        self.DiagnosisEntry.configure(disabledforeground="#a3a3a3")
        self.DiagnosisEntry.configure(font=font10)
        self.DiagnosisEntry.configure(foreground="#000000")
        self.DiagnosisEntry.configure(insertbackground="black")
        self.DiagnosisEntry.configure(width=224)

        self.SeverityEntry = Entry(self.Frame5)
        self.SeverityEntry.place(relx=0.5, rely=0.3, height=15
                , relwidth=0.44)
        self.SeverityEntry.configure(background="white")
        self.SeverityEntry.configure(disabledforeground="#a3a3a3")
        self.SeverityEntry.configure(font=font10)
        self.SeverityEntry.configure(foreground="#000000")
        self.SeverityEntry.configure(insertbackground="black")
        self.SeverityEntry.configure(width=224)

        self.DateOfLastAppEntry = Entry(self.Frame5)
        self.DateOfLastAppEntry.place(relx=0.5, rely=0.35, height=15
                , relwidth=0.44)
        self.DateOfLastAppEntry.configure(background="white")
        self.DateOfLastAppEntry.configure(disabledforeground="#a3a3a3")
        self.DateOfLastAppEntry.configure(font=font10)
        self.DateOfLastAppEntry.configure(foreground="#000000")
        self.DateOfLastAppEntry.configure(insertbackground="black")
        self.DateOfLastAppEntry.configure(width=44)

        self.RPreviousRecordButton = Button(self.Frame5)
        self.RPreviousRecordButton.place(relx=0.05, rely=0.81, height=30
                , width=130)
        self.RPreviousRecordButton.configure(activebackground="#7ccd7c")
        self.RPreviousRecordButton.configure(activeforeground="#000000")
        self.RPreviousRecordButton.configure(background="#7ccd7c")
        self.RPreviousRecordButton.configure(disabledforeground="#a3a3a3")
        self.RPreviousRecordButton.configure(font=font13)
        self.RPreviousRecordButton.configure(foreground="#000000")
        self.RPreviousRecordButton.configure(highlightbackground="#7ccd7c")
        self.RPreviousRecordButton.configure(highlightcolor="black")
        self.RPreviousRecordButton.configure(pady="0")
        self.RPreviousRecordButton.configure(text='''Previous Record''')

        self.RNextRecordButton = Button(self.Frame5)
        self.RNextRecordButton.place(relx=0.42, rely=0.81, height=30, width=100)
        self.RNextRecordButton.configure(activebackground="#7ccd7c")
        self.RNextRecordButton.configure(activeforeground="#000000")
        self.RNextRecordButton.configure(background="#7ccd7c")
        self.RNextRecordButton.configure(disabledforeground="#a3a3a3")
        self.RNextRecordButton.configure(font=font13)
        self.RNextRecordButton.configure(foreground="#000000")
        self.RNextRecordButton.configure(highlightbackground="#7ccd7c")
        self.RNextRecordButton.configure(highlightcolor="black")
        self.RNextRecordButton.configure(pady="0")
        self.RNextRecordButton.configure(text='''Next Record''')

        self.AddRecordButton = Button(self.Frame5,command=MeighPharmacyGUI_Functions.addpatientrecord)
        self.AddRecordButton.place(relx=0.05, rely=0.46, height=30, width=98)
        self.AddRecordButton.configure(activebackground="#7ccd7c")
        self.AddRecordButton.configure(activeforeground="#000000")
        self.AddRecordButton.configure(background="#7ccd7c")
        self.AddRecordButton.configure(disabledforeground="#a3a3a3")
        self.AddRecordButton.configure(font=font13)
        self.AddRecordButton.configure(foreground="#000000")
        self.AddRecordButton.configure(highlightbackground="#7ccd7c")
        self.AddRecordButton.configure(highlightcolor="black")
        self.AddRecordButton.configure(pady="0")
        self.AddRecordButton.configure(text='''Add Record''')

        self.UpdateRecordButton = Button(self.Frame5,command=MeighPharmacyGUI_Functions.editpatientrecord)
        self.UpdateRecordButton.place(relx=0.05, rely=0.53, height=30, width=120)
        self.UpdateRecordButton.configure(activebackground="#7ccd7c")
        self.UpdateRecordButton.configure(activeforeground="#000000")
        self.UpdateRecordButton.configure(background="#7ccd7c")
        self.UpdateRecordButton.configure(disabledforeground="#a3a3a3")
        self.UpdateRecordButton.configure(font=font13)
        self.UpdateRecordButton.configure(foreground="#000000")
        self.UpdateRecordButton.configure(highlightbackground="#7ccd7c")
        self.UpdateRecordButton.configure(highlightcolor="black")
        self.UpdateRecordButton.configure(pady="0")
        self.UpdateRecordButton.configure(text='''Update Record''')

        self.DeleteRecordButton = Button(self.Frame5,command=MeighPharmacyGUI_Functions.deletepatientrecord)
        self.DeleteRecordButton.place(relx=0.05, rely=0.61, height=30, width=115)
        self.DeleteRecordButton.configure(activebackground="#7ccd7c")
        self.DeleteRecordButton.configure(activeforeground="#000000")
        self.DeleteRecordButton.configure(background="#7ccd7c")
        self.DeleteRecordButton.configure(disabledforeground="#a3a3a3")
        self.DeleteRecordButton.configure(font=font13)
        self.DeleteRecordButton.configure(foreground="#000000")
        self.DeleteRecordButton.configure(highlightbackground="#7ccd7c")
        self.DeleteRecordButton.configure(highlightcolor="black")
        self.DeleteRecordButton.configure(pady="0")
        self.DeleteRecordButton.configure(text='''Delete Record''')

        self.Labelframe10 = LabelFrame(self.Labelframe9)
        self.Labelframe10.place(relx=0.58, rely=0.25, relheight=0.21
                , relwidth=0.4)
        self.Labelframe10.configure(relief=GROOVE)
        self.Labelframe10.configure(font=font13)
        self.Labelframe10.configure(foreground="black")
        self.Labelframe10.configure(text='''Search for a Patient Record using its ID:''')
        self.Labelframe10.configure(background="#7ccd7c")
        self.Labelframe10.configure(width=300)

        self.SearchPatientRecordEntry = Entry(self.Labelframe10)
        self.SearchPatientRecordEntry.place(relx=0.2, rely=0.35, height=20
                , relwidth=0.55)
        self.SearchPatientRecordEntry.configure(background="white")
        self.SearchPatientRecordEntry.configure(disabledforeground="#a3a3a3")
        self.SearchPatientRecordEntry.configure(font=font10)
        self.SearchPatientRecordEntry.configure(foreground="#000000")
        self.SearchPatientRecordEntry.configure(insertbackground="black")

        self.SearchPatientRecordButton = Button(self.Labelframe10,command=MeighPharmacyGUI_Functions.searchpatientrecord)
        self.SearchPatientRecordButton.place(relx=0.37, rely=0.61, height=30
                , width=64)
        self.SearchPatientRecordButton.configure(activebackground="#7ccd7c")
        self.SearchPatientRecordButton.configure(activeforeground="#000000")
        self.SearchPatientRecordButton.configure(background="#7ccd7c")
        self.SearchPatientRecordButton.configure(disabledforeground="#a3a3a3")
        self.SearchPatientRecordButton.configure(font=font13)
        self.SearchPatientRecordButton.configure(foreground="#000000")
        self.SearchPatientRecordButton.configure(highlightbackground="#7ccd7c")
        self.SearchPatientRecordButton.configure(highlightcolor="black")
        self.SearchPatientRecordButton.configure(pady="0")
        self.SearchPatientRecordButton.configure(text='''Search''')
        #Code for Outputs Tab
        self.Labelframe11 = LabelFrame(self.TNotebook1_t5)
        self.Labelframe11.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Labelframe11.configure(relief=GROOVE)
        self.Labelframe11.configure(font=font13)
        self.Labelframe11.configure(foreground="black")
        self.Labelframe11.configure(text='''Create a Variety of Outputs of Appointments, Patients and Pharmacists here:''')
        self.Labelframe11.configure(background="#d9d9d9")
        self.Labelframe11.configure(width=150)

        self.Frame6 = Frame(self.Labelframe11)
        self.Frame6.place(relx=0.03, rely=0.05, relheight=0.40, relwidth=0.95)
        self.Frame6.configure(relief=GROOVE)
        self.Frame6.configure(borderwidth="2")
        self.Frame6.configure(relief=GROOVE)
        self.Frame6.configure(background="#7ccd7c")
        self.Frame6.configure(width=705)

        self.CreateBookingOutputButton = Button(self.Frame6,command=bookingdata)
        self.CreateBookingOutputButton.place(relx=0.23, rely=0.29, height=50
                , width=148)
        self.CreateBookingOutputButton.configure(activebackground="#d9d9d9")
        self.CreateBookingOutputButton.configure(activeforeground="#000000")
        self.CreateBookingOutputButton.configure(background="#d9d9d9")
        self.CreateBookingOutputButton.configure(disabledforeground="#a3a3a3")
        self.CreateBookingOutputButton.configure(font=font13)
        self.CreateBookingOutputButton.configure(foreground="#000000")
        self.CreateBookingOutputButton.configure(highlightbackground="#d9d9d9")
        self.CreateBookingOutputButton.configure(highlightcolor="black")
        self.CreateBookingOutputButton.configure(pady="0")
        self.CreateBookingOutputButton.configure(text='''Create Booking
Output''')
        self.CreateBookingOutputButton.configure(width=148)

        self.CreatePharmacistListButton = Button(self.Frame6,command=pharmacistdata)
        self.CreatePharmacistListButton.place(relx=0.52, rely=0.19, height=30
                , width=190)
        self.CreatePharmacistListButton.configure(activebackground="#d9d9d9")
        self.CreatePharmacistListButton.configure(activeforeground="#000000")
        self.CreatePharmacistListButton.configure(background="#d9d9d9")
        self.CreatePharmacistListButton.configure(disabledforeground="#a3a3a3")
        self.CreatePharmacistListButton.configure(font=font13)
        self.CreatePharmacistListButton.configure(foreground="#000000")
        self.CreatePharmacistListButton.configure(highlightbackground="#d9d9d9")
        self.CreatePharmacistListButton.configure(highlightcolor="black")
        self.CreatePharmacistListButton.configure(pady="0")
        self.CreatePharmacistListButton.configure(text='''Create List of All the Pharmacists''')
        self.CreatePharmacistListButton.configure(width=190)

        self.CreatePatientListButton = Button(self.Frame6,command=patientdata)
        self.CreatePatientListButton.place(relx=0.52, rely=0.57, height=30
                , width=188)
        self.CreatePatientListButton.configure(activebackground="#d9d9d9")
        self.CreatePatientListButton.configure(activeforeground="#000000")
        self.CreatePatientListButton.configure(background="#d9d9d9")
        self.CreatePatientListButton.configure(disabledforeground="#a3a3a3")
        self.CreatePatientListButton.configure(font=font13)
        self.CreatePatientListButton.configure(foreground="#000000")
        self.CreatePatientListButton.configure(highlightbackground="#d9d9d9")
        self.CreatePatientListButton.configure(highlightcolor="black")
        self.CreatePatientListButton.configure(pady="0")
        self.CreatePatientListButton.configure(text='''Create List of All Patients''')
        self.CreatePatientListButton.configure(width=188)
        #Code for Welcome label at the tob of the screen
        self.WelcomeLabel = Label(top)
        self.WelcomeLabel.place(relx=0.23, rely=0.03, height=44, width=375)
        self.WelcomeLabel.configure(background="#f0ffff")
        self.WelcomeLabel.configure(disabledforeground="#a3a3a3")
        self.WelcomeLabel.configure(font=font13)
        self.WelcomeLabel.configure(foreground="#000000")
        self.WelcomeLabel.configure(text='''Welcome User''')
        self.WelcomeLabel.configure(text=("%s" % (LoginScreen_Functions.getcurrentuser())))
        self.WelcomeLabel.configure(width=375)
        MeighPharmacyGUI_Functions.userpermission()



#This starts the program
if __name__ == '__main__':
    vp_start_system()