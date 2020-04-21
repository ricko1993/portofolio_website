from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from .forms import ContactForm
import os


app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# sakrij kredencijale u env var...
app.config['MAIL_USERNAME'] = 'mijatovski@gmail.com'
app.config['MAIL_PASSWORD'] = 'qsvmyyttlsoiuvre'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# takodje i secret key...
app.config['SECRET_KEY'] = 'drowssap'

mail = Mail(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', contact=True)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST': 
        if form.validate_on_submit():      
            msg = Message(form.subject.data, sender='portofolio@mail.com', recipients=['mijatovski@gmail.com'])
            msg.body = f" From: {form.name.data} \n Email:  {form.email.data} \n Email Content: \n {form.message.data}"
            mail.send(msg)
            flash('You are successfully submited form', 'success')
            return render_template('contact_form.html', form=form, success=True)
        else:
            flash('Please check your credentials and all fields are required !!!', 'danger')
            return redirect(url_for('contact'))
    else:
        return render_template('contact_form.html', form=form)


if __name__=='__main__':
    app.run(host='192.168.1.100')