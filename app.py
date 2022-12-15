from flask import Flask
from flask import render_template, redirect, flash,request
from forms import LoginForm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

class CreateUserForm(FlaskForm):
    username = StringField(label=('Username'), 
        validators=[DataRequired(), 
        Length(max=64)])
    email = StringField(label=('Email'), 
        validators=[DataRequired(), 
        Email(), 
        Length(max=120)])
    password = PasswordField(label=('Password'), 
        validators=[DataRequired(), 
        Length(min=8, message='Password should be at least %(min)d characters long')])
    confirm_password = PasswordField(
        label=('Confirm Password'), 
        validators=[DataRequired(message='*Required'),
        EqualTo('password', message='Both password fields must be equal!')])

    receive_emails = BooleanField(label=('Receive merketting emails.'))

    submit = SubmitField(label=('Submit'))



app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'



@app.route('/', methods=('GET', 'POST'))
def index():
    form = CreateUserForm()
    if form.validate_on_submit():
        print("username=",request.form['username'])
        print("email=",request.form['email'])
        print("password=",request.form['password'])
        
    return render_template('index.html', form=form)




if __name__ == "__main__":

  app.run(debug = True,port=9000)