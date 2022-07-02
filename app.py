from flask import Flask, redirect, render_template,request,url_for
from Weather import Weather
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import os

class CityForm(FlaskForm):
    city = StringField('city', validators=[DataRequired()])


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/",methods=['GET','POST'])
def index():
    form = CityForm()
    if form.validate_on_submit():
        print(form.city.data)
        return redirect(url_for('index'))
    return render_template("index.html",form=form)

app.run(debug=True)