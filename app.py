from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response

import sqlite3

app = Flask(__name__)
app.secret_key = 'abcedefg'  # Needed for flashing messages


@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == "test@gmail.com" and password == "password123":
            session['user'] = email 
            return redirect(url_for('home'))
        else:
            flash("Incorrect email or password!")
            return redirect(url_for('login'))
    resp = make_response(render_template('login.html'))
    resp.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Expires'] = '0'
    return resp

@app.route("/home")
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)