from flask import Flask, render_template
from Weather import Weather
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

class CityForm(FlaskForm):
    city = StringField('city',validators=[DataRequired()])
    submit = SubmitField("Search")

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/",methods=['GET','POST'])
def index():
    form = CityForm()
    city = False
    contents = False
    link=False
    if form.validate_on_submit():
        city = form.city.data
        weather = Weather(url=f"SIKE")
        contents = weather.getWeather()
        link = "https://openweathermap.org/img/w/"+ contents[2]+".png"
        form.city.data = ""
    return render_template("index.html",form=form,city=city,contents=contents,link=link)


app.run(debug=True)