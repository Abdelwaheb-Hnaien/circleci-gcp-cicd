"""this iis the main program"""
from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)
#comment
@app.route('/')
def base():
    """base route"""
    return render_template("index.html")

@app.route('/rabbit')
def rabbit():
    """rabbit route"""
    return redirect("https://en.wikipedia.org/wiki/Rabbit")

@app.route('/go_home')
def home():
    """home route"""
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
