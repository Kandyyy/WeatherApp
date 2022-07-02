from flask import Flask, render_template
from Weather import Weather

app = Flask(__name__)
weather = Weather(url='')

@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True)