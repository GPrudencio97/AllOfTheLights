from flask import Flask, render_template, request
from app import app
import lights

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('color') == 'RED':
            lights.red()
        elif request.form.get('color') == 'ORANGE':
            lights.orange()
        elif request.form.get('color') == 'YELLOW':
            lights.yellow()
        elif request.form.get('color') == 'GREEN':
            lights.green()
        elif request.form.get('color') == 'BLUE':
            lights.blue()
        elif request.form.get('color') == 'INDIGO':
            lights.indigo()
        elif request.form.get('color') == 'VIOLET':
            lights.violet()
        else:
            return "aLl Of ThE LiGhTs"
    else: 
        lights.off()
    return render_template('index.html')

@app.route('/current', methods=['GET', 'POST'])
def current():
    if request.method == 'POST':
        if request.form.get('color') == 'RED':
            lights.red()
        elif request.form.get('color') == 'ORANGE':
            lights.orange()
        elif request.form.get('color') == 'YELLOW':
            lights.yellow()
        elif request.form.get('color') == 'GREEN':
            lights.green()
        elif request.form.get('color') == 'BLUE':
            lights.blue()
        elif request.form.get('color') == 'INDIGO':
            lights.indigo()
        elif request.form.get('color') == 'VIOLET':
            lights.violet()
        else:
            return "aLl Of ThE LiGhTs"
    elif request.method == 'GET':
        return render_template('index.html')