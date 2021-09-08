import logging
from app import app
from flask import render_template, request, Response
from flask_wtf import form
from app.lights.colors import *
from threading import Thread
from apscheduler.schedulers.background import BackgroundScheduler

color = 'NULL'
brightness = 100
stop_run = False

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    t = Thread(target=run_pattern)
    t.start()
    return render_template('index.html')


@app.route('/control', methods=['GET', 'POST'])
def current():
    
    global color
    global brightness
    global stop_run

    color = request.form.get('submit_button')
    brightness = request.form.get('text')

    if request.method == 'POST':
        if request.form['submit_button'] == 'RED':
            print("Pressed Red Button")
            brightness = request.form.get('text')
            stop_run = True
            
        if request.form['submit_button'] == 'ORANGE':
            print("Pressed Orange Button")
            brightness = request.form.get('text')
            stop_run = True

        if request.form['submit_button'] == 'YELLOW':
            print("Pressed Yellow Button")
            brightness = request.form.get('text')
            stop_run = True

        if request.form['submit_button'] == 'GREEN':
            print("Pressed Green Button")
            brightness = request.form.get('text')
            stop_run = True

        if request.form['submit_button'] == 'BLUE':
            print("Pressed Blue Button")
            brightness = request.form.get('text')
            stop_run = True

        if request.form['submit_button'] == 'INDIGO':
            print("Pressed Indigo Button")
            brightness = request.form.get('text')
            stop_run = True

        if request.form['submit_button'] == 'VIOLET':
            print("Pressed Violet Button")
            brightness = request.form.get('text')
            stop_run = True

        if request.form['submit_button'] == 'WHITE':
            print("Pressed White Button")
            brightness = request.form.get('text')
            stop_run = True

        if request.form['submit_button'] == 'ON':
            print("Pressed On Button")
            brightness = request.form.get('text')
            stop_run = True

        if request.form['submit_button'] == 'OFF':
            print("Pressed Off Button")
            brightness = request.form.get('text')
            stop_run = True

        if request.form['submit_button'] == 'RAINBOW':
            print("Pressed Rainbow Button")
            brightness = request.form.get('text')
            stop_run = False

        if request.form['submit_button'] == 'RAINBOW_CYCLE':
            print("Press Rainbow Cycle Button")
            brightness = request.form.get('text')
            stop_run = False

        if request.form['submit_button'] == 'RGB_TWINKLE':
            print("Press Rainbow Cycle Button")
            brightness = request.form.get('text')
            stop_run = False

    return render_template('control.html', form=form, color=color, brightness=brightness)

def run_pattern():
    
    global color
    global stop_run
    global brightness
    
    while not stop_run:
        if color == "RAINBOW":
            rainbow(brightness)
        if color == "RAINBOW_CYCLE":
            rainbowCycle(brightness)
        if color == "RGB_TWINKLE":
            rgb_twinkle(brightness)
    
    if color == "RED":
        red(brightness)
    if color == "ORANGE":
        orange(brightness)
    if color == "YELLOW":
        yellow(brightness)
    if color == "GREEN":
        green(brightness)
    if color == "BLUE":
        blue(brightness)
    if color == "INDIGO":
        indigo(brightness)
    if color == "VIOLET":
        violet(brightness)
    if color == "WHITE":
        lights_on(brightness)
    if color == "ON":
        lights_on(brightness)
    if color == "OFF":
        lights_off()

    return Response(run_pattern())

def auto_on():
    global brightness
    global color

    color = "ON"
    run_pattern(brightness)
    
def auto_off():
    global color

    color = "OFF"
    run_pattern(brightness)
    
    
 
start = BackgroundScheduler()
start.add_job(auto_on, 'cron', hour=17)
start.start()

stop = BackgroundScheduler()
stop.add_job(auto_off, 'cron', hour=2)
stop.start()

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)
       
            
            
