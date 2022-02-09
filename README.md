# doctorapp



create database and tables using db.sql file

Pease run "python api.py" in terminal to start doctor application

Frontend (Check the frontend in mobile browser view)
http://localhost:5000/

HOMEPAGE:
DOCTOR SPECIFICATION:
DOCTOR NAME AND DETAILS:
DOCTOR APPOINTMENT SCHEDULED:
APPOINTMENT":
CONTACT:
![Web capture_9-2-2022_174850_localhost](https://user-images.githubusercontent.com/98824353/153200150-a002d4dc-de9f-43d0-8489-27cce21eac16.jpeg)





Rest APIS

GET - http://localhost:5000/doctordetails

POST - http://localhost:5000/create-appointment

{
    "appointmentname" : "siva",
    "appointmentdate" : "22/05/2022",
    "appointmentemail" : "siva12@gmail.com",
    "appointmenttext" : "checkup",
    "appointmentdoctorname": "arun"
}

GET - http://localhost:5000/appointments

PUT - http://localhost:5000/appointments/update

{
    "appoinmentid": 1
    "appointmentname" : "siva",
    "appointmentdate" : "22/05/2022",
    "appointmentemail" : "siva12@gmail.com",
    "appointmenttext" : "checkup",
    "appointmentdoctorname": "arun"
}


DELETE - http://localhost:5000/delete/<int:appointmentid>
