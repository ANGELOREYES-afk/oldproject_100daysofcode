from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
power = []
wifi = []
coffee = []
for ran in range(1, 5):
    power.append("💪"*ran)
    wifi.append("🔌"*ran)
    coffee.append("☕"*ran)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    select_rating = SelectField("coffee rating", choices=coffee, validators=[DataRequired()])
    select_wifi = SelectField("wifi rating", choices=wifi, validators=[DataRequired()])
    select_power = SelectField("coffee rating", choices=power, validators=[DataRequired()])
    url = StringField("location", validators=[DataRequired(), URL()])
    opening = StringField('Open', validators=[DataRequired()])
    closing = StringField('Close', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding="UTF8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.url.data},"
                           f"{form.opening.data},"
                           f"{form.closing.data},"
                           f"{form.select_rating.data},"
                           f"{form.select_wifi.data},"
                           f"{form.select_power.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="UTF8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        f = list_of_rows[0]
    return render_template('cafes.html', f=f, cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
