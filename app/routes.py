import os, sys
from flask import Flask, render_template, request
from flask_wtf import FlaskForm, form
from app import app

def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'RED':
            print("Run trueRed")
            os.system('sudo python3 trueRed.py')
        elif request.form['submit_button'] == 'ORANGE':
            print("Run trueOrange")
            os.system('sudo python3 trueOrange.py')
        elif request.form['submit_button'] == 'YELLOW':
            print("Run trueYellow")
            os.system('sudo python3 trueYellow.py')
        elif request.form['submit_button'] == 'GREEN':
            print("Run trueGreen")
            os.system('sudo python3 trueGreen.py')
        elif request.form['submit_button'] == 'BLUE':
            print("Run trueBlue")
            os.system('sudo python3 trueBlue.py')
        elif request.form['submit_button'] == 'INDIGO':
            print("Run trueIndigo")
            os.system('sudo python3 trueIndigo.py')
        elif request.form['submit_button'] == 'VIOLET':
            print("Run trueViolet")
            os.system('sudo python3 trueViolet.py')
        elif request.form['submit_button'] == 'ON':
            print("ON")
            os.system('sudo python3 lightsOn.py -c')
        else:
            request.form['submit_button'] == 'OFF'
            print("OFF")
            os.system('sudo python3 lightsOff.py')

    return render_template('index.html')

@app.route('/control', methods=['GET', 'POST'])
def current():
    color = request.form.get('submit_button')
    if request.method == 'POST':
        if request.form['submit_button'] == 'RED':
            print("Run trueRed")
            os.system('sudo python3 trueRed.py')
        elif request.form['submit_button'] == 'ORANGE':
            print("Run trueOrange")
            os.system('sudo python3 trueOrange.py')
        elif request.form['submit_button'] == 'YELLOW':
            print("Run trueYellow")
            os.system('sudo python3 trueYellow.py')
        elif request.form['submit_button'] == 'GREEN':
            print("Run trueGreen")
            os.system('sudo python3 trueGreen.py')
        elif request.form['submit_button'] == 'BLUE':
            print("Run trueBlue")
            os.system('sudo python3 trueBlue.py')
        elif request.form['submit_button'] == 'INDIGO':
            print("Run trueIndigo")
            os.system('sudo python3 trueIndigo.py')
        elif request.form['submit_button'] == 'VIOLET':
            print("Run trueViolet")
            os.system('sudo python3 trueViolet.py')
        elif request.form['submit_button'] == 'ON':
            print("ON")
            os.system('sudo python3 lightsOn.py -c')
        else:
            request.form['submit_button'] == 'OFF'
            print("OFF")
            os.system('sudo python3 lightsOff.py')
        

    return render_template('control.html', form=form, color=color)

