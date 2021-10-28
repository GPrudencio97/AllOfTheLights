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


@app.route('/', methods=['GET', 'POST', 'PATCH'])
@app.route('/index', methods=['GET', 'POST', 'PATCH'])
def index():
    global z
    global color
    global brightness

    if z == True:
        if request.method == 'POST':
            event_object.set()
            print("Thread is already running")
            color = request.form.get('submit_button')
            if request.form['submit_button'] == 'ON':
                print("Pressed On Button")
            if request.form['submit_button'] == 'OFF':
                print("Pressed Off Button")
            return render_template('index.html', form=form, color=color, brightness=brightness)
        elif request.method == 'PATCH':
            event_object.set()
            brightness = request.get_json(force=True)
            return make_response("OK", 200)
        else:
            return render_template('index.html', form=form, color=color, brightness=brightness)
    else:
        z = True
        t = threading.Thread(target=run_pattern)
        t.start()
        print("Thread has started")
        return render_template('index.html', form=form, color=color, brightness=brightness)


@app.route('/control', methods=['GET', 'POST', 'PATCH'])
def current():
    global color
    global brightness

    event_object.set()

    if request.method == 'POST':

        color = request.form.get('submit_button')

        if request.form['submit_button'] == 'RED':
            print("Pressed Red Button")

        if request.form['submit_button'] == 'ORANGE':
            print("Pressed Orange Button")

        if request.form['submit_button'] == 'YELLOW':
            print("Pressed Yellow Button")

        if request.form['submit_button'] == 'GREEN':
            print("Pressed Green Button")

        if request.form['submit_button'] == 'BLUE':
            print("Pressed Blue Button")

        if request.form['submit_button'] == 'INDIGO':
            print("Pressed Indigo Button")

        if request.form['submit_button'] == 'VIOLET':
            print("Pressed Violet Button")

        if request.form['submit_button'] == 'WHITE':
            print("Pressed White Button")

        if request.form['submit_button'] == 'ON':
            print("Pressed On Button")

        if request.form['submit_button'] == 'OFF':
            print("Pressed Off Button")

        if request.form['submit_button'] == 'RAINBOW':
            print("Pressed Rainbow Button")

        if request.form['submit_button'] == 'RAINBOW CYCLE':
            print("Press Rainbow Cycle Button")

        if request.form['submit_button'] == 'RGB TWINKLE':
            print("Press Rainbow Cycle Button")

        return render_template('control.html', form=form, color=color, brightness=brightness)

    elif request.method == 'PATCH':
        brightness = request.get_json(force=True)
        return make_response("OK", 200)

    else:
        return render_template('control.html', form=form, color=color, brightness=brightness)


@app.route('/colorpicker', methods=['GET', 'POST', 'PATCH'])
def color_picker():
    global brightness
    global color

    if request.method == 'PATCH':
        data = request.get_json(force=True)
        if len(data) == 1:
            setColor = data
            rgbColor = setColor.get("rgbColor")
            r = int(rgbColor[0])
            g = int(rgbColor[1])
            b = int(rgbColor[2])
            color_changer(r, g, b)
            return make_response("OK", 200)
        else:
            brightness = data
            new_brightness(brightness)
            return make_response("OK", 200)
    if request.method == 'GET':
        color = 'COLOR PICKER'
        event_object.set()
        event_object.clear()
        return render_template('colorpicker.html', form=form, color=color, brightness=brightness)
    if request.method == 'POST':
        event_object.set()
        color = request.form.get('submit_button')
        if request.form['submit_button'] == 'ON':
            print("Pressed On Button")
        if request.form['submit_button'] == 'OFF':
            print("Pressed Off Button")
        return render_template('colorpicker.html', form=form, color=color, brightness=brightness)


@app.route('/numberpattern', methods=['GET', 'PATCH'])
def numberpattern():
    global color

    if request.method == 'GET':
        color = 'NUMBER PATTERN'
        return render_template('numberpattern.html', color=color)


@app.route('/reds', methods=['GET', 'POST', 'PATCH'])
def reds():
    global color
    global brightness

    event_object.set()

    if request.method == 'POST':

        color = request.form.get('submit_button')

        if request.form['submit_button'] == 'RED':
            print("Pressed Red Button")

        if request.form['submit_button'] == 'CRIMSON':
            print("Pressed Crimson Button")

        if request.form['submit_button'] == 'VERMILION':
            print("Pressed Vermilion Button")

        if request.form['submit_button'] == 'RUBY':
            print("Pressed Ruby Button")

        if request.form['submit_button'] == 'PINK':
            print("Pressed Pink Button")

        if request.form['submit_button'] == 'HOT PINK':
            print("Pressed Hot Pink Button")

        if request.form['submit_button'] == 'DEEP PINK':
            print("Pressed Deep Pink Button")

        if request.form['submit_button'] == 'FUCHSIA PINK':
            print("Pressed Fuchsia Pink Button")

        if request.form['submit_button'] == 'ORANGE':
            print("Pressed Orange Button")

        if request.form['submit_button'] == 'ORANGERED':
            print("Pressed Orangered Button")

        if request.form['submit_button'] == 'YELLOW ORANGE':
            print("Pressed Yellow Orange Button")

        if request.form['submit_button'] == 'BURNT ORANGE':
            print("Press Burnt Orange Button")

        if request.form['submit_button'] == 'ON':
            print("Pressed On Button")

        if request.form['submit_button'] == 'OFF':
            print("Pressed Off Button")

        return render_template('reds.html', form=form, color=color, brightness=brightness)

    elif request.method == 'PATCH':
        brightness = request.get_json(force=True)
        return make_response("OK", 200)

    else:
        return render_template('reds.html', form=form, color=color, brightness=brightness)


@app.route('/blues', methods=['GET', 'POST', 'PATCH'])
def blues():
    global color
    global brightness

    event_object.set()

    if request.method == 'POST':

        color = request.form.get('submit_button')

        if request.form['submit_button'] == 'RED':
            print("Pressed Red Button")

        if request.form['submit_button'] == 'CRIMSON':
            print("Pressed Crimson Button")

        if request.form['submit_button'] == 'VERMILION':
            print("Pressed Vermilion Button")

        if request.form['submit_button'] == 'RUBY':
            print("Pressed Ruby Button")

        if request.form['submit_button'] == 'PINK':
            print("Pressed Pink Button")

        if request.form['submit_button'] == 'HOT PINK':
            print("Pressed Hot Pink Button")

        if request.form['submit_button'] == 'DEEP PINK':
            print("Pressed Deep Pink Button")

        if request.form['submit_button'] == 'FUCHSIA PINK':
            print("Pressed Fuchsia Pink Button")

        if request.form['submit_button'] == 'ORANGE':
            print("Pressed Orange Button")

        if request.form['submit_button'] == 'ORANGERED':
            print("Pressed Orangered Button")

        if request.form['submit_button'] == 'YELLOW ORANGE':
            print("Pressed Yellow Orange Button")

        if request.form['submit_button'] == 'BURNT ORANGE':
            print("Press Burnt Orange Button")

        if request.form['submit_button'] == 'ON':
            print("Pressed On Button")

        if request.form['submit_button'] == 'OFF':
            print("Pressed Off Button")

        return render_template('blues.html', form=form, color=color, brightness=brightness)

    elif request.method == 'PATCH':
        brightness = request.get_json(force=True)
        return make_response("OK", 200)

    else:
        return render_template('blues.html', form=form, color=color, brightness=brightness)


@app.route('/greens', methods=['GET', 'POST', 'PATCH'])
def greens():
    global color
    global brightness

    event_object.set()

    if request.method == 'POST':

        color = request.form.get('submit_button')

        if request.form['submit_button'] == 'RED':
            print("Pressed Red Button")

        if request.form['submit_button'] == 'CRIMSON':
            print("Pressed Crimson Button")

        if request.form['submit_button'] == 'VERMILION':
            print("Pressed Vermilion Button")

        if request.form['submit_button'] == 'RUBY':
            print("Pressed Ruby Button")

        if request.form['submit_button'] == 'PINK':
            print("Pressed Pink Button")

        if request.form['submit_button'] == 'HOT PINK':
            print("Pressed Hot Pink Button")

        if request.form['submit_button'] == 'DEEP PINK':
            print("Pressed Deep Pink Button")

        if request.form['submit_button'] == 'FUCHSIA PINK':
            print("Pressed Fuchsia Pink Button")

        if request.form['submit_button'] == 'ORANGE':
            print("Pressed Orange Button")

        if request.form['submit_button'] == 'ORANGERED':
            print("Pressed Orangered Button")

        if request.form['submit_button'] == 'YELLOW ORANGE':
            print("Pressed Yellow Orange Button")

        if request.form['submit_button'] == 'BURNT ORANGE':
            print("Press Burnt Orange Button")

        if request.form['submit_button'] == 'ON':
            print("Pressed On Button")

        if request.form['submit_button'] == 'OFF':
            print("Pressed Off Button")

        return render_template('greens.html', form=form, color=color, brightness=brightness)

    elif request.method == 'PATCH':
        brightness = request.get_json(force=True)
        return make_response("OK", 200)

    else:
        return render_template('greens.html', form=form, color=color, brightness=brightness)

    
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

    if color == "RAINBOW":
        rainbow(brightness)
    elif color == "RAINBOW CYCLE":
        rainbow_cycle(brightness)
    elif color == "RGB TWINKLE":
        rgb_twinkle(brightness)
    elif color == "RED":
        status_array = [brightness, 255, 0, 0]
        set_color(status_array)
        pass
    elif color == "ORANGE":
        status_array = [brightness, 255, 165, 0]
        set_color(status_array)
        pass
    elif color == "YELLOW":
        status_array = [brightness, 255, 255, 0]
        set_color(status_array)
        pass
    elif color == "GREEN":
        status_array = [brightness, 0, 255, 0]
        set_color(status_array)
        pass
    elif color == "BLUE":
        status_array = [brightness, 0, 0, 255]
        set_color(status_array)
        pass
    elif color == "INDIGO":
        status_array = [brightness, 75, 0, 130]
        set_color(status_array)
        pass
    elif color == "VIOLET":
        status_array = [brightness, 238, 130, 238]
        set_color(status_array)
        pass
    elif color == "WHITE":
        status_array = [brightness, 255, 255, 255]
        set_color(status_array)
        pass
    elif color == "ON":
        status_array = [brightness, 255, 255, 255]
        set_color(status_array)
        pass
    elif color == "OFF":
        status_array = [brightness, 0, 0, 0]
        set_color(status_array)
        pass
    elif color == "CRIMSON":
        status_array = [brightness, 220, 20, 60]
        set_color(status_array)
    elif color == "VERMILION":
        status_array = [brightness, 227, 66, 52]
        set_color(status_array)
    elif color == "RUBY":
        status_array = [brightness, 224, 17, 95]
        set_color(status_array)
    elif color == "PINK":
        status_array = [brightness, 255, 192, 203]
        set_color(status_array)
    elif color == "HOT PINK":
        status_array = [brightness, 255, 105, 180]
        set_color(status_array)
    elif color == "DEEP PINK":
        status_array = [brightness, 255, 20, 147]
        set_color(status_array)
    elif color == "FUCHSIA PINK":
        status_array = [brightness, 255, 119, 255]
        set_color(status_array)
    elif color == "ORANGERED":
        status_array = [brightness, 255, 69, 0]
        set_color(status_array)
    elif color == "YELLOW ORANGE":
        status_array = [brightness, 255, 174, 66]
        set_color(status_array)
    elif color == "BURNT ORANGE":
        status_array = [brightness, 204, 85, 0]
        set_color(status_array)
    else:
        print(f'Invalid color: {color}')

    print(f'{color} waiting')
    if color != "RAINBOW" and color != "RAINBOW CYCLE" and color != "RGB TWINKLE":
        event_object.wait()

    return Response(run_pattern())


def auto_on():
    global color

    event_object.set()
    color = "ON"


def auto_off():
    global color

    event_object.set()
    color = "OFF"


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



