from flask import render_template, flash, redirect, url_for
from Blogger.models import User, Blog
from Blogger.forms import RegistrationForm, LoginForm
from Blogger import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/", methods=["GET"])
def index():
    user = current_user
    return render_template("index.html", title="Home", cssFile="home.css", user=user)


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="about", cssFile="about.css")


@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html", title="concat")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f"Welcome {user.name}", "success")
            return redirect(url_for("index"))
        else:
            flash(f"Invalid Credentials", "danger")
    return render_template("login.html", title="login", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            password=hashed_password,
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.name.data}", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="register", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/blog/add")
@login_required
def addBlog():
    return render_template("add_blog.html", title="Add Blog")
