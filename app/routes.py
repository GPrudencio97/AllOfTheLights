from flask import Flask, render_template, request
from app import app
import lights

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('red') == 'RED':
            lights.red()
        elif request.form.get('orange') == 'ORANGE':
            lights.orange()
        elif request.form.get('yellow') == 'YELLOW':
            lights.yellow()
        elif request.form.get('green') == 'GREEN':
            lights.green()
        elif request.form.get('blue') == 'BLUE':
            lights.blue()
        elif request.form.get('indigo') == 'INDIGO':
            lights.indigo()
        elif request.form.get('violet') == 'VIOLET':
            lights.violet()
        else:
            return "aLl Of ThE LiGhTs"
    elif request.method == 'GET':
        return render_template('index.html')

    return render_template("index.html")