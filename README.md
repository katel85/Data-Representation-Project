# Data-Representation-Project
Project Data Representation 2022 G00048625

**Project Overview**

This project aims to create a web application in flask that has a restful API. It should contain a database and webpages that consume the API (perform CURD operations on the data).

The link for this repository is [Github](https://github.com/katel85/Data-Representation-Project) and 
[Pythonanywhere](https://g00048625.pythonanywhere.com/login.html)

The pythonanywhere webpage will be active until 15th April 2023. Access for login is username *admin* and password *admin*.
I have created a website for admin staff in a fictional consultant clinic in the Midlands. I created two DAO python files called appointmentDAO and clinicDAO. These are used by the server to create the RESTful API. The API is constructed in the server and calls the methods from both the DAO files. All these methods worked in the cmd enviroment using the curl commands and also using Postman. One issue I encountered was the PUT method worked in CURL and POSTMAN but when I went to see if the database had updated it did not seem to log the changes corrected. No errors where encoutered in CURL or POSTMAN and status code was 200. There is an issue here and I did not seem to catch it. Feedback would be greatly appreciated.

I also tried to do a login page using flask and sessions but overall this did not work out for me. In the end I just wrote a standard login.html page for the website.

The website currently will allow the user to create and delete both clinics and appointments. Redirects are used in the pages so you can see how your work in going and how many apointments and clinics are on the website.

**File Index and descriptions**

- ".gitignore" - Standard ignore file with config used here to stop information going to server
- "config.py" - File for configuration of MySQL parameters
- "createdatabase.py" - created ProjectDatabase in sql using python to create database in sql and also the tables needed for clinics and appointments.
- "clinicDAO.py" - Data Access Object file for interacting with the  database
- "appointmentDAO"- Data Access Object file for interacting with the  database
- "server.py" - Web server for local host. This is out RESTFUL API page with all the CRUD functions. Passed the url mapping and location of the static pages when creating the app.    All url endpoints were tested on this using CURL and POSTMAN
- "testserver.py"- Used this file to test server API was working correctly
- "static pages folder" - this folder contains the html pages used for our website that will interact with the flask app using ajax script
- "requirements.txt" - folder was used in the virtual enviroment to store all the packages that were required for running the program.


**How to Run the application**

- Repository code can be cloned from https://github.com/katel85/Data-Representation-Project
- One this has been completed it can be opened on whatever python interpreter you please. I have used VS code for this project.
- Run the application in the virual enviroment. The requirements file has the packages required for this application to work.
- Create the database. First ensure your sql console is running, wampserver was used for the mySQL console. Then run the createdatabase.py file.The config file was constructed to hold the database parameters for user,host,password and database name.This file was put into the gignore file so that these parameters are not passed to the server.
- Server.py file can then be run on cmd or visual studio code and this will give you the site that the flask server is running on ie. http://XXX.0.0.1:XXXX. This can then be copied into your internet browser and use http://XXX.0.0.1:XXXX/login.html to go to the login page of the website. 
- Alternatively you could go to https://g00048625.pythonanywhere.com/login.html to see the application running.


**Further work required on the project**

- I would like to have incorporated the [Current waitint lists in ireland](https://data.gov.ie/dataset/outpatient-waiting-list/resource/dfd8f7e9-13b8-4344-9612-dbe0cece4524 ) from  
 the data.gov.ie website but unfortunately I ran out on time on this.


 **References**
[1] Andrew Beatty Github Repository: https://github.com/andrewbeattycourseware/datarepresentation
[2] Flask Tutorial: https://www.tutorialspoint.com
[3] w3schools Tutorials:  https://www.w3schools.com/
[5] Online Booking System With Python Flask (Step-By-Step)-https://code-boxx.com/python-online-booking/-Simple 
[6] How to use Flask-Session in Python Flask ?-https://www.geeksforgeeks.org/how-to-use-flask-session-in-python-flask/?ref=rp-How to use Flask-Session in Python Flask ?
[7] Creating a Login Page in Flask Using Sessions-https://www.youtube.com/watch?v=2Zz97NVbH0U



















