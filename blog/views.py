from flask_blog import app, db
from flask import render_template, redirect, flash, url_for
from blog.form import SetupForm
from author.models import Author
from blog.models import Blog
from author.decorators import login_required
import bcrypt


@app.route('/')
@app.route('/index')
def index():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    return 'Hello World!'


@app.route('/admin')
@login_required
def admin():
    return render_template('blog/admin.html')


@app.route('/setup', methods=['GET', 'POST'])
def setup():
    form = SetupForm()
    error = ""
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        author = Author(
            fullname=form.fullname.data,
            email=form.email.data,
            username=form.username.data,
            password=hashed_password,
            is_author=True
        )
        db.session.add(author)
        db.session.flush()
        if author.id:
            blog = Blog(
                name=form.name.data,
                admin=author.id
            )
            db.session.add(blog)
            db.session.flush()

            if author.id and blog.id:
                db.session.commit()
                flash("Blog created")
                return redirect(url_for('admin'))
            else:
                db.session.rollback()
                error = "Error creating blog"

        else:
            db.session.rollback()
            error = "Error creating user"

    return render_template('blog/setup.html', form=form, error=error)

