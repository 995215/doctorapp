# doctorapp

Check the frontend in mobile browser view


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
