from flask import Flask, render_template, request, redirect, Response, jsonify, url_for, session 
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import or_
# from models import Student
import mysql.connector
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)
app.secret_key = 'your_secret_key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ma1020304050@localhost:3306/dorms'
# db = SQLAlchemy(app)
# from flask_sqlalchemy import SQLAlchemy
# connect to database


# class User(db.Model):
#     user_id = db.Column(db.BigInteger, primary_key=True)
#     name = db.Column(db.String(50))
#     password = db.Column(db.String(50))

# class Building(db.Model):
#     building_id = db.Column(db.BigInteger, primary_key=True)
#     location = db.Column(db.String(50))
#     name = db.Column(db.String(50))
#     floor = db.Column(db.BigInteger)

# class DormAdmin(db.Model):
#     user_id = db.Column(db.BigInteger, primary_key=True)
#     shift = db.Column(db.String(50))
#     supervisor = db.Column(db.String(50))
#     building_id = db.Column(db.BigInteger, db.ForeignKey('building.building_id'))

#     building = db.relationship('Building', backref=db.backref('dorm_admins'))

# class Student(db.Model):
#     gu_id = db.Column(db.BigInteger, primary_key=True)
#     national_id = db.Column(db.BigInteger)
#     first_name = db.Column(db.String(50))
#     last_name = db.Column(db.String(50))
#     date_of_birth = db.Column(db.Date)
#     gender = db.Column(db.String(10))
#     country = db.Column(db.String(50))
#     city = db.Column(db.String(50))
#     street = db.Column(db.String(50))
#     phone_numbers = db.Column(db.String(50))
#     email = db.Column(db.String(50))
#     gpa = db.Column(db.Float)
#     major = db.Column(db.String(50))
#     payment_id = db.Column(db.BigInteger)

# class Employee(db.Model):
#     emp_id = db.Column(db.BigInteger, primary_key=True)
#     national_id = db.Column(db.BigInteger)
#     first_name = db.Column(db.String(50))
#     last_name = db.Column(db.String(50))
#     date_of_birth = db.Column(db.Date)
#     gender = db.Column(db.String(10))
#     country = db.Column(db.String(50))
#     city = db.Column(db.String(50))
#     street = db.Column(db.String(50))
#     phone_numbers = db.Column(db.String(50))
#     email = db.Column(db.String(50))
#     employee_type = db.Column(db.String(50))
#     emp_faculty = db.Column(db.String(50))
#     payment_id = db.Column(db.BigInteger)

# class Violation(db.Model):
#     violation_id = db.Column(db.BigInteger, primary_key=True)
#     violation_name = db.Column(db.String(50))
#     type = db.Column(db.String(50))
#     state = db.Column(db.String(50))
#     description = db.Column(db.String(255))
#     date = db.Column(db.Date)
#     gu_id = db.Column(db.BigInteger, db.ForeignKey('student.gu_id'))

#     student = db.relationship('Student', backref=db.backref('violations'))

# class MedicalRecord(db.Model):
#     medical_id = db.Column(db.BigInteger, primary_key=True)
#     type = db.Column(db.String(50))
#     date = db.Column(db.Date)
#     gu_id = db.Column(db.BigInteger, db.ForeignKey('student.gu_id'))

#     student = db.relationship('Student', backref=db.backref('medical_records'))

# class Faculty(db.Model):
#     emp_id = db.Column(db.BigInteger, primary_key=True)
#     full_time = db.Column(db.Boolean)
#     program_name = db.Column(db.String(50))
#     emp_id = db.Column(db.BigInteger, db.ForeignKey('employee.emp_id'))

#     employee = db.relationship('Employee', backref=db.backref('faculty'))

# class Room(db.Model):
#     room_id = db.Column(db.BigInteger, primary_key=True)
#     room_number = db.Column(db.BigInteger)
#     room_capacity = db.Column(db.BigInteger)
#     room_availability = db.Column(db.Boolean)
#     room_type = db.Column(db.String(50))
#     building_id = db.Column(db.BigInteger, db.ForeignKey('building.building_id'))

#     building = db.relationship('Building', backref=db.backref('rooms'))


# class Booking(db.Model):
#     booking_id = db.Column(db.BigInteger, primary_key=True)
#     check_in_time = db.Column(db.DateTime)
#     check_out_time = db.Column(db.DateTime)
#     payment_status = db.Column(db.Boolean)
#     contract = db.Column(db.String(50))
#     no_of_nights = db.Column(db.BigInteger)
#     room_id = db.Column(db.BigInteger, db.ForeignKey('room.room_id'))
#     gu_id = db.Column(db.BigInteger, db.ForeignKey('student.gu_id'))
#     emp_id = db.Column(db.BigInteger, db.ForeignKey('employee.emp_id'))

#     room = db.relationship('Room', backref=db.backref('bookings'))
#     student = db.relationship('Student', backref=db.backref('bookings'))
#     employee = db.relationship('Employee', backref=db.backref('bookings'))

    


# connect to database

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ma1020304050",
    database = "dorms"
)
cursor = db.cursor()

# enter data to database
@app.route('/submit', methods=['POST'])
def submit():
    gu_id = request.form['gu_id']
    national_id = request.form['national_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    gender = request.form['gender']
    country = request.form['country']
    city = request.form['city']
    street = request.form['street']
    phone_numbers = request.form['phone_numbers']
    email = request.form['email']
    gpa = request.form['gpa']
    MedicalCondition = request.form['MedicalCondition']
    major = request.form['major']

    mycursor = db.cursor()
    # Insert new student record into students table
    sql = "INSERT INTO students (gu_id, national_id, first_name, last_name, date_of_birth, gender, country, city, street, phone_numbers, email, gpa, major,MedicalCondition) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
    val = (gu_id, national_id, first_name, last_name, date_of_birth, gender, country, city, street, phone_numbers, email, gpa, major,MedicalCondition)
    mycursor.execute(sql, val)

    # Commit the transaction
    db.commit()
    return ('', 200)


@app.route('/save', methods=['POST'])
def save():
    emp_id = request.form['emp_id']
    national_id = request.form['national_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    gender = request.form['gender']
    country = request.form['country']
    city = request.form['city']
    street = request.form['street']
    phone_numbers = request.form['phone_numbers']
    email = request.form['email']
    employee_type = request.form['employee_type']
    emp_Faculty = request.form['emp_Faculty']

    mycursor = db.cursor()
    # Insert new employee record into employees table
    sql = "INSERT INTO employees (emp_id, national_id, first_name, last_name, date_of_birth, gender, country, city, street, phone_numbers, email, employee_type, emp_Faculty) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
    val = (emp_id, national_id, first_name, last_name, date_of_birth, gender, country, city, street, phone_numbers, email, employee_type, emp_Faculty)
    mycursor.execute(sql, val)

    # Commit the transaction
    db.commit()
    return ('', 200)


@app.route('/SearchStudent')
def SearchStudent():
    # Get the search query from the request parameters
    search_query = request.args.get('q')
    
    # If a search query is provided, retrieve only matching data
    if search_query:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM students WHERE national_id LIKE %s OR major LIKE %s OR gu_id LIKE %s OR first_name LIKE %s OR last_name LIKE %s OR phone_numbers LIKE %s', ('%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%'))
        students_data = cursor.fetchall()
        cursor.close()
    else:
        # Retrieve all data from the 'students' table
        cursor = db.cursor()
        cursor.execute('SELECT * FROM students')
        students_data = cursor.fetchall()
        cursor.close()

        
    
    # Render the 'students.html' template and pass the retrieved data and search query to it
    return render_template('SearchStudent.html', title="Search For Student", custom_css="SearchStudent" ,students_data=students_data, search_query=search_query)
@app.route('/SearchEmployee')
def SearchEmployee():
    # Get the search query from the request parameters
    search_query = request.args.get('q')
    
    # If a search query is provided, retrieve only matching data
    if search_query:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM employees WHERE emp_id LIKE %s OR national_id LIKE %s OR first_name LIKE %s OR last_name LIKE %s', ('%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%'))
        Employee_data = cursor.fetchall()
        cursor.close()
    else:
        # Retrieve all data from the 'students' table
        cursor = db.cursor()
        cursor.execute('SELECT * FROM employees')
        Employee_data = cursor.fetchall()
        cursor.close()
    
    # Render the 'students.html' template and pass the retrieved data and search query to it
    return render_template('SearchEmployee.html', title="Search for Employee", custom_css= "SearchStudent" , Employee_data=Employee_data, search_query=search_query)

# main pages
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            session['username'] = user[1]  # Store the username in a session variable
            return redirect('/home')
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/home')
def home():
    if 'username' in session:
        username = session['username']

        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user:
            gu_id = user[0]  # Assuming student_id is stored in the first column
            cursor.execute("SELECT * FROM students WHERE gu_id = %s", (gu_id,))
            student_data = cursor.fetchone()

            return render_template('home.html',title="Home", custom_css="home" ,username=username, student_data=student_data)
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.route('/register')
def register():
    return render_template('register.html', title="Register", custom_css="home")

@app.route('/acceptance')
def acceptance():
    return render_template('acceptance.html', title="Acceptance", custom_css="home")

@app.route('/admin')
def admin():
    return render_template('admin.html', title="Admin", custom_css="home")

@app.route('/violation')
def violation():
    return render_template('Violation.html', title="Violation", custom_css="home")

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']

        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user:
            gu_id = username  # Assuming student_id is stored in the first column
            cursor.execute("SELECT * FROM students WHERE gu_id = %s", (gu_id,))
            student_data = cursor.fetchone()

            if student_data:
                gu_id = student_data[0]
                national_id = student_data[1]
                first_name = student_data[2]
                last_name = student_data[3]
                date_of_birth = student_data[4]
                gender = student_data[5]
                country = student_data[6]
                city = student_data[7]
                street = student_data[8]
                phone_numbers = student_data[9]
                email = student_data[10]
                gpa = student_data[11]
                major = student_data[12]

                return render_template('profile.html', title="Profile", custom_css="profile" ,gu_id=gu_id, national_id=national_id, first_name=first_name,
                                       last_name=last_name,
                                       date_of_birth=date_of_birth, gender=gender,
                                       country=country, city=city,
                                       street=street, phone_numbers=phone_numbers,
                                       email=email, gpa=gpa,
                                       major=major)
            else:
                return render_template('profile.html', error='Profile data not found')
        else:
            return redirect('/')
    else:
        return redirect('/')


@app.route('/addStudent')
def addStudent():
    return render_template('addStudent.html', title="Add Student", custom_css="register")

@app.route('/addViolation')  # Renamed the endpoint function from 'violation' to 'addviolation'
def add_violation():
    return render_template('addViolation.html', title="Add Violation", custom_css="register")

@app.route('/SearchViolation')
def SearchViolation():
    return render_template('SearchViolation.html', title="Search Violation", custom_css="Violation")

@app.route('/addEmployee')
def addEmployee():
    return render_template('addEmployee.html', title="Add Employee", custom_css="register")

@app.route('/room')
def room():
    return render_template('room.html', title="Room")

@app.route('/notification')
def notification():
    return render_template('notification.html', title="Notification", custom_css="home")

@app.route('/addUser')
def addUser():
    return render_template('addUser.html', title="Add User", custom_css="register")

@app.route('/medicalCondation')
def medicalCondation():
    # Get the search query from the request parameters
    search_query = request.args.get('q')

    # Columns to select from the database
    columns = "MedicalCondition, gu_id"

    # If a search query is provided, retrieve only matching data
    if search_query:
        cursor = db.cursor()
        query = f"SELECT {columns} FROM students WHERE gu_id LIKE %s OR national_id LIKE %s OR first_name LIKE %s OR last_name LIKE %s"
        cursor.execute(query, ('%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%'))
        Employee_data = cursor.fetchall()
        cursor.close()
    else:
        # Retrieve all data from the 'employees' table
        cursor = db.cursor()
        query = f"SELECT {columns} FROM students"
        cursor.execute(query)
        Employee_data = cursor.fetchall()
        cursor.close()
    
    return render_template('medicalCondation.html', title="Medical Condation", custom_css="SearchStudent", Employee_data=Employee_data, search_query=search_query)

@app.route('/gpa')
def gpa():
    # Get the search query from the request parameters
    search_query = request.args.get('q')

    # Columns to select from the database
    columns = "gpa, gu_id"

    # If a search query is provided, retrieve only matching data
    if search_query:
        cursor = db.cursor()
        query = f"SELECT {columns} FROM students WHERE (gu_id LIKE %s OR national_id LIKE %s OR first_name LIKE %s OR last_name LIKE %s) AND gpa > 3 ORDER BY gpa DESC"
        cursor.execute(query, ('%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%'))
        student_data = cursor.fetchall()
        cursor.close()
    else:
        # Retrieve data from the 'students' table with GPA > 3 and order by GPA descending
        cursor = db.cursor()
        query = f"SELECT {columns} FROM students WHERE gpa > 3 ORDER BY gpa DESC"
        cursor.execute(query)
        student_data = cursor.fetchall()
        cursor.close()

    return render_template('gpa.html', title="GPA", custom_css="SearchStudent", student_data=student_data, search_query=search_query)


@app.route('/book', methods=['POST'])
def book():
    building_id = request.form['building_id']
    location = request.form['location']

    mycursor = db.cursor()
    sql = "INSERT INTO buildings (location, building_id) VALUES (%s, %s)"
    val = [(location,building_id)]  # Wrap the location value in a list

    mycursor.executemany(sql, val)  # Use executemany instead of execute

    db.commit()
    return ('', 200)

@app.route('/accept')
def accept():
    return render_template('accpted.html')

@app.route('/refused')
def refused():
    return render_template('refused.html')

@app.route('/booking')
def booking():
    return render_template('booking.html', title="booking", custom_css="register")

# @app.route('/role', methods=['POST'])
# def register():
#     student_id = request.form['student_id']
#     username = request.form['username']
#     password = request.form['password']
#     role = request.form['role']  # Assuming role is selected from a dropdown or radio buttons

#     # Check if the student ID exists in the student table
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM student WHERE StudentID = %s", (student_id,))
#     student_data = cursor.fetchone()

#     if student_data:
#         # Student ID exists, proceed with creating the user in the users table
#         cursor.execute("INSERT INTO users (student_id, username, password, role) VALUES (%s, %s, %s, %s)",
#                        (student_id, username, password, role))
#         db.commit()

#         # Redirect to a success page or login page
#         return ('', 200)

def run_flask_app():
    app.run(host='localhost', port=5000)

# Start the Flask app in a new thread
threading.Thread(target=run_flask_app).start()

# Create a new WebDriver instance
driver = webdriver.Chrome('D:\my_studies\sem_2\Database course\Project\erd\housing project')



# Open the login page
driver.get('http://localhost:5000/')

# Find the username and password input fields, and submit button
username_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')
submit_button = driver.find_element(By.XPATH,'.//input[@type="submit"]')

# Enter username and password
username_field.send_keys('123')
password_field.send_keys('123')

# Wait for the page to load
driver.implicitly_wait(5)

# Click the submit button to login
submit_button.click()

# Open the web page
driver.get('http://127.0.0.1:5000/addStudent')

# Read the Excel file into a DataFrame
data_frame = pd.read_excel('D:/my_studies/sem_2/Database course/Project/erd/housing project/student.xlsx')


# Iterate over the rows of the DataFrame
for index, row in data_frame.iterrows():
   
       
# Extract the values from each row  
    gu_id = row['gu_id']
    national_id = row['national_id']
    first_name = row['first_name']
    last_name = row['last_name']
    date_of_birth = row['date_of_birth']
    gender = row['gender']
    country = row['country']
    city = row['city']
    street = row['street']
    phone_numbers = row['phone_numbers']
    email = row['email']
    gpa = row['gpa']
    MedicalCondition = row['MedicalCondition']
    major = row['major']

    

    # Locate the form fields using their respective selectors
    gu_id_field = driver.find_element(By.NAME, 'gu_id')
    national_id_field = driver.find_element(By.NAME, 'national_id')
    first_name_field = driver.find_element(By.NAME, 'first_name')
    last_name_field = driver.find_element(By.NAME, 'last_name')
    date_of_birth_field = driver.find_element(By.NAME, 'date_of_birth')
    gender_field = driver.find_element(By.NAME, 'gender')
    country_field = driver.find_element(By.NAME, 'country')
    city_field = driver.find_element(By.NAME, 'city')
    street_field = driver.find_element(By.NAME, 'street')
    phone_numbers_field = driver.find_element(By.NAME, 'phone_numbers')
    email_field = driver.find_element(By.NAME, 'email')
    gpa_field = driver.find_element(By.NAME, 'gpa')
    MedicalCondition_field = driver.find_element(By.NAME, 'MedicalCondition')
    major_field = driver.find_element(By.NAME, 'major')
    
    
    # Populate the form fields with the extracted values
    gu_id_field.send_keys(str(gu_id))
    national_id_field.send_keys(str(national_id))
    first_name_field.send_keys(first_name)
    last_name_field.send_keys(last_name)
    date_of_birth_field.send_keys(str(date_of_birth))
    gender_field.send_keys(gender)
    country_field.send_keys(country)
    city_field.send_keys(city)
    street_field.send_keys(street)
    phone_numbers_field.send_keys(phone_numbers)
    email_field.send_keys(email)
    gpa_field.send_keys(str(gpa))
    MedicalCondition_field.send_keys(MedicalCondition)
    major_field.send_keys(major)

    # Submit the form
    button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    driver.execute_script("arguments[0].click();", button)

     # Wait for the page to load after form submission
    driver.implicitly_wait(10)

    # Clear the form fields for the next iteration
    gu_id_field.clear()
    national_id_field.clear()
    first_name_field.clear()
    last_name_field.clear()
    date_of_birth_field.clear()
    gender_field.clear()
    country_field.clear()
    city_field.clear()
    street_field.clear()
    phone_numbers_field.clear()
    email_field.clear()
    gpa_field.clear()
    MedicalCondition_field.clear()
    major_field.clear()



# Close the browser
driver.quit()

if __name__ == '__main__':
    app.run()
