import logging, sys, time
from flask import render_template, request
from app import app
from flask_wtf import form
from flask_executor import Executor
from app.lights.colors import *
from threading import Event
from apscheduler.schedulers.background import BackgroundScheduler
    

executor = Executor(app)
exit = Event()
color = 'NULL'
status = "DONE"
global brightness

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    
    global color
    color = request.form.get('submit_button')
    return render_template('index.html')

@app.route('/control', methods=['GET', 'POST'])
def current():
    
    global color
    color = request.form.get('submit_button')
    brightness = request.form.get('text')

    if request.method == 'POST':
        if request.form['submit_button'] == 'RED':
            print("Pressed Red Button")
            brightness = request.form.get('text')
            
        elif request.form['submit_button'] == 'ORANGE':
            print("Pressed Orange Button")
            brightness = request.form.get('text')

        elif request.form['submit_button'] == 'YELLOW':
            print("Pressed Yellow Button")
            brightness = request.form.get('text')

        elif request.form['submit_button'] == 'GREEN':
            print("Pressed Green Button")
            brightness = request.form.get('text')

        elif request.form['submit_button'] == 'BLUE':
            print("Pressed Blue Button")
            brightness = request.form.get('text')

        elif request.form['submit_button'] == 'INDIGO':
            print("Pressed Indigo Button")
            brightness = request.form.get('text')

        elif request.form['submit_button'] == 'VIOLET':
            print("Pressed Violet Button")
            brightness = request.form.get('text')

        elif request.form['submit_button'] == 'WHITE':
            print("Pressed White Button")
            brightness = request.form.get('text')

        elif request.form['submit_button'] == 'ON':
            print("Pressed On Button")
            brightness = request.form.get('text')

        elif request.form['submit_button'] == 'OFF':
            print("Pressed Off Button")
            brightness = request.form.get('text')

        elif request.form['submit_button'] == 'RAINBOW':
            print("Pressed Rainbow Button")
            brightness = request.form.get('text')

        elif request.form['submit_button'] == 'RAINBOW_CYCLE':
            print("Press Rainbow Cycle Button")
            brightness = request.form.get('text')

    
    run_pattern.submit(color, brightness)
    #print("render template")
    return render_template('control.html', form=form, color=color, brightness=brightness), color

@executor.job
def run_pattern(pattern, brightness):
    
    global color
    global status
    global strip
    
    print("Run " + pattern)
    #print(brightness)
    try:

        while pattern == "RAINBOW":    
            pattern = color    
            #print("RAINBOW IS RUNNING")
            while status != "DONE":
                time.sleep(1/1000)
            status = "BEGIN"
            #print(status)
            status = rainbow(brightness)
            #print(status)
        
        while pattern == "RAINBOW_CYCLE":
            pattern = color
            #print("RAINBOW CYCLE IS RUNNING")
            while status != "DONE":
                time.sleep(1/1000)
            status = "BEGIN"
            #print(status)
            status = rainbowCycle(brightness)
            #print(status)

        while pattern == "RGB_TWINKLE":
            pattern = color
            #print("RGB_TWINKLE IS RUNNING")
            while status != "DONE":
                time.sleep(1/1000)
            status = "BEGIN"
            #print(status)
            status = rgb_twinkle(brightness)
            #print(status)
                       
        else:
            while status != "DONE":
                time.sleep(1/10000)
                if brightness != brightness:
                    sys.exit()
            else:
                #print(status)
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

def auto_on():
    default_brightness = 100
    lights_on(default_brightness)
    
def auto_off():
    lights_off()
    
 
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
       
            
            
