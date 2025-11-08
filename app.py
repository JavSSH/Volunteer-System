from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response
from controllers.UserLoginController import UserLoginController
from controllers.ViewUserAccController import ViewUserAccController
from controllers.ViewProfileController import ViewProfileController
from controllers.pm.ViewVolunteerCategoryController import ViewVolunteerCategoryController
from flask import render_template


app = Flask(__name__)
app.secret_key = 'abcedefg'  # Needed for flashing messages


@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    # Check is user is logged in
    if 'email' in session and session['role_id'] == 1:
        return redirect(url_for('viewUserAccountPage'))
    # Check if user credentials are valid
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        current_user = UserLoginController.login(email, password)
        if current_user != None:
            session['email'] = current_user.email
            session['user_id'] = current_user.user_id
            session['role_id'] = current_user.role_id
            if current_user.role_id == 1:
                return redirect(url_for('viewUserAccountPage'))
            if current_user.role_id == 2:
                return redirect(url_for('viewVolunteerCategoryPage'))
            return redirect(url_for('other_dashboard'))
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

@app.route("/ViewUserAccountPage", methods=["GET"])
def viewUserAccountPage():
    if 'email' not in session:
        return redirect(url_for('login'))

    user_keyword = (request.args.get('user_keyword') or "").strip()   # ← read the search text
    controller = ViewUserAccController()
    if not user_keyword:
        all_users = controller.viewUser()
    else:
        all_users = controller.searchUser(user_keyword)
    return render_template("useradmin/ViewUserAccountPage.html", users=all_users, user_keyword=user_keyword)

@app.route('/viewUserProfilePage/<int:user_id>')
def viewUserProfilePage(user_id):
    profiles = ViewProfileController.viewProfile(user_id)
    return render_template('useradmin/viewUserProfilePage.html', profiles=profiles)

@app.route("/ViewVolunteerCategoryPage", methods=["GET"])
def viewVolunteerCategoryPage():
    if 'email' not in session:
        return redirect(url_for('login'))

    category_keyword = (request.args.get('category_keyword') or "").strip()   # ← read the search text
    controller = ViewVolunteerCategoryController()
    if not category_keyword:
        all_categories = controller.viewVolunteerCategory()
    else:
        all_categories = controller.viewVolunteerCategory()
        # all_users = controller.searchVolunteerCategory(user_keyword)
    return render_template("pm/ViewVolunteerCategoryPage.html", categories=all_categories, category_keyword=category_keyword)

@app.route("/other_dashboard")
def other_dashboard():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

''' 
Example Login Credentials

latisha.brandle@volunteer.com  password123)) # CSR Rep
rhonda.bonnet@volunteer.com    password123)) # PM
kirsteni.demcik@volunteer.com  password123)) # PIN
lawton.korfmann@volunteer.com  password123)) # UserAdmin
'''