#!/usr/bin/python
from flask import Flask,request,jsonify
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/root/tools/py_service/images/'

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/upload', methods = ['POST'])
def upload():
    if ('file' not in request.files) :
        if ('file' not in request.form) :
            fpath = None
        else :
            fpath = request.form.get('file')
    else :
        f = request.files['file']
        fpath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(fpath)

    try :
        if None == fpath :
            result = jsonify({"output" : "invalid param", "err" : 1})
        else :
            output = subprocess.check_output(["zbarimg", "-q", "--raw", fpath]).strip();
            result = jsonify({"output" : output, "err" : 0})
    except subprocess.CalledProcessError, e:
        result = jsonify({"output" : e.output, "err" : e.returncode})
    return result


if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0', debug=False)
