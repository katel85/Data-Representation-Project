from clinicDAO import clinicDao
from appointmentDAO import appointmentDao

Clinic4 = {

    "Clinic_ID": 7,
    "Clinic_Name": "Pain Management",
    "Day": "Tuesday",
    "Time": "13.00",
    "Consultant": "Mr Reilly",
    
}

Clinic5= {
    "Clinic_ID": 8,
    "Clinic_Name": "Dermatology",
    "Day": "Monday",
    "Time": "15.00",
    "Consultant": "MrCauldwell",
    
}


Appoint4 = {
    "Patient_PPS": "36985214",
    "Clinic_ID": 7,
    "Clinic_Name": "Pain Management",
    "Day": "Tuesday",
    "Time": "16.30",
}

Appoint5 = {
    "Patient_Name": "14785236",
    "Clinic_ID": 7,
    "Clinic_Name": "Pain Management",
    "Day": "Tuesday",
    "Time": "17.30",
}


#returnValue = clinicDao.create(Clinic4) #test - code for server.py
#returnValue = clinicDao.create(Clinic5) #test - code for server.py
#returnValue = clinicDao.getAll()
#print(returnValue)
#returnValue = clinicDao.findById(1)
#print(returnValue)
#returnValue = clinicDao.update(Clinic5)
#print(returnValue)
#returnValue = clinicDao.getAll()
#print(returnValue)
#returnValue = clinicDao.delete(8)
#print(returnValue)
#returnValue = clinicDao.getAll()
#print(returnValue)
#returnValue = clinicDao.findById(4)
#print(returnValue)

#returnValue = appointmentDao.create(Appoint4)
#returnValue = appointmentDao.create(Appoint5)
#returnValue = appointmentDao.getAll()
#print(returnValue)
#returnValue = appointmentDao.findById("36985214")
#print(returnValue)
#returnValue = appointmentDao.update("36985214")
#print(returnValue)
