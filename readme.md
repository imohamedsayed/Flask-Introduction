
# Flask Project Documentation

## What is Flask?
Flask is a lightweight web application framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

## Features
- Built-in development server and debugger
- RESTful request dispatching
- Jinja2 templating
- Secure cookies support
- Unit testing support
- Extensive documentation
- Google App Engine compatibility

## Prerequisites
- Python 3.7+
- pip (Python package installer)

## Installation
1. Create a virtual environment:

python -m venv venv


2. Activate the virtual environment:
- Windows:

venv\Scripts\activate

- Unix/MacOS:

source venv/bin/activate


3. Install Flask:

pip install flask


## Project Structure

my_flask_app/
├── static/
│   └── css/
│   └── js/
├── templates/
│   └── index.html
├── main.py
└── README.md


## Running the Application
1. Make sure your virtual environment is activated
2. Set the Flask application:
   - Windows:

   set FLASK_APP=app.py

   - Unix/MacOS:

   export FLASK_APP=app.py


3. Run the application:

flask run


The application will be available at `http://127.0.0.1:5000/`

## Development Mode
To enable debug mode:
- Windows:

set FLASK_ENV=development

- Unix/MacOS:

export FLASK_ENV=development


## Dependencies
Install all required packages:

pip install -r requirements.txt


## Testing
Run tests using:

python -m pytest


## API Documentation

GET /home
GET /
GET /about
GET /login
GET /register

POST /login
POST /register
