import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm, form
from app import app
from app.lights.colors import *

@app.errorhandler(404)
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
            print("Run red")
            red()
        elif request.form['submit_button'] == 'ORANGE':
            print("Run orange")
            orange()
        elif request.form['submit_button'] == 'YELLOW':
            print("Run yellow")
            yellow()
        elif request.form['submit_button'] == 'GREEN':
            print("Run green")
            green()
        elif request.form['submit_button'] == 'BLUE':
            print("Run blue")
            blue()
        elif request.form['submit_button'] == 'INDIGO':
            print("Run indigo")
            indigo()
        elif request.form['submit_button'] == 'VIOLET':
            print("Run violet")
            violet()
        else:
            request.form['submit_button'] == 'ON'
            print("ON")
            os.system('sudo python3 lightsOn.py -c')

    return render_template('index.html')

@app.route('/control', methods=['GET', 'POST'])
def current():
    if request.method == 'POST':
        if request.form['submit_button'] == 'RED':
            print("Run red")
            red()
        elif request.form['submit_button'] == 'ORANGE':
            print("Run orange")
            orange()
        elif request.form['submit_button'] == 'YELLOW':
            print("Run yellow")
            yellow()
        elif request.form['submit_button'] == 'GREEN':
            print("Run green")
            green()
        elif request.form['submit_button'] == 'BLUE':
            print("Run blue")
            blue()
        elif request.form['submit_button'] == 'INDIGO':
            print("Run indigo")
            indigo()
        elif request.form['submit_button'] == 'VIOLET':
            print("Run violet")
            violet()
        elif request.form['submit_button'] == 'ON':
            print("ON")
            os.system('sudo python3 lightsOn.py -c')
        else:
            request.form['submit_button'] == 'OFF'
            print("OFF")
            os.system('sudo python3 lightsOff.py')
        

    return render_template('control.html', form=form, color=color)

