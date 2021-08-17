import sys, time
from flask import Flask, render_template, request
from app import app
from flask_wtf import form
from flask_executor import Executor
from app.lights.colors import *
from threading import Event

executor = Executor(app)
exit = Event()
color = 'NULL'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    
    global color
    color = request.form.get('submit_button')
    brightness = request.form.get('text')
    if brightness == "":
        brightness = 100

    if request.method == 'POST':
        if request.form['submit_button'] == 'RED':
            print("Pressed Red Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'ORANGE':
            print("Pressed Orange Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'YELLOW':
            print("Pressed Yellow Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'GREEN':
            print("Pressed Green Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'BLUE':
            print("Pressed Blue Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'INDIGO':
            print("Pressed Indigo Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'VIOLET':
            print("Pressed Violet Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'WHITE':
            print("Pressed White Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'ON':
            print("Pressed On Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'OFF':
            print("Pressed Off Button")
        elif request.form['submit_button'] == 'RAINBOW':
            print("Pressed Rainbow Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
    
    run_pattern.submit(color, brightness)
    return render_template('index.html')

@app.route('/control', methods=['GET', 'POST'])
def current():
    
    global color
    color = request.form.get('submit_button')
    brightness = request.form.get('text')
    if brightness == "":
        brightness = 100

    if request.method == 'POST':
        if request.form['submit_button'] == 'RED':
            print("Pressed Red Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'ORANGE':
            print("Pressed Orange Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'YELLOW':
            print("Pressed Yellow Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'GREEN':
            print("Pressed Green Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'BLUE':
            print("Pressed Blue Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'INDIGO':
            print("Pressed Indigo Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'VIOLET':
            print("Pressed Violet Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'WHITE':
            print("Pressed White Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'ON':
            print("Pressed On Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
        elif request.form['submit_button'] == 'OFF':
            print("Pressed Off Button")
        elif request.form['submit_button'] == 'RAINBOW':
            print("Pressed Rainbow Button")
            brightness = request.form.get('text')
            if brightness == "":
                brightness = 100
    
    run_pattern.submit(color, brightness)
    print("render template")
    return render_template('control.html', form=form, color=color), color

@executor.job
def run_pattern(pattern, brightness):
    
    global color
    global status
    

    print("Run " + pattern)
    try:


        while pattern == "RAINBOW":    
            pattern = color
            print("RAINBOW IS RUNNING")
            status = "BEGIN"
            print(status)
            status = rainbow(brightness)
            print(status)
                       
        else:
            if status == "":
                print(status)
                status == ""
                sys.exit()
            else:
                while status != "DONE":
                    #print(status)
                    time.sleep(1/1000)
                else:
                    print(status)
                    status == ""
                    sys.exit()


    except SystemExit:
        if pattern == "RED":
            red(brightness)
        elif pattern == "ORANGE":
            orange(brightness)
        elif pattern == "YELLOW":
            yellow(brightness)
        elif pattern == "GREEN":
            green(brightness)
        elif pattern == "BLUE":
            blue(brightness)
        elif pattern == "INDIGO":
            indigo(brightness)
        elif pattern == "VIOLET":
            violet(brightness)
        elif pattern == "WHITE":
            lights_on(brightness)
        elif pattern == "ON":
            lights_on(brightness)
        else:
            lights_off()

    
        
            
            
