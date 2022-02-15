// SHOW MENU

const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId)

    if(toggle && nav){
        toggle.addEventListener('click', () =>{
            nav.classList.toggle('show')
        });
     }
}

showMenu('nav_toggle','nav_menu')

// active & remove active
const navlink = document.querySelectorAll('.nav_link')
navlink.forEach(n => n.classList.remove('active'))

function linkaction(){
    navlink.forEach(n => n.classList.remove('active'))
    this.classList.add('active')

    const navmenu = document.getElementById('nav_menu')
    navmenu.classList.remove('show')
}

navlink.forEach(n => n.addEventListener('click', linkaction))
fetch('/doctors')
  .then(response => response.json())
  .then(data => {

            var doctors = '<tr>'
            doctors += '<tread>'
            doctors += '<th>name</th>'
            doctors += '<th>degree</th>'
            doctors += '<th>specification</th>'
            doctors += '<th>startime</th>'
            doctors += '<th>endtime</th>'
            doctors += '</tread>'
            doctors += '</tr>'

            var doctors_names = '<option value=""> select doctorname</option>'
            
            
        
    data.forEach(function(value){
        doctors += '<tr>'
        doctors += '<tbody>'
        doctors += '<td>'+value["doctorname"]+'</td>'
        doctors += '<td>'+value["doctordegree"]+'</td>'
        doctors += '<td>'+value["doctorspecification"]+'</td>'
        doctors += '<td>'+value["doctorstarttime"]+'</td>'
        doctors += '<td>'+value["doctorendtime"]+'</td>'
        doctors += '</tbody>'
        doctors += '</tr>'
        document.getElementById("doctor_list").innerHTML = doctors
       
        doctors_names += '<option value="'+value["doctorname"]+'">'+value["doctorname"]+'</option>'
        document.getElementById("doctors_names").innerHTML = doctors_names
        console.log(value);
       console.log(value["doctorname"]);
    });
    
  });

function fetch_appointments() {
    fetch('/appointments')
.then(response => response.json())
.then(data =>{

   var appointment = '<tr>'
  appointment += '<tread>'
  appointment += '<th>name</th>'
  appointment += '<th>date</th>'
  appointment += '<th>doctorname</th>'
  appointment += '<th>email</th>'
  appointment += '<th>text</th>'
  appointment += '</tread>'
  appointment += '</tr>'

  data.forEach(function(value){
      appointment += '<tr>'
      appointment += '<tbody>'
      appointment += '<td>'+value["appointmentname"]+'</td>'
      appointment += '<td>'+value["appointmentdate"]+'</td>'
      appointment += '<td>'+value["appointmentdoctorname"]+'</td>'
      appointment += '<td>'+value["appointmentemail"]+'</td>'
      appointment += '<td>'+value["appointmenttext"]+'</td>'
      appointment += '</tbody>'
      appointment += '</tr>'
      document.getElementById("appointment_list").innerHTML = appointment

  });
});
}

fetch_appointments();

  


function create_appointment(form) {
    console.log("test");
    const formData = new URLSearchParams(new FormData(document.getElementById("appointment_form")));
    console.log(formData);

    var formobject = {};
    formData.forEach(function(value, key){
        formobject[key] = value;
    });

    formobject = JSON.stringify(formobject);

    fetch("/create-appointment", {
        method:"POST", 
        body: formobject,
        headers: {
            "Content-Type": "application/json",
            // "Content-Type": "multipart/form-data",
        }
      }).then(response => response.json())
      .then(data => {
        fetch_appointments();
          console.log(data);
      });
}



