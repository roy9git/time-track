from flask import Flask,request,render_template,redirect
import os
import sqlite3

curr_loc = os.path.dirname(os.path.abspath(__file__))

myapp = Flask(__name__)

@myapp.route('/')
def homepage():
    return render_template('homepage.html')

@myapp.route('/Login', methods=['GET', 'POST'])
def Login():

    if request.method == 'POST':
        name = request.form.get('Email-address')
        post = request.form.get('Password')
        # still need to complete

    return render_template('login.html')

@myapp.route('/Loggedin', methods=['GET', 'POST'])
def Loggedin():
    return render_template('loggedin.html')

@myapp.route('/register', methods = ['GET','POST'])
def register():
    return render_template('register.html')

'''@myapp.route('/',methods = ['POST'])
def checklogin():
    EA = request.form['Email-address']
    PW = request.form['Password']

    sqlconnection = sqlite3.Connection(curr_loc + '\Login.db')
    cursor = sqlconnection.cursor()
    query1 = 'SELECT Email-address, Password from myForm where Email-address = {ea} AND Password = {pw}'.format(ea = EA, pw = PW)
    
    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows)==1:
        return render_template(loggedin.html)
    else:
         return redirect('/register')

@myapp.route('/register', methods = ['GET','POST'])
def registerpage():
    if request.method == 'POST':
        DEA = request.form['Email-address']
        DPW = request.form['Password']
        sqlconnection = sqlite3.Connection(curr_loc + '\Login.db')
        cursor = sqlconnection.cursor()
        query1 = 'INSERT INTO myForm VALUES({ea},{pw})'.format(ea = DEA, pw = DPW)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect('/')
    return render_template('register.html')'''


if __name__ == '__main__':
       myapp.run()