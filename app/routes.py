import logging
import time
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
state = 'SOLID'
speed = 'MEDIUM'
color1 = 'NONE'
color2 = 'NONE'
color3 = 'NONE'
color4 = 'NONE'
pattern = 1


@app.route('/', methods=['GET', 'POST', 'PATCH'])
@app.route('/index', methods=['GET', 'POST', 'PATCH'])
def index():
    global z
    global color
    global brightness

    if z is True:
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
    global state
    global speed

    event_object.set()

    if request.method == 'POST':

        if request.form.get('submit_button'):
            color = request.form.get('submit_button')
            print(f'Pressed {color} button')
        elif request.form.get('state_button'):
            state = request.form.get('state')
            print(f'The current state is {state}')
        elif request.form.get('speed_button'):
            speed = request.form.get('speed')
            print(f'The current speed is now {speed}')

        return render_template('control.html', form=form, color=color, brightness=brightness, state=state, speed=speed)

    elif request.method == 'PATCH':
        brightness = request.get_json(force=True)
        return make_response("OK", 200)

    else:
        return render_template('control.html', form=form, color=color, brightness=brightness, state=state)


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


@app.route('/numberpattern', methods=['GET', 'POST', 'PATCH'])
def numberpattern():
    global color
    global brightness
    global color1
    global color2
    global pattern

    color = 'NUMBER PATTERN'

    event_object.set()

    if request.method == 'POST':
        pattern = request.form.get('pattern')
        color1 = request.form.get('color1')
        color2 = request.form.get('color2')
        return render_template('numberpattern.html', color=color, brightness=brightness, pattern=pattern, color1=color1,
                               color2=color2)
    elif request.method == 'PATCH':
        brightness = request.get_json(force=True)
        return make_response("OK", 200)
    else:
        return render_template('numberpattern.html', color=color, brightness=brightness)


@app.route('/reds', methods=['GET', 'POST', 'PATCH'])
def reds():
    global color
    global brightness
    global state

    event_object.set()

    if request.method == 'POST':

        if request.form.get('submit_button'):
            color = request.form.get('submit_button')
            print(f'Pressed {color} button')

        elif request.form.get('state_button'):
            state = request.form.get('state')
            print(f'The current state is {state}')

        return render_template('reds.html', form=form, color=color, brightness=brightness, state=state)

    elif request.method == 'PATCH':
        brightness = request.get_json(force=True)
        return make_response("OK", 200)

    else:
        return render_template('reds.html', form=form, color=color, brightness=brightness, state=state)


@app.route('/blues', methods=['GET', 'POST', 'PATCH'])
def blues():
    global color
    global brightness
    global state

    event_object.set()

    if request.method == 'POST':
        if request.form.get('submit_button'):
            color = request.form.get('submit_button')
            print(f'Pressed {color} button')

        elif request.form.get('state_button'):
            state = request.form.get('state')
            print(f'The current state is {state}')

        return render_template('blues.html', form=form, color=color, brightness=brightness, state=state)

    elif request.method == 'PATCH':
        brightness = request.get_json(force=True)
        return make_response("OK", 200)

    else:
        return render_template('blues.html', form=form, color=color, brightness=brightness, state=state)


@app.route('/greens', methods=['GET', 'POST', 'PATCH'])
def greens():
    global color
    global brightness
    global state

    event_object.set()

    if request.method == 'POST':

        if request.form.get('submit_button'):
            color = request.form.get('submit_button')
            print(f'Pressed {color} button')

        elif request.form.get('state_button'):
            state = request.form.get('state')
            print(f'The current state is {state}')

        return render_template('greens.html', form=form, color=color, brightness=brightness, state=state)

    elif request.method == 'PATCH':
        brightness = request.get_json(force=True)
        return make_response("OK", 200)

    else:
        return render_template('greens.html', form=form, color=color, brightness=brightness, state=state)


@app.route('/colorchase', methods=['GET', 'POST', 'PATCH'])
def color_chase():
    global color
    global brightness
    global speed
    global color3
    global color4

    event_object.set()
    color = 'COLOR CHASE'

    if request.method == 'PATCH':
        brightness = request.get_json(force=True)
        return make_response("OK", 200)
    elif request.method == 'POST':
        color3 = request.form.get('color1')
        color4 = request.form.get('color2')
        speed = request.form.get('speed')
        return render_template('colorchase.html', color=color, brightness=brightness, speed=speed,
                               color3=color3, color4=color4)
    else:
        color3 = "NONE"
        color4 = "NONE"
        return render_template('colorchase.html', color=color, brightness=brightness)


@app.route('/colorcycle', methods=['GET', 'POST'])
def colorcycle():
    global color
    global brightness
    global speed

    event_object.set()

    if request.method == 'PATCH':
        brightness = request.get_json(force=True)
        return make_response("OK", 200)
    elif request.method == 'POST':
        if request.form.get('submit_button'):
            color = request.form.get('submit_button')
            print(f'Pressed {color} button')
        elif request.form.get('speed_button'):
            speed = request.form.get('speed')
            print(f'The current speed is now {speed}')

    return render_template('colorcycle.html', color=color, brightness=brightness, speed=speed)

def run_pattern():
    global color
    global brightness
    global state
    global speed

    event_object.clear()

    print(f'{color} running')

    if color == "RAINBOW":
        rainbow(brightness)
    elif color == "RAINBOW CYCLE":
        rainbow_cycle(brightness)
    elif color == "RGB TWINKLE":
        rgb_twinkle(brightness)
    elif color == "RAINBOW THEATER CHASE":
        rainbow_theater_chase(brightness, speed)
    elif color == "RAINBOW CYCLE THEATER CHASE":
        rainbow_cycle_theater_chase(brightness, speed)
    elif color == "THEATER CHASE":
        theater_chase(brightness, speed)
    elif color == "COLOR CHASE":
        get_chase_colors()
    elif color == "NUMBER PATTERN":
        get_pattern_colors()
    elif color == "COLOR CYCLE":
        color_cycle(brightness, speed)
    elif color == "RANDOM CYCLE":
        random_cycle(brightness, speed)
    elif color == "RED":
        status_array = [brightness, state, 255, 0, 0]
        set_color(status_array)
        pass
    elif color == "ORANGE":
        status_array = [brightness, state, 255, 165, 0]
        set_color(status_array)
        pass
    elif color == "YELLOW":
        status_array = [brightness, state, 255, 255, 0]
        set_color(status_array)
        pass
    elif color == "GREEN":
        status_array = [brightness, state, 0, 128, 0]
        set_color(status_array)
        pass
    elif color == "BLUE":
        status_array = [brightness, state, 0, 0, 255]
        set_color(status_array)
        pass
    elif color == "INDIGO":
        status_array = [brightness, state, 75, 0, 130]
        set_color(status_array)
        pass
    elif color == "VIOLET":
        status_array = [brightness, state, 238, 130, 238]
        set_color(status_array)
        pass
    elif color == "WHITE":
        status_array = [brightness, state, 255, 255, 255]
        set_color(status_array)
        pass
    elif color == "ON":
        status_array = [brightness, state, 255, 255, 255]
        set_color(status_array)
        pass
    elif color == "OFF":
        status_array = [brightness, state, 0, 0, 0]
        set_color(status_array)
        pass
    elif color == "CRIMSON":
        status_array = [brightness, state, 220, 20, 60]
        set_color(status_array)
        pass
    elif color == "VERMILION":
        status_array = [brightness, state, 227, 66, 52]
        set_color(status_array)
        pass
    elif color == "RUBY":
        status_array = [brightness, state, 224, 17, 95]
        set_color(status_array)
        pass
    elif color == "PINK":
        status_array = [brightness, state, 255, 192, 203]
        set_color(status_array)
        pass
    elif color == "HOT PINK":
        status_array = [brightness, state, 255, 105, 180]
        set_color(status_array)
        pass
    elif color == "DEEP PINK":
        status_array = [brightness, state, 255, 20, 147]
        set_color(status_array)
        pass
    elif color == "FUCHSIA PINK":
        status_array = [brightness, state, 255, 119, 255]
        set_color(status_array)
        pass
    elif color == "ORANGERED":
        status_array = [brightness, state, 255, 69, 0]
        set_color(status_array)
        pass
    elif color == "YELLOW ORANGE":
        status_array = [brightness, state, 255, 174, 66]
        set_color(status_array)
        pass
    elif color == "BURNT ORANGE":
        status_array = [brightness, state, 204, 85, 0]
        set_color(status_array)
        pass
    elif color == "LIME":
        status_array = [brightness, state, 0, 255, 0]
        set_color(status_array)
        pass
    elif color == "FORESTGREEN":
        status_array = [brightness, state, 34, 139, 34]
        set_color(status_array)
        pass
    elif color == "DARKGREEN":
        status_array = [brightness, state, 0, 100, 0]
        set_color(status_array)
        pass
    elif color == "CARIBBEAN GREEN":
        status_array = [brightness, state, 0, 204, 153]
        set_color(status_array)
        pass
    elif color == "JADE":
        status_array = [brightness, state, 0, 168, 107]
        set_color(status_array)
        pass
    elif color == "AQUAMARINE":
        status_array = [brightness, state, 127, 255, 212]
        set_color(status_array)
        pass
    elif color == "TURQUOISE GREEN":
        status_array = [brightness, state, 160, 214, 180]
        set_color(status_array)
        pass
    elif color == "NEON GREEN":
        status_array = [brightness, state, 57, 255, 20]
        set_color(status_array)
        pass
    elif color == "UFO GREEN":
        status_array = [brightness, state, 60, 208, 112]
        set_color(status_array)
        pass
    elif color == "EMERALD":
        status_array = [brightness, state, 80, 200, 0]
        set_color(status_array)
        pass
    elif color == "MYRTLE":
        status_array = [brightness, state, 33, 66, 30]
        set_color(status_array)
        pass
    elif color == "ROYAL BLUE":
        status_array = [brightness, state, 65, 105, 225]
        set_color(status_array)
        pass
    elif color == "NAVY":
        status_array = [brightness, state, 0, 0, 128]
        set_color(status_array)
        pass
    elif color == "DEEP SKY BLUE":
        status_array = [brightness, state, 0, 191, 255]
        set_color(status_array)
        pass
    elif color == "ELECTRIC BLUE":
        status_array = [brightness, state, 125, 249, 255]
        set_color(status_array)
        pass
    elif color == "CYAN":
        status_array = [brightness, state, 0, 183, 235]
        set_color(status_array)
        pass
    elif color == "IMPERIAL BLUE":
        status_array = [brightness, state, 0, 35, 149]
        set_color(status_array)
        pass
    elif color == "PURPLE":
        status_array = [brightness, state, 128, 0, 128]
        set_color(status_array)
        pass
    elif color == "DARK SLATE BLUE":
        status_array = [brightness, state, 72, 61, 139]
        set_color(status_array)
        pass
    elif color == "LAVENDER":
        status_array = [brightness, state, 181, 126, 220]
        set_color(status_array)
        pass
    elif color == "AMETHYST":
        status_array = [brightness, state, 153, 102, 204]
        set_color(status_array)
        pass
    elif color == "ROYAL PURPLE":
        status_array = [brightness, state, 120, 81, 169]
        set_color(status_array)
        pass
    elif color == "NUMBER PATTERN":
        new_brightness(brightness)
        pass
    else:
        print(f'Invalid color: {color}')

    print(f'{color} waiting')
    if color != "RAINBOW" and color != "RAINBOW CYCLE" and color != "RGB TWINKLE" and color != "RAINBOW THEATER CHASE"\
            and color != "THEATER CHASE" and color != "COLOR CHASE" and color != "COLOR CYCLE" and color != "RANDOM CYCLE":
        event_object.wait()

    return Response(run_pattern())


def get_chase_colors():
    global brightness
    global speed
    global color3
    global color4

    color3 = color3
    color4 = color4

    if color3 == "RED":
        code1 = [255, 0, 0]
        pass
    elif color3 == "ORANGE":
        code1 = [255, 165, 0]
        pass
    elif color3 == "YELLOW":
        code1 = [255, 255, 0]
        pass
    elif color3 == "GREEN":
        code1 = [0, 128, 0]
        pass
    elif color3 == "BLUE":
        code1 = [0, 0, 255]
        pass
    elif color3 == "INDIGO":
        code1 = [75, 0, 130]
        pass
    elif color3 == "VIOLET":
        code1 = [238, 130, 238]
        pass
    else:
        code1 = [0, 0, 0]

    if color4 == "RED":
        code2 = [255, 0, 0]
        pass
    elif color4 == "ORANGE":
        code2 = [255, 165, 0]
        pass
    elif color4 == "YELLOW":
        code2 = [255, 255, 0]
        pass
    elif color4 == "GREEN":
        code2 = [0, 128, 0]
        pass
    elif color4 == "BLUE":
        code2 = [0, 0, 255]
        pass
    elif color4 == "INDIGO":
        code2 = [75, 0, 130]
        pass
    elif color4 == "VIOLET":
        code2 = [238, 130, 238]
        pass
    else:
        code2 = [0, 0, 0]

    status_array = [brightness, speed, code1, code2]
    color_theater_chase(status_array)


def get_pattern_colors():
    global color1
    global color2
    global pattern
    global brightness

    color1 = color1
    color2 = color2

    if color1 == "RED":
        code1 = [255, 0, 0]
        pass
    elif color1 == "ORANGE":
        code1 = [255, 165, 0]
        pass
    elif color1 == "YELLOW":
        code1 = [255, 255, 0]
        pass
    elif color1 == "GREEN":
        code1 = [0, 128, 0]
        pass
    elif color1 == "BLUE":
        code1 = [0, 0, 255]
        pass
    elif color1 == "INDIGO":
        code1 = [75, 0, 130]
        pass
    elif color1 == "VIOLET":
        code1 = [238, 130, 238]
        pass
    else:
        code1 = [0, 0, 0]

    if color2 == "RED":
        code2 = [255, 0, 0]
        pass
    elif color2 == "ORANGE":
        code2 = [255, 165, 0]
        pass
    elif color2 == "YELLOW":
        code2 = [255, 255, 0]
        pass
    elif color2 == "GREEN":
        code2 = [0, 128, 0]
        pass
    elif color2 == "BLUE":
        code2 = [0, 0, 255]
        pass
    elif color2 == "INDIGO":
        code2 = [75, 0, 130]
        pass
    elif color2 == "VIOLET":
        code2 = [238, 130, 238]
        pass
    else:
        code2 = [0, 0, 0]

    status_array = [brightness, pattern, code1, code2]
    num_pattern(status_array)


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
