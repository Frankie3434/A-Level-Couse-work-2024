 #This code imports modules that are required for my code to run, similar to the MeighPharmacGUI file
import sys
import sqlite3
import Validationfunctions as validate 

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

# functions for the Main GUI
def insertpatient():
    DateOfBirth = ("%s-%s-%s" % (w.PYearEntry.get(),w.PMonthEntry.get(),w.PDateEntry.get()))
    Entry = (w.PFirstnameEntry.get(),
             w.PSurnameEntry.get(),
             DateOfBirth,
             w.PAddressEntry.get(),
             w.PPostcodeEntry.get(),
             w.PMobileEntry.get(),
             w.PTelephoneEntry.get(),
             w.PEmailEntry.get())
    
    if (validate.lengthcheck("Firstname",Entry[0],1,20) and
        validate.lengthcheck("Surname",Entry[1],1,20) and
        validate.lengthcheck("Year",w.PYearEntry.get(),4,4) and
        validate.lengthcheck("Month",w.PMonthEntry.get(),2,2) and
        validate.lengthcheck("Date",w.PDateEntry.get(),2,2) and
        validate.validatedate(DateOfBirth) and
        validate.lengthcheck("Address",Entry[3],1,30) and
        validate.validatepostcode(Entry[4]) and
        validate.lengthcheck("MobileNo",Entry[5],11,11) and
        validate.lengthcheck("Telephone",Entry[6],11,11) and
        validate.lengthcheck("Email",Entry[7],1,20)):
         
        with sqlite3.connect("MPharm.db") as db:
            cursor = db.cursor()
            sql = "insert into Patient(Firstname,Surname,DateOfBirth,Address,Postcode,MobileNo,Telephone,Email) values(?,?,?,?,?,?,?,?)"
            cursor.execute(sql,Entry)
            db.commit
    messagebox.showinfo("Patient Added","Patient : %s %s has been added to the system." % (Entry[0:2]))
    print('MeighPharmacyGUI_Functions.insertpatient')
    sys.stdout.flush()

def updatepatient():#function for updating of patient records
     #asks user if they wish to update, proceeds with update if "yes"
     if messagebox.askyesno("Please Confirm Edit?","Are you sure you want to Edit this patient?"):
         DateOfBirth = ("%s-%s-%s" % (w.PYearEntry.get(),w.PMonthEntry.get(),w.PDateEntry.get()))
         Entry =(w.PSurnameEntry.get(),         #Gather entry from fields
                 w.PFirstnameEntry.get(),
                 DateOfBirth,
                 w.PAddressEntry.get(),
                 w.PPostcodeEntry.get(),
                 w.PMobileEntry.get(),
                 w.PTelephoneEntry.get(),
                 w.PEmailEntry.get(),
                 CurrentPatientID)
         if (validate.lengthcheck("Firstname",Entry[0],1,20) and
        validate.lengthcheck("Surname",Entry[1],1,20) and
        validate.lengthcheck("Year",w.PYearEntry.get(),4,4) and
        validate.lengthcheck("Month",w.PMonthEntry.get(),2,2) and
        validate.lengthcheck("Date",w.PDateEntry.get(),2,2) and
        validate.validatedate(DateOfBirth) and
        validate.lengthcheck("Address",Entry[3],1,30) and
        validate.validatepostcode(Entry[4]) and
        validate.lengthcheck("MobileNo",Entry[5],11,11) and
        validate.lengthcheck("Telephone",Entry[6],11,11) and
        validate.lengthcheck("Email",Entry[7],1,20)):
         
            with sqlite3.connect("MPharm.db") as db:
                     cursor = db.cursor()
                     sql =("""
                    UPDATE Patient
                    SET Surname = "%s", Firstname= "%s", DateOfBirth = "%s", Address = "%s",
                    Postcode = "%s", MobileNo = "%s", Telephone = "%s", Email = "%s"
                    WHERE PatientID = %s """ % (Entry))
                     cursor.execute(sql)
                     db.commit
         messagebox.showinfo("Patient Edited","The Patient Record has been Edited.")
         print('MeighPharmacyGUI_Functions.updatepatient')#ensures that process has gone through, useful when fixing errors

def deletepatient(): #function for deletion of a patient record
    if messagebox.askyesno("Confirm Deletetion?","Are you sure you want to delete patient?"): #ask user if they want to delete the record
        
        with sqlite3.connect("MPharm.db") as db:
            cursor = db.cursor()
            sql = ("DELETE FROM Patient WHERE PatientID = %s" % (CurrentPatientID))
            cursor.execute(sql)
            record = cursor.fetchall()
            db.commit
        messagebox.showinfo("Deleted", "Patient with ID : %s has been deleted" % (CurrentPatientID))
        print('MeighPharmacyGUI_Functions.deletepatient')

def searchpatient():
    global CurrentPatientID
    CurrentPatientID = w.PatientSearchEntry.get()
    with sqlite3.connect("MPharm.db") as db:
        cursor = db.cursor()
        sql = ("Select * from Patient Where PatientID = %s" % (CurrentPatientID))
        cursor.execute(sql)
        record = cursor.fetchall()
        db.commit
    print("length of record: %s" % (len(record)))
    if len(record) == 0:
        w.Frame1.bell()
        messagebox.showerror("Error", "Patient details with ID : %s not found. Please try again." % (CurrentPatientID))
    else:    
        #Clears Entry Fields
        w.PFirstnameEntry.delete(0,100)
        w.PSurnameEntry.delete(0,100)
        w.PDateEntry.delete(0,100)
        w.PMonthEntry.delete(0,100)
        w.PYearEntry.delete(0,100)
        w.PAddressEntry.delete(0,100)
        w.PPostcodeEntry.delete(0,100)
        w.PMobileEntry.delete(0,100)
        w.PTelephoneEntry.delete(0,100)
        w.PEmailEntry.delete(0,100)

        #Below Code splits the "DateOfBirth" field in the Patient record
        #into their Date, Month and Year Components.
        date = record[0][3][8:11]
        month = record[0][3][5:7]
        year = record[0][3][:4]

        #inserts the values of patient details into their respective entry fields.
        w.PFirstnameEntry.insert(0,str(record[0][1]))
        w.PSurnameEntry.insert(0,str(record[0][2]))
        w.PDateEntry.insert(0,date)
        w.PMonthEntry.insert(0,month)
        w.PYearEntry.insert(0,year)
        w.PAddressEntry.insert(0,str(record[0][4]))
        w.PPostcodeEntry.insert(0,str(record[0][5]))
        w.PMobileEntry.insert(0,str(record[0][6]))
        w.PTelephoneEntry.insert(0,str(record[0][7]))
        w.PEmailEntry.insert(0,str(record[0][8]))
        print('MeighPharmacyGUI_Functions.searchpatient')

#Pharmacist Functions
def insertpharmacist():
    Entry = (w.PHFirstnameEntry.get(),
             w.PHSurnameEntry.get(),
             w.PHAddressEntry.get(),
             w.PHPostcodeEntry.get(),
             w.PHUniversityEntry.get(),
             w.PHBorMEntry.get())

    if (validate.lengthcheck("Firstname",Entry[0],1,20) and
        validate.lengthcheck("Surname",Entry[1],1,20) and
        validate.lengthcheck("Address",Entry[2],1,20) and
        validate.lengthcheck("Postcode",Entry[3],1,20) and
        validate.lengthcheck("University",Entry[4],1,20) and
        validate.lengthcheck("BachelorsOrMasters",Entry[5],1,20)):
        
        with sqlite3.connect("MPharm.db") as db:
            cursor = db.cursor()
            sql = "insert into Pharmacist(Firstname,Surname,Address,Postcode,University,BachelorsOrMasters) values(?,?,?,?,?,?)"
            cursor.execute(sql,Entry)
            db.commit
        messagebox.showinfo("Pharmacist Added","Pharmacist : %s %s has been added to the records." % (Entry[0:2]))
        print('MeighPharmacyGUI_Functions.insertpharmacist')
        sys.stdout.flush()

def searchpharmacist():
    global CurrentPharmacistID
    CurrentPharmacistID = w.SearchPharmacistEntry.get()
    with sqlite3.connect("MPharm.db") as db:
        cursor = db.cursor()
        sql = ("Select * from Pharmacist Where PharmacistID = %s" % (CurrentPharmacistID))
        cursor.execute(sql)
        record = cursor.fetchall()
        db.commit
    print("length of record: %s" % (len(record)))
    if len(record) == 0:
        w.Frame1.bell()
        messagebox.showerror("Error", "Pharmacist with ID : %s not found. Please try again." % (CurrentPharmacistID))
    else:    
        #Clears Entry Fields
        w.PHFirstnameEntry.delete(0,100)
        w.PHSurnameEntry.delete(0,100)
        w.PHAddressEntry.delete(0,100)
        w.PHPostcodeEntry.delete(0,100)
        w.PHUniversityEntry.delete(0,100)
        w.PHBorMEntry.delete(0,100)
        
        
        #inserts the values of pharmacist details into their respective entry fields.
        w.PHFirstnameEntry.insert(0,str(record[0][1]))
        w.PHSurnameEntry.insert(0,str(record[0][2]))
        w.PHAddressEntry.insert(0,str(record[0][3]))
        w.PHPostcodeEntry.insert(0,str(record[0][4]))
        w.PHUniversityEntry.insert(0,str(record[0][5]))
        w.PHBorMEntry.insert(0,str(record[0][6]))
        print('MeighPharmacyGUI_Functions.searchpharmacist')

def editpharmacist():#function for editing of Pharmacist records
     #asks user if they wish to update, proceeds with update if "yes"
    if messagebox.askyesno("Confirm edit?","Are you sure you want to edit this pharmacist?"):
        Entry = (w.PHFirstnameEntry.get(),
             w.PHSurnameEntry.get(),
             w.PHAddressEntry.get(),
             w.PHPostcodeEntry.get(),
             w.PHUniversityEntry.get(),
             w.PHBorMEntry.get(),
             CurrentPharmacistID)

        if (validate.lengthcheck("Firstname",Entry[0],1,20) and
        validate.lengthcheck("Surname",Entry[1],1,20) and
        validate.lengthcheck("Address",Entry[2],1,20) and
        validate.lengthcheck("Postcode",Entry[3],1,20) and
        validate.lengthcheck("University",Entry[4],1,20) and
        validate.lengthcheck("BachelorsOrMasters",Entry[5],1,20)):
        
            with sqlite3.connect("MPharm.db") as db:
                    cursor = db.cursor()
                    sql =("""
                    UPDATE Pharmacist
                    SET Firstname = "%s", Surname= "%s", Address = "%s", Postcode = "%s", University = "%s", BachelorsOrMasters = "%s"
                    WHERE PharmacistID = "%s"
                    """ % (Entry))
                    cursor.execute(sql)
                    db.commit
            messagebox.showinfo("Pharmacist Edited","The pharmacist Record has been Edited.")
            print('MeighPharmacyGUI_Functions.editpharmacist')#ensures that process has gone through, useful when fixing errors

def deletepharmacist(): #function for deletion of a pharmacist
    if messagebox.askyesno("Confirm Deletetion?","Are you sure you want to delete Pharmacist?"): #ask user if they want to delete the record
        with sqlite3.connect("MPharm.db") as db:
            cursor = db.cursor()
            sql = ("DELETE FROM Pharmacist WHERE PharmacistID = %s" % (CurrentPharmacistID))
            cursor.execute(sql)
            db.commit
        messagebox.showinfo("Deleted", "Pharmacist with ID : %s has been deleted" % (CurrentPharmacistID))
        w.PHFirstnameEntry.delete(0,100)
        w.PHSurnameEntry.delete(0,100)
        w.PHAddressEntry.delete(0,100)
        w.PHPostcodeEntry.delete(0,100)
        w.PHUniversityEntry.delete(0,100)
        w.PHBorMEntry.delete(0,100)
        print('MeighPharmacyGUI_Functions.deletepharmacist')

#Booking Functions
def addbooking():
    Date = ("%s-%s-%s" % (w.BYearEntry.get(),w.BMonthEntry.get(),w.BDateEntry.get()))
    Time= ("%s:%s" % (w.BHourEntry.get(),w.BMinuteEntry.get()))
    Entry = (w.BPatientIDEntry.get(),
             w.BPharmacistIDEntry.get(),
             w.BNurseIDEntry.get(),
             Date,
             Time,
             w.BookingTypeEntry.get())


    if (validate.lengthcheck("Patient ID",Entry[0],1,4) and
        validate.lengthcheck("Pharmacist ID",Entry[1],1,4) and
        validate.lengthcheck("Nurse ID",Entry[2],1,4) and
        validate.lengthcheck("Year",w.BYearEntry.get(),4,4) and
        validate.lengthcheck("Month",w.BMonthEntry.get(),2,2) and
        validate.lengthcheck("Date",w.BDateEntry.get(),2,2) and
        validate.lengthcheck("Hour",w.BHourEntry.get(),2,2) and
        validate.lengthcheck("Minute",w.BMinuteEntry.get(),2,2) and
        validate.validatedate(Date) and
        validate.validatetime(Time) and
        validate.lengthcheck("Booking Type",Entry[5],1,20)):
        
        with sqlite3.connect("MPharm.db") as db:
            cursor = db.cursor()
            sql = "insert into Bookings(PatientID,PharmacistID,NurseID,Date,Time,BookingType) values(?,?,?,?,?,?)"
            cursor.execute(sql,Entry)
            db.commit
        messagebox.showinfo("Booking Added","Booking has been added to the records.")
        print('MeighPharmacyGUI_Functions.addbooking')
        sys.stdout.flush()

def searchbooking():
    global CurrentBookingID
    CurrentBookingID = w.BookingSearchEntry.get()
    with sqlite3.connect("MPharm.db") as db:
        cursor = db.cursor()
        sql = ("""Select * from Bookings Where BookingID = "%s" """ % (CurrentBookingID))
        cursor.execute(sql)
        record = cursor.fetchall()
        db.commit
    print("length of record: %s" % (len(record)))
    if len(record) == 0:
        w.Frame1.bell()
        messagebox.showerror("Error", "Booking with ID : %s not found. Please try again." % (CurrentBookingID))
    else:    
        #Clears Entry Fields
        w.BPatientIDEntry.delete(0,100)
        w.BPharmacistIDEntry.delete(0,100)
        w.BNurseIDEntry.delete(0,100)
        w.BDateEntry.delete(0,100)
        w.BMonthEntry.delete(0,100)
        w.BYearEntry.delete(0,100)
        w.BHourEntry.delete(0,100)
        w.BMinuteEntry.delete(0,100)
        w.BookingTypeEntry.delete(0,100)

        #Below Code splits the booking Date and booking Time Fields in the bookings Table
        #into their Date, Month and Year Components.
        date = record[0][4][8:11]
        month = record[0][4][5:7]
        year = record[0][4][:4]

        hour = record[0][5][:2]
        minute = record[0][5][3:]


        #inserts the values of booking details into their respective entry fields.
        w.BPatientIDEntry.insert(0,str(record[0][1]))
        w.BPharmacistIDEntry.insert(0,str(record[0][2]))
        w.BNurseIDEntry.insert(0,str(record[0][3]))
        w.BDateEntry.insert(0,date)
        w.BMonthEntry.insert(0,month)
        w.BYearEntry.insert(0,year)
        w.BHourEntry.insert(0,hour)
        w.BMinuteEntry.insert(0,minute)
        w.BookingTypeEntry.insert(0,str(record[0][6]))
        print('MeighPharmacyGUI_Functions.searchbooking')

def editbooking():
     #asks user if they wish to edit, proceeds with edit if "yes"
    if messagebox.askyesno("Confirm Edit?","Are you sure you want to edit this booking?"):
        Date = ("%s-%s-%s" % (w.BYearEntry.get(),w.BMonthEntry.get(),w.BDateEntry.get()))
        Time= ("%s:%s" % (w.BHourEntry.get(),w.BMinuteEntry.get()))
        Entry = (w.BPatientIDEntry.get(),
                 w.BPharmacistIDEntry.get(),
                 w.BNurseIDEntry.get(),
                 Date,
                 Time,
                 w.BookingTypeEntry.get(),
                 CurrentBookingID)

        if (validate.lengthcheck("Patient ID",Entry[0],1,4) and
        validate.lengthcheck("Pharmacist ID",Entry[1],1,4) and
        validate.lengthcheck("Nurse ID",Entry[2],1,4) and
        validate.lengthcheck("Year",w.BYearEntry.get(),4,4) and
        validate.lengthcheck("Month",w.BMonthEntry.get(),2,2) and
        validate.lengthcheck("Date",w.BDateEntry.get(),2,2) and
        validate.lengthcheck("Hour",w.BHourEntry.get(),2,2) and
        validate.lengthcheck("Minute",w.BMinuteEntry.get(),2,2) and
        validate.validatedate(Date) and
        validate.validatetime(Time) and 
        validate.lengthcheck("Booking Type",Entry[5],1,30)):
            
            with sqlite3.connect("MPharm.db") as db:
                cursor = db.cursor()
                sql =("""
                    UPDATE Bookings
                    SET PatientID = "%s", PharmacistID= "%s", NurseID = "%s", Date = "%s", Time = "%s", BookingType = "%s"
                    WHERE BookingID = "%s"
                    """ % (Entry))
                cursor.execute(sql)
                db.commit
            messagebox.showinfo("Booking edited","The booking has been edited.")
            print('MeighPharmacyGUI_Functions.editbooking')#ensures that process has gone through, useful when fixing errors


def deletebooking(): #function for deletion of an booking
    if messagebox.askyesno("Confirm Deletetion?","Are you sure you want to delete booking?"): #ask user if they want to delete the record
        with sqlite3.connect("MPharm.db") as db:
            cursor = db.cursor()
            sql = ("DELETE FROM Bookings WHERE BookingID = %s" % (CurrentBookingID))
            cursor.execute(sql)
            db.commit
        messagebox.showinfo("Deleted", "booking with ID : %s has been deleted" % (CurrentBookingID))
        w.BPatientIDEntry.delete(0,100)
        w.BPharmacistIDEntry.delete(0,100)
        w.BNurseIDEntry.delete(0,100)
        w.BDateEntry.delete(0,100)
        w.BMonthEntry.delete(0,100)
        w.BYearEntry.delete(0,100)
        w.BHourEntry.delete(0,100)
        w.BMinuteEntry.delete(0,100)
        w.BookingTypeEntry.delete(0,100)
        print('MeighPharmacyGUI_Functions.deletebooking')

#Nurse Functions
def addnurse():
    StartDate = ("%s-%s-%s" % (w.NStartYearEntry.get(),w.NStartMonthEntry.get(),w.NStartDateEntry.get()))
    Entry = (w.NFirstnameEntry.get(),
             w.NSurnameEntry.get(),
             w.NAddressEntry.get(),
             w.NPostcodeEntry.get(),
             w.NMobileEntry.get(),
             StartDate,
             w.NMedicalSchoolEntry.get())

    if (validate.lengthcheck("Firstname", Entry[0],1,20) and
    validate.lengthcheck("Surname", Entry[1],1,20) and
    validate.lengthcheck("Address", Entry[2],1,20)and
    validate.lengthcheck("Postcode", Entry[3],1,8) and
    validate.lengthcheck("Mobile", Entry[4],1,20) and
    validate.validatedate(StartDate) and
    validate.lengthcheck("Medical School", Entry[6],1,20)):
    
        with sqlite3.connect("Mpharm.db") as db:
            cursor = db.cursor()
            sql = "insert into Nurse(Firstname,Surname,Address,Postcode,Mobile,Startdate,MedicalSchool) values(?,?,?,?,?,?,?)"
            cursor.execute(sql,Entry)
            db.commit
        messagebox.showinfo("Nurse Added","Nurse %s been added to the records." % (Entry[1]))
        print('MeighPharmacyGUI_Functions.addnurse')
        sys.stdout.flush()

def searchnurse():
    global CurrentNurseID
    CurrentNurseID = w.SearchNurseEntry.get()
    with sqlite3.connect("Mpharm.db") as db:
        cursor = db.cursor()
        sql = ("Select * from Nurse Where NurseID = %s" % (CurrentNurseID))
        cursor.execute(sql)
        record = cursor.fetchall()
        db.commit
    print("length of record: %s" % (len(record)))
    if len(record) == 0:
        w.Frame1.bell()
        messagebox.showerror("Error", "Nurse with ID : %s not found. Please try again." % (CurrentNurseID))
    else:    
        #Clears Entry Fields
        w.NFirstnameEntry.delete(0,100)
        w.NSurnameEntry.delete(0,100)
        w.NAddressEntry.delete(0,100)
        w.NPostcodeEntry.delete(0,100)
        w.NMobileEntry.delete(0,100)
        w.NStartDateEntry.delete(0,100)
        w.NStartMonthEntry.delete(0,100)
        w.NStartYearEntry.delete(0,100)
        w.NMedicalSchoolEntry.delete(0,100)

        Ndate = record[0][6][8:11]
        Nmonth = record[0][6][5:7]
        Nyear = record[0][6][:4]


        #inserts the values of nurse details into their respective entry fields.
        w.NFirstnameEntry.insert(0,str(record[0][1]))
        w.NSurnameEntry.insert(0,str(record[0][2]))
        w.NAddressEntry.insert(0,str(record[0][3]))
        w.NPostcodeEntry.insert(0,str(record[0][4]))
        w.NMobileEntry.insert(0,str(record[0][5]))
        w.NStartDateEntry.insert(0,Ndate)
        w.NStartMonthEntry.insert(0,Nmonth)
        w.NStartYearEntry.insert(0,Nyear)
        w.NMedicalSchoolEntry.insert(0,str(record[0][7]))
        print('MeighPharmacyGUI_Functions.searchnurse')


def editnurse():
     #asks user if they wish to edit, proceeds with edit if "yes"
    if messagebox.askyesno("Confirm edit?","Are you sure you want to edit this nurse?"):
        StartDate = ("%s-%s-%s" % (w.NStartYearEntry.get(),w.NStartMonthEntry.get(),w.NStartDateEntry.get()))
        Entry = (w.NFirstnameEntry.get(),
             w.NSurnameEntry.get(),
             w.NAddressEntry.get(),
             w.NPostcodeEntry.get(),
             w.NMobileEntry.get(),
             StartDate,
             w.NMedicalSchoolEntry.get(),
             CurrentNurseID)
        
        if (validate.lengthcheck("Firstname", Entry[0],1,20) and
    validate.lengthcheck("Surname", Entry[1],1,20) and
    validate.lengthcheck("Address", Entry[2],1,20)and
    validate.lengthcheck("Postcode", Entry[3],1,8) and
    validate.lengthcheck("Mobile", Entry[4],1,20) and
    validate.validatedate(StartDate) and
    validate.lengthcheck("MedicalSchool", Entry[6],1,20)):
            with sqlite3.connect("Mpharm.db") as db:
                cursor = db.cursor()
                sql =("""
                    UPDATE Nurse
                    SET Firstname = "%s", Surname= "%s",  Address= "%s", Postcode = "%s", Mobile= "%s", StartDate= "%s", MedicalSchool= "%s"
                    WHERE NurseID = "%s"
                    """ % (Entry))
                cursor.execute(sql)
                db.commit
            messagebox.showinfo("Nurse edited","The Nurse has been edited.")
            print('MeighPharmacyGUI_Functions.editnurse')#ensures that process has gone through, useful when fixing errors

def deletenurse(): #function for deletion of an nurse
    #ask user if they want to delete the record
    if messagebox.askyesno("Confirm Deletetion?","Are you sure you want to delete nurse with ID : %s?" % (CurrentNurseID)):
        with sqlite3.connect("Mpharm.db") as db:
            cursor = db.cursor()
            sql = ("DELETE FROM Nurse WHERE NurseID = %s" % (CurrentNurseID))
            cursor.execute(sql)
            db.commit
        messagebox.showinfo("Deleted", "Nurse with ID : %s has been deleted" % (CurrentNurseID))
        w.NFirstnameEntry.delete(0,100)
        w.NSurnameEntry.delete(0,100)
        w.NAddressEntry.delete(0,100)
        w.NPostcodeEntry.delete(0,100)
        w.NMobileEntry.delete(0,100)
        w.NStartDateEntry.delete(0,100)
        w.NStartMonthEntry.delete(0,100)
        W.NStartYearEntry.delete(0,100)
        w.NMedicalSchool.delete(0,100)
        print('MeighPharmacyGUI_Functions.deletenurse')

#Patient Record Functions
def addpatientrecord():
    RecordDate = ("%s-%s-%s" % (w.RYearEntry.get(),w.RMonthEntry.get(),w.RDateEntry.get() ) )
    Entry = (w.RPatientIDEntry.get(),
             RecordDate,
             w.DiagnosisEntry.get(),
             w.SeverityEntry.get(),
             w.DateOfLastAppEntry.get())
    
    if (validate.lengthcheck("PatientID", Entry[0],1,4) and
    validate.lengthcheck("Year", w.RYearEntry.get(),4,4) and
    validate.lengthcheck("Month", w.RMonthEntry.get(),2,2) and
    validate.lengthcheck("Date", w.RDateEntry.get(),2,2) and
    validate.validatedate(RecordDate) and
    validate.lengthcheck("Diagnosis", Entry[2],1,50)and
    validate.lengthcheck("Severity", Entry[3],1,50)and
    validate.lengthcheck("DateOfLastAppointment", Entry[4],1,30)):
        
        with sqlite3.connect("MPharm.db") as db:
            cursor = db.cursor()
            sql = "insert into PatientRecords(PatientID,DateOfRecord,Diagnosis,Severity,DateOfLastAppointment) values(?,?,?,?,?)"
            cursor.execute(sql,Entry)
            db.commit
        messagebox.showinfo("Patient Added","A patient record has been added.")
        print('MeighPharmacyGUI_Functions.addpatientrecord')
        sys.stdout.flush()

def searchpatientrecord():
    global CurrentPatientRecordID
    CurrentPatientRecordID = w.SearchPatientRecordEntry.get()
    with sqlite3.connect("MPharm.db") as db:
        cursor = db.cursor()
        sql = ("Select * from PatientRecords Where RecordID = %s" % (CurrentPatientRecordID))
        cursor.execute(sql)
        record = cursor.fetchall()
        db.commit
    print("length of record: %s" % (len(record)))
    if len(record) == 0:
        w.Frame1.bell()
        messagebox.showerror("Error", "Patient Record with ID : %s not found. Please try again." % (CurrentPatientRecordID))
    else:    
        #Clears Entry Fields
        w.RecordIDEntry.delete(0,100)
        w.RPatientIDEntry.delete(0,100)
        w.RDateEntry.delete(0,100)
        w.RMonthEntry.delete(0,100)
        w.RYearEntry.delete(0,100)
        w.DiagnosisEntry.delete(0,100)
        w.SeverityEntry.delete(0,100)
        w.DateOfLastAppEntry.delete(0,100)


        date = record[0][2][8:11]
        month = record[0][2][5:7]
        year = record[0][2][:4]


        #inserts the values of Patient reccord details into their respective entry fields.
        w.RecordIDEntry.insert(0,str(record[0][0]))
        w.RPatientIDEntry.insert(0,str(record[0][1]))
        w.RDateEntry.insert(0,date)
        w.RMonthEntry.insert(0,month)
        w.RYearEntry.insert(0,year)
        w.DiagnosisEntry.insert(0,str(record[0][3]))
        w.SeverityEntry.insert(0,str(record[0][4]))
        w.DateOfLastAppEntry.insert(0,str(record[0][5]))
        print('MeighPharmacyGUI_Functions.searchpatientrecord')

def editpatientrecord():
    #asks user if they wish to update, proceeds with update if "yes"
    if messagebox.askyesno("Confirm Edit?","Are you sure you want to Edit this Patient Record?"):
        RecordDate = ("%s-%s-%s" % (w.RYearEntry.get(),w.RMonthEntry.get(),w.RDateEntry.get() ) )
        Entry = (w.RecordIDEntry.get(),
                 w.RPatientIDEntry.get(),
                 RecordDate,
                 w.DiagnosisEntry.get(),
                 w.SeverityEntry.get(),
                 w.DateOfLastAppEntry.get(),
                 CurrentPatientRecordID)
        if (validate.lengthcheck("PatientID", Entry[1],1,4) and
        validate.lengthcheck("Year", w.RYearEntry.get(),4,4) and
        validate.lengthcheck("Month", w.RMonthEntry.get(),2,2) and
        validate.lengthcheck("Date", w.RDateEntry.get(),2,2) and
        validate.validatedate(RecordDate) and
        validate.lengthcheck("Diagnosis", Entry[3],1,50)and
        validate.lengthcheck("Severity", Entry[4],1,50)and
        validate.lengthcheck("DateOfLastAppointment", Entry[5],1,30)):
            
            with sqlite3.connect("MPharm.db") as db:
                cursor = db.cursor()
                sql =("""
                    UPDATE PatientRecords
                    SET RecordID = "%s", PatientID= "%s", DateOfRecord= "%s", Diagnosis= "%s", Severity = "%s", DateOfLastAppointment = "%s"
                    WHERE RecordID = "%s"
                    """ % (Entry))
                cursor.execute(sql)
                db.commit
            messagebox.showinfo("Patient Record Edited","The Patient Record has been Edited.")
            print('MeighPharmacyGUI_Functions.editpatientrecord')#ensures that process has gone through, useful when fixing errors

def deletepatientrecord(): #function for deletion of an patient record
    #ask user if they want to delete the record
    if messagebox.askyesno("Confirm Deletetion?","Are you sure you want to delete Patient Record with ID : %s?" % (CurrentPatientRecordID)):
        with sqlite3.connect("MPharm.db") as db:
            cursor = db.cursor()
            sql = ("DELETE FROM PatientRecords WHERE RecordID = %s" % (CurrentPatientRecordID))
            cursor.execute(sql)
            db.commit
        messagebox.showinfo("Deleted", "Patient Record with ID : %s has been deleted" % (CurrentPatientRecordID))
        w.RecordIDEntry.delete(0,100)
        w.RPatientIDEntry.delete(0,100)
        w.RDateEntry.delete(0,100)
        w.RMonthEntry.delete(0,100)
        w.RYearEntry.delete(0,100)
        w.DiagnosisEntry.delete(0,100)
        w.SeverityEntry.delete(0,100)
        w.DateOfLastAppEntry.delete(0,100)
        print('MeighPharmacyGUI_Functions.deletepatientrecord')

def export_booking_data_to_text(db_file, text_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    
    # Execute a SELECT query to retrieve data from the Booking table
    c.execute("SELECT BookingID, PatientID, PharmacistID, NurseID, Date, Time, BookingType FROM Bookings")
    booking_data = c.fetchall()  # Fetch all rows
    
    # Close the database connection
    conn.close()
    
    # Write the data to the text file
    with open(text_file, 'w') as file:
        # Write the column headers
        file.write("BookingID, PatientID, PharmacistID, NurseID, Date, Time, BookingType\n")
        
        # Write each row of data
        for row in booking_data:
            file.write(",".join(map(str, row)) + "\n")
            
            


def export_pharmacist_data_to_text(db_file, text_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    
    # Execute a SELECT query to retrieve data from the Pharmacist table
    c.execute("SELECT PharmacistID, Firstname, Surname, Address, Postcode, University, BachelorsOrMasters FROM Pharmacist")
    pharmacist_data = c.fetchall()  # Fetch all rows
    
    # Close the database connection
    conn.close()
    
    # Write the data to the text file
    with open(text_file, 'w') as file:
        # Write the column headers
        file.write("PharmacistID, Firstname, Surname, Address, Postcode, University, BachelorsOrMasters\n")
        
        # Write each row of data
        for row in pharmacist_data:
            file.write(",".join(map(str, row)) + "\n")


def export_patient_data_to_text(db_file, text_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    
    # Execute a SELECT query to retrieve data from the Patient table
    c.execute("SELECT PatientID, Firstname, Surname, DateOfBirth, Address, Postcode, MobileNo, Telephone, Email FROM Patient")
    patient_data = c.fetchall()  # Fetch all rows
    
    # Close the database connection
    conn.close()
    
    # Write the data to the text file
    with open(text_file, 'w') as file:
        # Write the column headers
        file.write("PatientID, Firstname, Surname, DateOfBirth, Address, Postcode, MobileNo, Telephone, Email\n")
        
        # Write each row of data
        for row in patient_data:
            file.write(",".join(map(str, row)) + "\n")
            
           
def userpermission():
    import LoginScreen_Functions
    with sqlite3.connect("MPharm.db") as db:
            cursor = db.cursor()
            sql = """SELECT *
                        FROM login_details
                        WHERE Username = "%s" """ % (LoginScreen_Functions.getcurrentuser())
            cursor.execute(sql)
            record = cursor.fetchall()
            db.commit
    if record == "pharmaceuticalstaff":
        pass
    elif "pharmacist" in record:
        w.TNotebook1.tab(1, state="disabled")






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
    import MeighPharmacyGUI
    MeighPharmacyGUI.vp_start_system()