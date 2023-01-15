import mysql.connector
from mysql.connector import cursor
import config as cfg

class AppointmentDao:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=       cfg.mysql['host'],
        user=       cfg.mysql['user'],
        password=   cfg.mysql['password'],
        database=   cfg.mysql['database']
        )   
    

    def create(self, Appointment):
        cursor = self.db.cursor()
        sql = "insert into Appointment (Patient_PPS, Clinic_ID, Clinic_Name, Day, Time) values (%s,%s,%s,%s,%s)"
        values = [
            Appointment["Patient_PPS"],
            Appointment["Clinic_ID"],
            Appointment["Clinic_Name"],
            Appointment["Day"],
            Appointment["Time"],
        ]
        
        cursor.execute(sql, values)
        self.db.commit()

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from Appointment order by Clinic_ID'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, Patient_PPS):
        cursor = self.db.cursor()
        sql = 'select * from Appointment where Patient_PPS = %s'
        values = [Patient_PPS]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, Appointment):
        cursor = self.db.cursor()
        sql = "UPDATE Appointment SET Clinic_ID = %s, Clinic_Name = %s, Day=%s, Time=%s where Patient_PPS=%s"
        values = [
            Appointment['Clinic_ID'],
            Appointment["Clinic_Name"],
            Appointment["Day"],
            Appointment["Time"],
            Appointment["Patient_PPS"]
        ]

        cursor.execute(sql, values)
        self.db.commit()
        return Appointment


    def delete(self, Patient_PPS):
       cursor = self.db.cursor()
       sql = "DELETE FROM Appointment WHERE Patient_PPS = %s"
       values = [Patient_PPS]
       cursor.execute(sql, values)
       self.db.commit()
       return {}

    def convertToDict(self, result):
        colnames = ["Patient_PPS","Clinic_ID", "Clinic_Name", "Day", "Time"]
        Appointment = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                Appointment[colName] = value
        return Appointment

appointmentDao = AppointmentDao()
