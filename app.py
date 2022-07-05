from flask import Flask, make_response, redirect, render_template,request,url_for
from Weather import Weather
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

class CityForm(FlaskForm):
    city = StringField('city')
    submit = SubmitField("Search")

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/",methods=['GET','POST'])
def index():
    form = CityForm()
    city = False
    if form.validate_on_submit():
        city = form.city.data
        form.city.data = ""
    return render_template("index.html",form=form,city=city)


app.run(debug=True)