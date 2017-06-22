from flask_blog import app
from flask import render_template, redirect, url_for, session
from author.form import RegisterForm, LoginForm
from author.models import Author


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('author/register.html',
                           form=form)


@app.route('/success')
def success():
    return "Author Registered!!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = ""

    if form.validate_on_submit():
        pass

    return render_template('author/login.html', form=form, error=error)

