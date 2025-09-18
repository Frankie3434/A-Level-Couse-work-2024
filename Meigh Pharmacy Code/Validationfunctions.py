import sys
import sqlite3
import re

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

    
def presencecheck(entryname,entry):
    if len(entry) == 0:       
        return False
    

def lengthcheck(entryname,entry,minlength,maxlength):
    if minlength == 0:
        pass
    else:
        if presencecheck(entryname,entry) == False: #first checks for presence
            messagebox.showerror("Error","Enter a value for %s" % (entryname))
            return False
    if minlength == maxlength:
        if len(entry)!=minlength or len(entry)!=maxlength:
            messagebox.showerror("Error","Length of %s entry must be %s" % (entryname,minlength))
            return False
        else:
            return True
    elif len(entry) < minlength:
        messagebox.showerror("Error","Length of %s entry must be atleast %s" % (entryname,minlength))
        return False
    elif len(entry) > maxlength:
        messagebox.showerror("Error","Length of %s entry must not exceed %s" % (entryname,maxlength))
        return False
    else:
        return True

def validatepassword(password): #validation function for passwords
    #First the system assumes that the password does not meet the requirements
    correctlength = False
    containsuppercase = False 
    containslowercase = False
    containsnumber = False
    containsspecialcharacter = False
    #checks that the password is the correct length (minimum 8, maximum 255)
    if lengthcheck("password",password,8,255):
        correctlength = True 
    #iterating through the password string
    for character in password:
        if re.search("[^a-zA-Z0-9]+",character): #checks if the character in the password string is a special character
            containsspecialcharacter = True
        elif character.isupper():#checks if character in password string is uppercase
            containsuppercase = True
        elif character.islower():#checks if character in password is lowercase
            containslowercase = True
        elif character.isdigit():#checks if character in password string is a number
            containsnumber = True
    #if the length is correct and there is atleast 1 of each type of character, password returns as valid.
    if correctlength and containsuppercase and containslowercase and containsnumber and containsspecialcharacter:
        return True
    else:
        messagebox.showerror("Error"," The Password must contain atleast 1 Uppercase letter, 1 lowercase letter, 1 number and 1 special character.")
        return False



def hashpasswordencryption(password): #hashes the password using md5 encryption
    import hashlib
    hashed = hashlib.md5(password.encode())
    return hashed.hexdigest()#returns the hexadecimal representation of the hashed password.


            
    
def validatepostcode(postcode):#postcode validation, return true if postcode is valid, else return false.
    if presencecheck("Postcode",postcode) == False: #first checks for presence
            messagebox.showerror("Error","Please enter a value for Postcode")
            return False
    else:
        correctlength = False #assume length is not correct
        nospaces = postcode.replace(" ","") # removes all spaces in postcode entry, eg "BT99 1QQ" turns into "BT991QQ"
        if lengthcheck("Postcode",nospaces,6,8): #check if length is correct
            correctlength = True
            firsttwo = ("%s%s" % (nospaces[0],nospaces[1]))
            #next line checks that first two letters are BT and that the last three characters is a number followed by two letters.
            if firsttwo.upper() =="BT" and nospaces[-3].isdigit() and nospaces[-2].isalpha() and nospaces[-1].isalpha() and correctlength:
                return True
            else:
                messagebox.showerror("Error","Format of Postcode is incorrect, please try again.")
                return False

def validateID(IDName, ID):
    correctformat = True
    for character in ID:
        if character.isdigit():
            pass
        else:
            correctformat = False
    if correctformat:
        return True
    else:
        messagebox.showerror("Error","Format of %s is not correct." % (IDName))
        return False
            
        
       
def validatedate(date):
    #input given is in YYYY-MM-DD ISO 8601 Format which is accepted by sql's DATE field type.
    validyear = False
    validmonth = False
    validdate= False

    year = int(date[0:4])
    month = int(date[5:7])
    date =int(date[8:11])
    print(month)
    
    monthlist1=[1,3,5,7,8,10,12] #Months with 31 days
    monthlist2=[4,6,9,11]#Months with 30 days
    monthlist3=[2]#Months with 28 days

    if year > 0:
        validyear = True
    if month <= 12 and month > 0:
        validmonth = True
        
    if month in monthlist1: 
        if date <= 31 and date > 0:
            validdate = True
    elif month in monthlist2:
        if date <= 30 and date > 0:
            validdate = True
    elif month in monthlist3:
        if date <= 28 and date > 0:
            validdate = True
    if validdate and validmonth and validyear:
        return True
    else:
        if not validyear: #i.e if valid year is false
            messagebox.showerror("Error","Wrong Year entered")
        if not validmonth: #i.e if valid month is false
            messagebox.showerror("Error","Wrong Month entered")
        if not validdate: #i.e if valid date is false
            messagebox.showerror("Error","Wrong Date entered")
        return False
    
def validatetime(time):
    #input given is in HH:MM format which is accepted by sql's TIME field type.
    validhour = False
    validminutes = False

    hour = int(time[0:2])
    minutes = int(time[3:5])

    if hour <= 24 and hour > 0:
        validhour = True
    if minutes <= 60 and minutes > 0:
        validminutes = True
    if validminutes and validhour:
        return True
    else:
        if not validhour:
            messagebox.showerror("Error","Invalid Hour entered")
        if not validminutes:
            messagebox.showerror("Error","Invalid Minutes entered")
        return False