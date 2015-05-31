from flask import Flask, render_template, request
from src.helper import validator


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form/', methods=['POST'])
def form():
    validator(request.form)
    return "hgjfg"



if __name__ == "__main__":
    app.debug = True
    app.run()