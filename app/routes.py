import logging, time
from app import app
from flask import render_template, request, Response, make_response
from flask_wtf import form
from app.lights.colors import *
import threading
from apscheduler.schedulers.background import BackgroundScheduler

event_object = threading.Event()
color = 'OFF'
brightness = 100
z = False

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global z
    global color

    if z == True:
        event_object.set()
        print("Thread is already running")
        if request.method == 'POST':
            color = request.form.get('submit_button')
            if request.form['submit_button'] == 'ON':
                print("Pressed On Button")
            if request.form['submit_button'] == 'OFF':
                print("Pressed Off Button")
        return render_template('index.html', form=form, color=color)
    else:
        z = True
        t = threading.Thread(target=run_pattern)
        t.start()
        print("Thread has started")
        return render_template('index.html', form=form, color=color)


@app.route('/control', methods=['GET', 'POST'])
def current():
    global color
    global brightness

    event_object.set()

    if request.method == 'POST':

        color = request.form.get('submit_button')
        brightness = request.form.get('text')

        if request.form['submit_button'] == 'RED':
            print("Pressed Red Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'ORANGE':
            print("Pressed Orange Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'YELLOW':
            print("Pressed Yellow Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'GREEN':
            print("Pressed Green Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'BLUE':
            print("Pressed Blue Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'INDIGO':
            print("Pressed Indigo Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'VIOLET':
            print("Pressed Violet Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'WHITE':
            print("Pressed White Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'ON':
            print("Pressed On Button")
            brightness = request.form.get('text')    

        if request.form['submit_button'] == 'OFF':
            print("Pressed Off Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'RAINBOW':
            print("Pressed Rainbow Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'RAINBOW CYCLE':
            print("Press Rainbow Cycle Button")
            brightness = request.form.get('text')

        if request.form['submit_button'] == 'RGB TWINKLE':
            print("Press Rainbow Cycle Button")
            brightness = request.form.get('text')

    return render_template('control.html', form=form, color=color, brightness=brightness)


@app.route('/colorpicker', methods=['GET', 'PATCH'])
def color_picker():
    global brightness
    global color

    if request.method == 'PATCH':
        setColor = request.get_json(force=True)
        rgbColor = setColor.get("rgbColor")
        r = int(rgbColor[0])
        g = int(rgbColor[1])
        b = int(rgbColor[2])
        colorChanger(r, g, b)
        return make_response("OK", 200)
    if request.method == 'GET':
        color = 'COLOR PICKER'
        startColorPicker()
        event_object.set()
        event_object.clear()
        return render_template('colorpicker.html', color=color)
        
@app.route('/numberpattern', methods=['GET', 'PATCH'])
def numberpattern():
    global color

    if request.method == 'GET':
        color = 'NUMBER PATTERN'
        return render_template('numberpattern.html', color=color)

# def run_pattern():
#     global color
#     global brightness
#
#     while color == 'NULL':
#         time.sleep(.00001)
#
#     print(f'{color} running')
#
#     color_func = color.lower().replace(" ", "_")
#
#     # find function called 'color_func' in the locals() table and if it exists, call it
#     if locals()[color_func]:
#         locals()[color_func]()
#     else:
#         print(f'Invalid color: {color}')
#
#     print(f'{color} waiting')
#     if color != "RAINBOW" and color != "RAINBOW CYCLE" and color != "RGB TWINKLE":
#         event_object.wait()
#
#     return Response(run_pattern())


def run_pattern():
    global color
    global brightness

    event_object.clear()

    print(f'{color} running')

    # color_func = color.lower().replace(" ", "_")
    # locals()[color_func]()

    if color == "RAINBOW":
        rainbow(brightness)
        time.sleep(5)
    elif color == "RAINBOW CYCLE":
        rainbow_cycle(brightness)
        time.sleep(5)
    elif color == "RGB TWINKLE":
        rgb_twinkle(brightness)
        time.sleep(5)
    elif color == "RED":
        red(brightness)
        pass
    elif color == "ORANGE":
        orange(brightness)
        pass
    elif color == "YELLOW":
        yellow(brightness)
        pass
    elif color == "GREEN":
        green(brightness)
        pass
    elif color == "BLUE":
        blue(brightness)
        pass
    elif color == "INDIGO":
        indigo(brightness)
        pass
    elif color == "VIOLET":
        violet(brightness)
        pass
    elif color == "WHITE":
        lights_on(brightness)
        pass
    elif color == "ON":
        lights_on(brightness)
        pass
    elif color == "OFF":
        lights_off()
        pass
    else:
        print(f'Invalid color: {color}')

    print(f'{color} waiting')
    if color != "RAINBOW" and color != "RAINBOW CYCLE" and color != "RGB TWINKLE":
        event_object.wait()
        

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



