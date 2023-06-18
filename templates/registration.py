import cgi
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the SQLAlchemy instance
db = SQLAlchemy()

# Create declarative base
Base = declarative_base()

# Define User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    password = Column(String(20))

# Create database engine and session
engine = db.create_engine('sqlite:///mydatabase.sqlite3', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('username')
password = form.getvalue('password')

# Perform registration logic
if username and password:
    # Check if user already exists
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        response_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Registration Response</title>
            <link rel="stylesheet" href="main.css">
        </head>
        <body>
            <h1>Registration Error</h1>
            <p>Username <strong>{username}</strong> is already taken.</p>
        </body>
        </html>
        """
        response_html = response_html.format(username=username)
    else:
        # Create a new user
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()

        response_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Registration Response</title>
            <link rel="stylesheet" href="main.css">
        </head>
        <body>
            <h1>Registration Successful</h1>
            <p>Thank you, <strong>{username}</strong>, for registering!</p>
        </body>
        </html>
        """
        response_html = response_html.format(username=username)
else:
    response_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Registration Error</title>
        <link rel="stylesheet" href="main.css">
    </head>
    <body>
        <h1>Registration Error</h1>
        <p>Please provide a valid username and password.</p>
    </body>
    </html>
    """

# Set content type to HTML
print("Content-type: text/html\n")
# Print the response HTML
print(response_html)