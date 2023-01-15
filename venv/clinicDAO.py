import mysql.connector
from mysql.connector import cursor
import config as cfg

class ClinicsDao:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=       cfg.mysql['host'],
        user=       cfg.mysql['user'],
        password=   cfg.mysql['password'],
        database=   cfg.mysql['database']
        )
    
    
    def create(self, Clinics):
        cursor = self.db.cursor()
        sql = "insert into Clinics (Clinic_ID, Clinic_Name, Day, Time, Consultant) values (%s,%s,%s,%s,%s)"
        values = [
            Clinics["Clinic_ID"],
            Clinics["Clinic_Name"],
            Clinics["Day"],
            Clinics["Time"],
            Clinics["Consultant"],
            
            ]
        
        cursor.execute(sql, values)
        self.db.commit()

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from Clinics order by Day,Time'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, Clinic_ID):
        cursor = self.db.cursor()
        sql = 'select * from Clinics where Clinic_ID = %s'
        values = [Clinic_ID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, Clinics):
        cursor = self.db.cursor()
        sql = "UPDATE Clinics SET Clinic_Name = %s, Day=%s, Time=%s, Consultant=%s where Clinic_ID = %s"
        values = [
            Clinics["Clinic_Name"],
            Clinics["Day"],
            Clinics["Time"],
            Clinics["Consultant"],
            Clinics["Clinic_ID"],
            ]

        cursor.execute(sql, values)
        self.db.commit()
        return Clinics


    def delete(self, Clinic_ID):
       cursor = self.db.cursor()
       sql = "DELETE FROM Clinics WHERE Clinic_ID = %s"
       values = [Clinic_ID]
       cursor.execute(sql, values)
       self.db.commit()
       return {}



    def convertToDict(self, result):
        colnames = ["Clinic_ID", "Clinic_Name", "Day", "Time", "Consultant"]
        Clinics = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                Clinics[colName] = value
        return Clinics

clinicDAO = ClinicsDao()
