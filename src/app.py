from flask import Flask, render_template, request
from helper import validator, validate_admin
from userlib import UserHandler
import sys


app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form/', methods=['POST'])
def form():
    validate_request = validator(request.form)
    if validate_request==200:
        user = UserHandler(request.form['username'])
        if request.form['action'] == 'create':
            user.add(password=request.form['password'], shell=request.form['shell'], home_dir= request.form['directory'])
        if request.form['action'] == 'delete':
            user.delete()
        if request.form['action'] == 'modify':
            user.modify(password=request.form['password'], shell=request.form['shell'], home_dir= request.form['directory'])

        return render_template("success.html")
    else:
        return render_template("error.html", context= {"error_code": validate_request, "action": request.form.get('action')})


if __name__ == "__main__":
    if validate_admin():
        app.debug = True
        app.run(host='0.0.0.0', port=5000)
    else:

        sys.exit(1)