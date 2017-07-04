from flask_blog import app
from flask import render_template, redirect, url_for, session, request
from author.form import RegisterForm, LoginForm
from author.models import Author
from author.decorators import login_required
import bcrypt


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

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        authors = Author.query.filter_by(
            username=form.username.data
        ).limit(1)

        if authors.count():
            author = authors[0]
            if bcrypt.hashpw(
                    form.password.data,
                    author.password) == author.password:
                session['username'] = form.username.data
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return redirect(url_for('login_success'))
            else:
                error = "Incorrect username and password"
        else:
            error = "Incorrect username and password"

    return render_template('author/login.html', form=form, error=error)


@app.route('/login_success')
@login_required
def login_success():
    return "Author logged in!"


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))
