import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm, form
from app import app

app.errorhandler(404)
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
            print("RED")
        elif request.form['submit_button'] == 'ORANGE':
            print("ORANGE")
        elif request.form['submit_button'] == 'YELLOW':
            print("YELLOW")
        elif request.form['submit_button'] == 'GREEN':
            print("GREEN")
        elif request.form['submit_button'] == 'BLUE':
            print("BLUE")
        elif request.form['submit_button'] == 'INDIGO':
            print("INDIGO")
        elif request.form['submit_button'] == 'VIOLET':
            print("VIOLET")
        else:
            request.form['submit_button'] == 'OFF'
            print("OFF")

    return render_template('index.html')

@app.route('/control', methods=['GET', 'POST'])
def current():
    color = request.form.get('submit_button')
    if request.method == 'POST':
        if request.form['submit_button'] == 'RED':
            print("RED")
        elif request.form['submit_button'] == 'ORANGE':
            print("ORANGE")
        elif request.form['submit_button'] == 'YELLOW':
            print("YELLOW")
        elif request.form['submit_button'] == 'GREEN':
            print("GREEN")
        elif request.form['submit_button'] == 'BLUE':
            print("BLUE")
        elif request.form['submit_button'] == 'INDIGO':
            print("INDIGO")
        elif request.form['submit_button'] == 'VIOLET':
            print("VIOLET")
        elif request.form['submit_button'] == 'ON':
            print("ON")
        else:
            request.form['submit_button'] == 'OFF'
            print("OFF")
        

    return render_template('control.html', form=form, color=color)