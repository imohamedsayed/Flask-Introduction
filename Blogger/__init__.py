from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import environ

app = Flask(__name__)

app.config["SECRET_KEY"] = (
    "b339f8784e4baa72e389743af5b2ddbfa4271aa615838d7fec426f1aa6530955"
)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
loginManager.login_view = "users.login"
loginManager.login_message_category = "info"

# import users, blogs, main blueprints
from Blogger.main.routes import main
from Blogger.users.routes import users
from Blogger.blogs.routes import blogs

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(blogs)
