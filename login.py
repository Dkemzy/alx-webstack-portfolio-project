# Import the necessary modules
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
import secrets

# Create the Flask app
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Add a secret key for flash messages

# Create the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.sqlite3'
db = SQLAlchemy(app)

# Create the user model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))

# Create the login manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists in the database
        user = User.query.filter_by(username=username).first()

        # If the user exists and the password is correct, log the user in
        if user and user.password == password:
            login_user(user)
            return redirect('/profile')  # Redirect to profile page

        # Otherwise, show an error message
        else:
            flash('Invalid username or password')

    return render_template('login.html')

# Define the logout route
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

# Define the profile route
@app.route('/profile')
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html')
    else:
        return redirect('/login')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
