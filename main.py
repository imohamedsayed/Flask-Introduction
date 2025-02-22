from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "b339f8784e4baa72e389743af5b2ddbfa4271aa615838d7fec426f1aa6530955"


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Home', cssFile='home.css')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='about', cssFile='about.css')

@app.route('/contact' , methods=['GET'])
def contact():
    return render_template('contact.html', title='concat')

@app.route('/login' , methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (form.email.data == 'mohamed@gmail.com' and form.password.data == '123456'):
            flash(f'Login Successful for {form.email.data}', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Invalid Credentials', 'danger')
    return render_template('login.html', title='login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.name.data}', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='register', form=form)

if __name__ == "__main__":
    app.run(debug=True)
