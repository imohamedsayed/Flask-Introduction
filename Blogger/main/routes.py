from flask import render_template, Blueprint

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Home", cssFile="home.css")


@main.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="about", cssFile="about.css")


@main.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html", title="concat")
