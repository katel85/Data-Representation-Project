from flask import Flask, jsonify, request, abort,render_template,redirect,session,g,url_for
from clinicDAO import clinicDAO
from appointmentDAO import appointmentDao
import os
from flask import send_from_directory

app = Flask(__name__, static_url_path='', static_folder='staticpages')

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='admin', password='admin'))
users.append(User(id=3, username='Andrew', password='sinscealeile'))



app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template(url_for('profile'))

# Check Connection:
@app.route('/')
def index():
    return "hello"

# Return all Clinics:
@app.route('/Clinics')
def getAll():
    return jsonify(clinicDAO.getAll())


# Get by ID:
@app.route('/Clinics/<Clinic_ID>')
def findById(Clinic_ID):
    return jsonify(clinicDAO.findById(Clinic_ID))   


# Create new Clinic:
@app.route('/Clinics', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)

    Clinics = {
        "Clinic_ID": request.json['Clinic_ID'],
        "Clinic_Name": request.json['Clinic_Name'],
        "Day": request.json['Day'],
        "Time": request.json['Time'],
        "Consultant": request.json['Consultant'],
    }
    return jsonify(clinicDAO.create(Clinics))
    

# Update the database:
# Test:
# 
@app.route('/Clinics/<int:Clinic_ID>', methods=['PUT'])
def update(Clinic_ID):
    foundClinic = clinicDAO.findById(Clinic_ID)
    if not foundClinic:
        abort(404)   
    if not request.json:
        abort(400)
    reqJson = request.json
    if foundClinic == {}:
        return jsonify({}), 404  
    currentClinic = foundClinic
    if 'Clinic_Name' in reqJson:
        currentClinic['Clinic_Name'] = reqJson['Clinic_Name']
    if 'Day' in reqJson:
        currentClinic['Day'] = reqJson['Day']
    if 'Time' in reqJson:
        currentClinic['Time'] = reqJson['Time']
    if 'Consultant' in reqJson:
        currentClinic['Consultant'] = reqJson['Consultant']        
    clinicDAO.update(currentClinic)
    return jsonify(currentClinic)
        
@app.route('/Clinics/<Clinic_ID>' , methods=['DELETE'])
def delete(Clinic_ID):
    clinicDAO.delete(Clinic_ID)
    return jsonify({"done":True})


@app.route('/Appointment')
def getAll2():
    #print("in getall")
    return jsonify(appointmentDao.getAll())

# Get by ID:
@app.route('/Appointment/<Patient_PPS>')
def findById2(Patient_PPS):
    return jsonify(appointmentDao.findById(Patient_PPS))   


# Create new Clinic:
@app.route('/Appointment', methods=['POST'])
def create2():
    
    if not request.json:
        abort(400)

    Appointment = {
        "Patient_PPS": request.json['Patient_PPS'],
        "Clinic_ID": request.json['Clinic_ID'],
        "Clinic_Name": request.json['Clinic_Name'],
        "Day": request.json['Day'],
        "Time": request.json['Time'],
        }
    return jsonify(appointmentDao.create(Appointment))
    

# Update the database:
@app.route('/Appointment/<int:Patient_PPS>', methods=['PUT'])
def update2(Patient_PPS):
    foundAppointment = appointmentDao.findById(Patient_PPS)
    if not foundAppointment:
        abort(404)   
    if not request.json:
        abort(400)
    reqJson = request.json
    if foundAppointment == {}:
        return jsonify({}), 404  
    currentAppointment = foundAppointment
 
    if 'Clinic_ID' in reqJson:
        currentAppointment['Clinic_ID'] = reqJson['Clinic_ID']      
    if 'Clinic_Name' in reqJson:
        currentAppointment['Clinic_Name'] = reqJson['Clinic_Name']
    if 'Day' in reqJson:
        currentAppointment['Day'] = reqJson['Day']
    if 'Time' in reqJson:
        currentAppointment['Time'] = reqJson['Time'] 

    ##values = (currentAppointment['Clinic_ID'],currentAppointment['Clinic_Name'],currentAppointment['Day'],currentAppointment['Time'])
    appointmentDao.update(currentAppointment)
    return jsonify(currentAppointment)
        
@app.route('/Appointment/<Patient_PPS>' , methods=['DELETE'])
def delete2(Patient_PPS):
    appointmentDao.delete(Patient_PPS)
    return jsonify({"done":True})

if __name__ == '__main__' :
    app.run(debug= True)
