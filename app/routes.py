import logging, json
from app import app
from flask import render_template, request, Response
from flask_wtf import form
#from app.lights.colors import *
from threading import Thread
from apscheduler.schedulers.background import BackgroundScheduler

color = 'NULL'
brightness = 100
stop_run = False

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global t
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
            stop_run = True
            print("Pressed Red Button")
            brightness = request.form.get('text')
            
        if request.form['submit_button'] == 'ORANGE':
            stop_run = True
            print("Pressed Orange Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'YELLOW':
            stop_run = True
            print("Pressed Yellow Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'GREEN':
            stop_run = True
            print("Pressed Green Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'BLUE':
            stop_run = True
            print("Pressed Blue Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'INDIGO':
            stop_run = True
            print("Pressed Indigo Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'VIOLET':
            stop_run = True
            print("Pressed Violet Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'WHITE':
            stop_run = True
            print("Pressed White Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'ON':
            stop_run = True
            print("Pressed On Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'OFF':
            stop_run = True
            print("Pressed Off Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'RAINBOW':
            print("Pressed Rainbow Button")
            brightness = request.form.get('text')
            stop_run = False

        if request.form['submit_button'] == 'RAINBOW CYCLE':
            print("Press Rainbow Cycle Button")
            brightness = request.form.get('text')
            stop_run = False

        if request.form['submit_button'] == 'RGB TWINKLE':
            print("Press Rainbow Cycle Button")
            brightness = request.form.get('text')
            stop_run = False

        if request.form['submit_button'] == 'COLOR PICKER':
            print("Press Color Picker Button")
            brightness = request.form.get('text')
            stop_run = False

    return render_template('control.html', form=form, color=color, brightness=brightness)

@app.route('/colorpicker', methods=['GET', 'PATCH'])
def color_picker():
    global brightness
    #global color
    global stop_run
    global t

    #color == 'COLOR PICKER'
    #t.kill()
    stop_run = False

    if request.method == 'PATCH':
        setColor = request.get_json(force=True)
        rgbColor = setColor.get("rgbColor")
        r = int(rgbColor[0])
        g = int(rgbColor[1])
        b = int(rgbColor[2])
        colorChanger(r, g, b)
    if request.method == 'GET':
        #startColorPicker()
        return render_template('colorpicker.html')

def run_pattern():
    
    global color
    global stop_run
    global brightness
    
    while not stop_run:
        if color == "RAINBOW":
            rainbow(brightness)
        if color == "RAINBOW CYCLE":
            rainbowCycle(brightness)
        if color == "RGB TWINKLE":
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
    run_pattern()
    
def auto_off():
    global color

    color = "OFF"
    run_pattern()
    
    
 
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
       
            
            
