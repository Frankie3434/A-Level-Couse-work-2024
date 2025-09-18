import sqlite3

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to replace it (yes/no): " .format(table_name))
            if response == "y":
                keep_table = False
                print("The table {0} will be recreated - all data will be deleted." .format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept.")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_patient_table():
    sql = """create table Patient
            (PatientID integer,
            Firstname text,
            Surname text,
            DateOfBirth Date,
            Address text,
            Postcode text,
            MobileNo text,
            Telephone text,
            Email text,
            primary key(PatientID))
            """
    create_table(db_name,"Patient",sql)

def create_patientrecords_table():
    sql = """ create table PatientRecords
            (RecordID integer,
            PatientID integer,
            DateOfRecord date,
            Diagnosis text,
            Severity text,
            DateOfLastAppointment text,
            primary key(RecordID),
            foreign key(PatientID) references Patient(PatientID) on update cascade on delete cascade)"""
    create_table(db_name, "PatientRecords",sql)

def create_bookings_table():
    sql = """ create table Bookings
            (BookingID integer,
            PatientID integer,
            PharmacistID integer,
            NurseID integer,
            Date date,
            Time time,
            BookingType text,
            primary key(BookingID)
            foreign key(PatientID) references Patient(PatientID) on update cascade on delete cascade
            foreign key(PharmacistID) references Pharmacist(PharmacistID) on update cascade on delete cascade
            foreign key(NurseID) references Nurse(NurseID) on update cascade on delete cascade)"""
    create_table(db_name, "Bookings",sql)

def create_nurse_table():
    sql = """ create table Nurse
            (NurseID integer,
            Firstname text,
            Surname text,
            Address text,
            Postcode text,
            Mobile text,
            StartDate Date,
            Medicalschool text,
            primary key(NurseID))
            """
    create_table(db_name, "Nurse",sql)

def create_pharmacist_table():
    sql = """ create table Pharmacist
            (PharmacistID integer,
            Firstname text,
            Surname text,
            Address text,
            Postcode text,
            University text,
            BachelorsOrMasters text,
            primary key(PharmacistID))
            """
    create_table(db_name, "Pharmacist",sql)


def create_login_details_table():
    sql = """ create table login_details
            (Username text,
            Password VARCHAR,
            UserType text,
            primary key(Username))"""
    create_table(db_name, "login_details",sql)

if __name__ == "__main__":
    db_name = "MPharm.db"
    create_login_details_table()
    create_pharmacist_table()
    create_bookings_table()
    create_nurse_table()
    create_patientrecords_table()
    create_patient_table()
    