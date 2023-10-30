from flask import Flask, render_template, request
import subprocess
import os
import re
TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_cpp', methods=['POST'])
def run_cpp():
    m = request.form['m']
    n = request.form['n']
    starvcnt = request.form['starvcnt']
    result = subprocess.run(['./my_program', m, n, starvcnt], capture_output=True, text=True)
    output = result.stdout

    atb_count = output.count("A to B")
    bta_count = output.count("B to A")
    starvation_count = request.form['starvcnt']
    total_villagers = atb_count + bta_count

    return render_template('result.html', output=output, atb_count=atb_count, bta_count=bta_count, starvation_count=starvation_count, total_villagers=total_villagers)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
