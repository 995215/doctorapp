import pymysql
from app import app
from db import mysql
from flask import Flask, jsonify
from flask import flash, request


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/doctors')
def doctors():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM doctor_app.doctor;")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code=200
        print(rows)
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/doctordetails')
def doctors_details():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM doctor_app.doctor;")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code=200
        print(rows)
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
@app.route('/create-appointment', methods=['POST'])
def create_appointment():
    conn = None
    cursor = None
    try:
        _json = request.json
        _appointmentname = _json['appointmentname']
        _appointmentdate = _json['appointmentdate']
        _appointmentdoctorname = _json['appointmentdoctorname']
        _appointmentemail = _json['appointmentemail']
        _appointmenttext = _json['appointmenttext']
        print("test")
		# validate the received values
        if _appointmentname and _appointmentdate and _appointmentdoctorname and _appointmentemail and _appointmenttext and request.method == 'POST':
			
			# save edits  
             sql = "INSERT INTO appointment(appointmentname, appointmentdate, appointmentdoctorname, appointmentemail, appointmenttext) VALUES(%s, %s, %s, %s, %s)" 
             data = (_appointmentname, _appointmentdate, _appointmentdoctorname, _appointmentemail, _appointmenttext)
             conn = mysql.connect()
             cursor = conn.cursor()
             cursor.execute(sql, data)
             conn.commit()
             resp = jsonify('User added successfully!')
             resp.status_code = 200
             return resp
        else:
            return not_found()
    except Exception as e:
		     print(e)
    finally:
        cursor.close() 
        conn.close()


@app.route('/add', methods=['POST'])
def add_user():
    conn = None
    cursor = None
    try:
        _json = request.json
        _doctorname = _json['doctorname']
        _doctornumber = _json['doctornumber']
        _doctorappointment = _json['doctorappointment']
        print("test")
		# validate the received values
        if _doctorname and _doctornumber and _doctorappointment and request.method == 'POST':
			
			# save edits  
             sql = "INSERT INTO home_user(doctorname, doctornumber, doctorappointment) VALUES(%s, %s, %s)" 
             data = (_doctorname, _doctornumber, _doctorappointment,)
             conn = mysql.connect()
             cursor = conn.cursor()
             cursor.execute(sql, data)
             conn.commit()
             resp = jsonify('User added successfully!')
             resp.status_code = 200
             return resp
        else:
            return not_found()
    except Exception as e:
		     print(e)
    finally:
        cursor.close() 
        conn.close()
		
@app.route('/appointments')
def users():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM doctor_app.appointment;")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code=200
        print(rows)
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
		
@app.route('/appointments/<int:id>')
def user(id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT appointmentname appointmentname, appointmentdate appointmentdate, appointmentdoctortname appointmentdoctorname, appointmentemail appointmentemail, appointmenttext appointmenttext FROM appointment WHERE appointmentid=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/appointments/update', methods=['PUT'])
def update_user():
    conn = None
    cursor = None
    try:
        _json = request.json
        _appointmentid = _json['appointmentid']
        _appointmentname = _json['appointmentname']
        _appointmentdate = _json['appointmentdate']
        _appointmentdoctorname = _json['appointmentdoctorname']	
        _appointmentemail = _json['appointmentemail']	
        _appointmenttext = _json['appointmenttext']		
        # validate the received values
        if _appointmentid and _appointmentdate and _appointmentdoctorname and _appointmentemail and _appointmenttext and request.method == 'PUT':
            print("test")
            # save edits
            sql = "UPDATE appointment SET appointmentname=%s,appointmentdate=%s, appointmentdoctorname=%s, appointmentemail=%s, appointmenttext=%s WHERE  appoinmentid=%s"
            data = (_appointmentname, _appointmentdate, _appointmentdoctorname, _appointmentemail, _appointmenttext, _appointmentid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
        print("test")
    finally:
        cursor.close() 
        conn.close()
		
@app.route('/delete/<int:appointmentid>', methods=['DELETE'])
def delete_user(appointmentid):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM appointment WHERE appointmentid=%s", (appointmentid,))
		conn.commit()
		resp = jsonify('User deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run(debug=True)