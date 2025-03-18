from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = (
    "b339f8784e4baa72e389743af5b2ddbfa4271aa615838d7fec426f1aa6530955"
)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:engmso14789@localhost/flask1"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
loginManager.login_view = "login"
loginManager.login_message_category = "info"
from Blogger import routes
