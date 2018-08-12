# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

from databases import add_student # Add functions you need from databases.py on this line!!

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
