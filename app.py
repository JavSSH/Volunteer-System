from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response
from controllers.UserLoginController import UserLoginController
import sqlite3

app = Flask(__name__)
app.secret_key = 'abcedefg'  # Needed for flashing messages


@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    # Check is user is logged in
    if 'user' in session:
        return redirect(url_for('home'))
    # Check if user credentials are valid
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        current_user = UserLoginController.login(email, password)
        print("This is the debug ouput:", current_user)
        if current_user != None:
            session['user'] = current_user.email
            session['user_id'] = current_user.user_id
            return redirect(url_for('home'))
        else:
            flash("Incorrect email or password!")
            return redirect(url_for('login'))
    resp = make_response(render_template('login.html'))
    resp.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    resp.headers['Pragma'] = 'no-cache'
    resp.headers['Expires'] = '0'
    return resp

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/home")
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)