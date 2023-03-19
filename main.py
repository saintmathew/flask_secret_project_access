from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    email = StringField(label='email', validators=[InputRequired(), Email()])
    password = PasswordField(label='Password', validators=[InputRequired(), Length(min=6)])
    submit = SubmitField(label="Log in")


app = Flask(__name__)
app.secret_key = "dragonlord"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = MyForm()
    if request.method == "POST":
        if login_form.validate_on_submit():
            if login_form.email.data == "admin@mail.com" and login_form.password.data == "12345678":
                return render_template("success.html")
            else:
                return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
