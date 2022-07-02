from flask import Flask, render_template,request,url_for
from Weather import Weather

app = Flask(__name__)
weather = Weather(url='')

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == "POST":
        city = request.form.get("city")
        print(city)
    return render_template("index.html")

app.run(debug=True)