from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = "b339f8784e4baa72e389743af5b2ddbfa4271aa615838d7fec426f1aa6530955"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:engmso14789@localhost/flask1"

db = SQLAlchemy(app)


from Blogger import routes
