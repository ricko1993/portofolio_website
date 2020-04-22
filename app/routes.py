from app import app, mail
from flask_mail import Mail, Message
from flask import Flask, render_template, request, flash, redirect, url_for
from app.forms import ContactForm


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
