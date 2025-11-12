# Main Import Statements
from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response

# User Admin Import Statements
from controllers.useradmin.UserLoginController import UserLoginController
from controllers.useradmin.ViewUserAccController import ViewUserAccController
from controllers.useradmin.SearchUserAccController import SearchUserAccController
from controllers.useradmin.ViewProfileController import ViewProfileController
from controllers.useradmin.CreateUserAccController import CreateUserAccController
from controllers.useradmin.SuspendUserAccController import SuspendUserAccController
from controllers.useradmin.ReactivateUserAccController import ReactivateUserAccController

# Platform Manager Import Statements
from controllers.pm.ViewVolunteerCategoryController import ViewVolunteerCategoryController
from controllers.pm.DeleteVolunteerCategoryController import DeleteVolunteerCategoryController
from controllers.pm.SearchVolunteerCategoryController import SearchVolunteerCategoryController

# PIN Import Statements
from controllers.pin.ViewRequestController import ViewRequestController
from controllers.pin.DeleteRequestController import DeleteRequestController

# CSR Rep Import Statements
# from controllers.csrrep.XXXXX import XXXXController



app = Flask(__name__)
app.secret_key = 'abcedefg'  # Needed for flashing messages


@app.route("/")
def index():
    return redirect(url_for("login"))


# User Account Routes

@app.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    # Check is user is logged in
    if 'email' in session:
        if session['role_id'] == 1:
            return redirect(url_for('viewUserAccountPage'))
        if session['role_id'] == 2:
            return redirect(url_for('viewVolunteerCategoryPage'))
        if session['role_id'] == 3:
            return redirect(url_for('viewRequestsPage'))
        else:
            return redirect(url_for('other_dashboard'))
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
            if current_user.role_id == 3:
                return redirect(url_for('viewRequestPage'))
            if current_user.role_id == 3:
                return redirect(url_for('viewOpportunitiesPage'))
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
    if session['role_id'] != 1 and 'email' in session:
        return redirect(url_for('login'))

    user_keyword = (request.args.get('user_keyword') or "").strip()   # ← read the search text
    view_controller = ViewUserAccController()
    search_controller = SearchUserAccController()
    if not user_keyword:
        all_users = view_controller.viewUser()
    else:
        all_users = search_controller.searchUser(user_keyword)
    return render_template("useradmin/ViewUserAccountPage.html", users=all_users, user_keyword=user_keyword)

@app.route("/SuspendUserAccountPage", methods=["GET", "POST"])
def suspendUserAccountPage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 1 and 'email' in session:
        return redirect(url_for('login'))
    user_id = request.args.get('user_id')
    suspend_controller = SuspendUserAccController(user_id)
    print(user_id)
    suspend_controller.suspendUser(user_id)
    return redirect(url_for('viewUserAccountPage'))

@app.route("/ReactivateUserAccountPage", methods=["GET", "POST"])
def reactivateUserAccountPage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 1 and 'email' in session:
        return redirect(url_for('login'))
    user_id = request.args.get('user_id')
    reactivate_controller = ReactivateUserAccController(user_id)
    print(user_id)
    reactivate_controller.reactivateUser(user_id)
    return redirect(url_for('viewUserAccountPage'))
    
@app.route('/ViewUserProfilePage')
def viewUserProfilePage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 1 and 'email' in session:
        return redirect(url_for('login'))
    view_controller = ViewProfileController()
    profiles = view_controller.viewProfile()
    return render_template('useradmin/ViewUserProfilePage.html', profiles=profiles)

@app.route("/CreateUserAccountPage", methods=["GET", "POST"])
def createUserAccountPage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 1 and 'email' in session:
        return redirect(url_for('login'))
    if request.method == "GET":
        # Render the create dashboard page
        return render_template("useradmin/CreateUserAccountPage.html")
    # --- Handle form submission (POST request) ---
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()
    role_id = request.form.get("role_id", type=int)
    first_name = request.form.get("first_name", "").strip()
    last_name = request.form.get("last_name", "").strip()
    address = request.form.get("address", "").strip()
    phone = request.form.get("phone", "").strip()

    # --- Basic Validation ---
    if not (email and password and role_id and first_name and last_name):
        flash("Please fill in all required fields.")
        return redirect(url_for("createUserAccountPage"))

    try:
        result = CreateUserAccController.createUser(
            email=email,
            password=password,
            role_id=role_id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone
        )

        if result:
            flash("User account created successfully.")
            return redirect(url_for("viewUserAccountPage"))
        else:
            flash("Failed to create user account.")
            return redirect(url_for("createUserAccountPage"))

    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return redirect(url_for("createUserAccountPage"))
       

# Platform Manager Routes

@app.route("/ViewVolunteerCategoryPage", methods=["GET"])
def viewVolunteerCategoryPage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 2 and 'email' in session:
        return redirect(url_for('login'))

    category_keyword = (request.args.get('category_keyword') or "").strip()   # ← read the search text
    view_controller = ViewVolunteerCategoryController()
    search_controller = SearchVolunteerCategoryController()
    if not category_keyword:
        all_categories = view_controller.viewVolunteerCategory()
    else:
        all_categories = search_controller.searchVolunteerCategory(category_keyword)
    return render_template("pm/ViewVolunteerCategoryPage.html", categories=all_categories, category_keyword=category_keyword)

@app.route("/DeleteVolunteerCategoryPage", methods=["GET", "POST"])
def deleteVolunteerCategoryPage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 2 and 'email' in session:
        return redirect(url_for('login'))
    category_id = request.args.get('category_id')
    delete_controller = DeleteVolunteerCategoryController(category_id)
    print(category_id)
    delete_controller.deleteVolunteerCategory(category_id)
    return redirect(url_for('viewVolunteerCategoryPage'))
    

# Person In Need (PIN) Routes

@app.route("/ViewRequestPage", methods=["GET"])
def viewRequestPage():
    # --- Access control ---
    if 'email' not in session:
        return redirect(url_for('login'))
    # assuming role_id 3 = Person-In-Need (PIN)
    if session['role_id'] != 3:
        return redirect(url_for('login'))

    view_controller = ViewRequestController(session['user_id'])
    requests = view_controller.viewRequests(session['user_id'])
    return render_template("pin/ViewRequestsPage.html", requests=requests)

@app.route("/DeleteRequestPage", methods=["GET", "POST"])
def deleteRequestPage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 3 and 'email' in session:
        return redirect(url_for('login'))
    request_id = request.args.get('request_id')
    delete_controller = DeleteRequestController(request_id)
    delete_controller.deleteRequest(request_id)
    return redirect(url_for('viewRequestPage'))

@app.route("/ViewOpportunitiesPage", methods=["GET"])
def viewOpportunitiesPage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 4:  # Assuming CSR Rep
        return redirect(url_for('login'))

    controller = ViewVolunteerCategoryController()
    opportunities = controller.viewVolunteerCategory()

    return render_template("csr/ViewOpportunitiesPage.html", opportunities=opportunities)


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
bambi.berkely@volunteer.com  password123)) # PIN (active)
lawton.korfmann@volunteer.com  password123)) # UserAdmin
'''