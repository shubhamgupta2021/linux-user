from flask import Flask, render_template, request
from helper import validator
from userlib import UserHandler


app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form/', methods=['POST'])
def form():
    if validator(request.form):
        user = UserHandler(request.form['username'])
        if request.form['action'] == 'create':
            user.add(password=request.form['password'], shell=request.form['shell'], home_dir= request.form['directory'])
        if request.form['action'] == 'delete':
            user.delete()
        if request.form['action'] == 'modify':
            user.modify(password=request.form['password'], shell=request.form['shell'], home_dir= request.form['directory'])

        return "User Manipulation Successful"
    else:
        return "User Manipulation Failed"


if __name__ == "__main__":
    app.debug = True
    app.run()