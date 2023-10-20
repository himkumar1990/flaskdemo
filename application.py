from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/name", methods= ["GET"])
def hello_world():
    if request.method == "GET":
        return render_template('name.html')
    

@app.route("/greet", methods = ["POST"])
def greet():
    if request.method == "POST":
        username = request.form["name"]
        return render_template('greeting.html',user_name=username)


if __name__  == '__main__':
    app.debug = True
    app.run()