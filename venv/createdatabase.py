import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
password="root",
)

cursor = db.cursor()

# Create the database if it doesn't exist
#cursor.execute("CREATE DATABASE IF NOT EXISTS ProjectDatabase")
cursor.execute("USE ProjectDatabase")



# Create the 'Clinic' table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS Clinics(Clinic_ID varchar(20) PRIMARY KEY,Clinic_Name varchar(50),Day varchar(50),Time varchar(50), Consultant varchar(50))")

#Populate the 'CLinics' table of the initial database:
sql = "INSERT INTO Clinics values(%s,%s,%s,%s,%s)"
#values = ("1","Gastroenterology", "Monday","08.00am","Dr Leddy")
#values = ("2","Endoscopy", "Monday","10.00am","Dr Beatty")
#values = ("3","ENT", "Monday","12.00Pm","Dr Carr")
#values = ("4","Orthopaedics", "Monday","15.00pm","Dr McLoughlin")
#values = ("5","Cardiology", "Tuesday","08.00am","Dr Simmons")
#cursor.execute(sql,values)

# Create the 'Appointment' table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS Appointment(Patient_PPS varchar(30) PRIMARY KEY,Clinic_ID varchar(10),Clinic_Name varchar(50),Day varchar(50),Time varchar(50))")

#Populate the 'Booking' table of the initial database
sql = "INSERT INTO Appointment values(%s,%s,%s,%s,%s)"
#values = ("15935712","2","Endoscopy", "Monday","10.10am") 
#values = ("00001234","2","Endoscopy", "Monday","10.30am") 
#values = ("00001235","2","Endoscopy", "Monday","10.45am")
values = ("00001236","2","Endoscopy", "Monday","11.30am")
cursor.execute(sql,values)

db.commit()

