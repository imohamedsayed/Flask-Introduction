from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home', cssFile='home.css')

@app.route('/about')
def about():
    return render_template('about.html', title='about', cssFile='about.css')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='concat')

if __name__ == "__main__":
    app.run(debug=True)
