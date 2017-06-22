from flask_blog import app, db
from flask import render_template, redirect, flash, url_for
from blog.form import SetupForm
from author.models import Author
from blog.models import Blog


@app.route('/admin')
def admin():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    return render_template('blog/admin.html')


@app.route('/setup', methods=['GET', 'POST'])
def setup():
    form = SetupForm()
    return render_template('blog/setup.html', form=form)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'
