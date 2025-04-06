
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    # Basic logic here - replace with database logic
    if username == "admin" and password == "1234":
        return "Welcome back, admin!"
    return "Invalid credentials."

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    # Save user info to database here (mocked)
    return f"Account created for {username}!"

if __name__ == '__main__':
    app.run(debug=True)
