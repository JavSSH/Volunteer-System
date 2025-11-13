# Main Import Statements
from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response
import sqlite3

# User Admin Import Statements
from controllers.useradmin.UserLoginController import UserLoginController
from controllers.useradmin.CreateUserAccController import CreateUserAccController
from controllers.useradmin.ViewUserAccController import ViewUserAccController
from controllers.useradmin.UpdateUserAccController import UpdateUserAccController
from controllers.useradmin.SuspendUserAccController import SuspendUserAccController
from controllers.useradmin.ReactivateUserAccController import ReactivateUserAccController
from controllers.useradmin.SearchUserAccController import SearchUserAccController

from controllers.useradmin.CreateProfileController import CreateProfileController
from controllers.useradmin.ViewProfileController import ViewProfileController
from controllers.useradmin.UpdateProfileController import UpdateProfileController
from controllers.useradmin.SuspendProfileController import SuspendProfileController
from controllers.useradmin.ReactivateProfileController import ReactivateProfileController
from controllers.useradmin.SearchProfileController import SearchProfileController

# Platform Manager Import Statements
from controllers.pm.CreateVolunteerCategoryController import CreateVolunteerCategoryController
from controllers.pm.ViewVolunteerCategoryController import ViewVolunteerCategoryController
from controllers.pm.UpdateVolunteerCategoryController import UpdateVolunteerCategoryController
from controllers.pm.DeleteVolunteerCategoryController import DeleteVolunteerCategoryController
from controllers.pm.SearchVolunteerCategoryController import SearchVolunteerCategoryController
from controllers.pm.GenerateDailyReportController import GenerateDailyReportController
from controllers.pm.GenerateWeeklyReportController import GenerateWeeklyReportController
from controllers.pm.GenerateMonthlyReportController import GenerateMonthlyReportController

# PIN Import Statements
from controllers.pin.ViewRequestController import ViewRequestController
from controllers.pin.DeleteRequestController import DeleteRequestController
from controllers.pin.CreateRequestController import CreateRequestController
from controllers.pin.FilterCompletedRequests import FilterCompletedRequests
from controllers.pin.RequestShortlistController import RequestShortlistController
from controllers.pin.SearchCompletedRequestsController import SearchCompletedRequestsController
from controllers.pin.UpdateRequestController import UpdateRequestController
from controllers.pin.ViewCompletedRequestsController import ViewCompletedRequestsController

# CSR Rep Import Statements
from controllers.csrrep.ViewOpportunitiesDetailsController import ViewOpportunitiesDetailsController
from controllers.csrrep.SearchOpportunitiesController import SearchOpportunitiesController
from controllers.csrrep.ViewShortlistController import ViewShortlistController
from controllers.csrrep.ViewCompletedServicesController import ViewCompletedServicesController
from controllers.csrrep.SearchCompletedServicesController import SearchCompletedServicesController
from controllers.csrrep.SearchShortlistController import SearchShortlistController
from controllers.csrrep.AddToShortlistController import AddToShortlistController




app = Flask(__name__)
app.secret_key = 'abcedefg'  # Needed for flashing messages


@app.route("/")
def index():
    return redirect(url_for("login"))


# User Admin Routes

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
        if session['role_id'] == 4:
            return redirect(url_for('viewOpportunitiesPage'))
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
            if current_user.role_id == 4:
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

@app.route("/CreateUserAccountPage", methods=["GET", "POST"])
def createUserAccountPage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 1 and 'email' in session:
        return redirect(url_for('login'))
    
    if request.method == "GET":
        return render_template("useradmin/CreateUserAccountPage.html")
    
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()
    role_id = request.form.get("role_id", type=int)
    first_name = request.form.get("first_name", "").strip()
    last_name = request.form.get("last_name", "").strip()
    address = request.form.get("address", "").strip()
    phone = request.form.get("phone", "").strip()

    if not (email and password and role_id and first_name and last_name):
        flash("Please fill in all required fields.", "error")
        return redirect(url_for("createUserAccountPage"))

    try:
        create_controller = CreateUserAccController()
        result = create_controller.createUser(
            role_id=role_id,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone
        )

        if result:
            flash("User Account Created!", "success")
            return redirect(url_for("viewUserAccountPage"))
        else:
            flash("Email already exists. Please use a different email.", "error")
            return redirect(url_for("createUserAccountPage"))

    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for("createUserAccountPage"))


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
    
@app.route("/CreateProfilePage", methods=["GET", "POST"])
def createProfilePage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 1:
        return redirect(url_for('login'))

    if request.method == "GET":
        return render_template("useradmin/CreateProfilePage.html")

    role_name = request.form.get("role_name", "").strip()
    description = request.form.get("description", "").strip()

    if not (role_name and description):
        flash("Please fill in all required fields.", "error")
        return redirect(url_for("createProfilePage"))

    try:
        create_profile_controller = CreateProfileController()
        result = create_profile_controller.createProfile(
            role_name=role_name,
            description=description
        )

        if result:
            flash("Profile Created!", "success")
            return redirect(url_for("viewProfilePage"))
        else:
            flash("Role name already exists. Please use a different role name.", "error")
            return redirect(url_for("createProfilePage"))

    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for("createProfilePage"))

@app.route("/ViewProfilePage", methods=["GET"])
def viewProfilePage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 1:
        return redirect(url_for('login'))

    profile_keyword = (request.args.get('profile_keyword') or "").strip()  # read search input

    view_controller = ViewProfileController()
    search_controller = SearchProfileController()

    if not profile_keyword:
        profiles = view_controller.ViewProfile()
    else:
        profiles = search_controller.searchProfile(profile_keyword)

    return render_template("useradmin/ViewProfilePage.html", profiles=profiles, profile_keyword=profile_keyword)

@app.route("/SuspendProfilePage", methods=["GET", "POST"])
def suspendProfilePage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 1 and 'email' in session:
        return redirect(url_for('login'))
    role_id = request.args.get('role_id')
    suspend_controller = SuspendProfileController()
    suspend_result = suspend_controller.suspendProfile(role_id)
    if not suspend_result:
        flash("Can't suspend User Admin or Platform Manager!", "error")
    return redirect(url_for('viewProfilePage'))

@app.route("/ReactivateProfilePage", methods=["GET", "POST"])
def reactivateProfilePage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 1 and 'email' in session:
        return redirect(url_for('login'))
    role_id = request.args.get('role_id')
    reactivate_controller = ReactivateProfileController()
    reactivate_controller.reactivateProfile(role_id)
    return redirect(url_for('viewProfilePage'))
       

# Platform Manager Routes
@app.route("/CreateVolunteerCategoryPage", methods=["GET", "POST"])
def createVolunteerCategoryPage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 2:
        return redirect(url_for('login'))

    if request.method == "GET":
        return render_template("pm/CreateVolunteerCategoryPage.html")

    category_name = request.form.get("category_name", "").strip()
    category_desc = request.form.get("category_desc", "").strip()

    if not (category_name and category_desc):
        flash("Please fill in all required fields.", "error")
        return redirect(url_for("createVolunteerCategoryPage"))

    try:
        create_controller = CreateVolunteerCategoryController()
        result = create_controller.createVolunteerCategory(
            category_name=category_name,
            category_desc=category_desc
        )

        if result:
            flash("Volunteer Category Created!", "success")
            return redirect(url_for("viewVolunteerCategoryPage"))
        else:
            flash("Category name already exists. Please use a different name.", "error")
            return redirect(url_for("createVolunteerCategoryPage"))

    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for("createVolunteerCategoryPage"))

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

@app.route("/UpdateVolunteerCategoryPage/<int:category_id>", methods=["GET", "POST"])
def updateVolunteerCategoryPage(category_id):
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 2:
        return redirect(url_for('login'))

    update_controller = UpdateVolunteerCategoryController()

    if request.method == "GET":
        category = update_controller.getCategoryById(category_id)
        if not category:
            flash("Category not found", "error")
            return redirect(url_for("viewVolunteerCategoryPage"))
        return render_template("pm/UpdateVolunteerCategoryPage.html", category=category)

    # POST: get form data
    category_name = request.form.get("category_name", "").strip()
    category_desc = request.form.get("category_desc", "").strip()

    if not (category_name and category_desc):
        flash("Please fill in all required fields.", "error")
        return redirect(url_for("updateVolunteerCategoryPage", category_id=category_id))

    try:
        result = update_controller.updateVolunteerCategory(
            category_id=category_id,
            category_name=category_name,
            category_desc=category_desc
        )

        if result:
            flash("Volunteer Category Updated!", "success")
            return redirect(url_for("viewVolunteerCategoryPage"))
        else:
            flash("Category name already exists. Please use a different name.", "error")
            return redirect(url_for("updateVolunteerCategoryPage", category_id=category_id))

    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for("updateVolunteerCategoryPage", category_id=category_id))

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
    
@app.route("/ReportManagementPage", methods=["GET"])
def reportManagementPage():
    # --- Access control (PM only) ---
    if 'email' not in session:
        return redirect(url_for('login'))
    if session.get('role_id') != 2:   # 2 == Platform Manager
        return redirect(url_for('login'))

    # read filters from query string
    period       = (request.args.get("report_period") or "").strip()     # daily | weekly | monthly
    report_date  = (request.args.get("report_date") or "").strip()       # YYYY-MM-DD (daily / weekly)
    report_month = (request.args.get("report_month") or "").strip()      # YYYY-MM (monthly)
    limit        = request.args.get("limit", type=int)

    report_data = []
    error = None

    try:
        if period == "daily":
            if not report_date:
                error = "Please choose a date for the daily report."
            else:
                report_data = GenerateDailyReportController.generateDailyReport(report_date, limit)

        elif period == "weekly":
            if not report_date:
                error = "Please choose a start date for the weekly report."
            else:
                report_data = GenerateWeeklyReportController.generateWeeklyReport(report_date, limit)

        elif period == "monthly":
            if not report_month:
                error = "Please choose a month in YYYY-MM for the monthly report."
            else:
                report_data = GenerateMonthlyReportController.generateMonthlyReport(report_month, limit)

        elif period:  # invalid string passed
            error = "Invalid period. Use daily, weekly, or monthly."

    except Exception as e:
        error = f"Error generating report: {e}"

    if error:
        flash(error)

    # Render the management page (shows empty state if no params yet)
    return render_template(
        "pm/ReportManagementPage.html",
        report_data=report_data,
        report_period=period,
        report_date=report_date,
        report_month=report_month,
        limit=limit
    )

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

@app.route("/CreateRequestPage", methods=["GET", "POST"])
def createRequestPage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 3:
        return redirect(url_for('login'))

    if request.method == "GET":
        view_category_controller = ViewVolunteerCategoryController()
        all_categories = view_category_controller.viewVolunteerCategory()
        return render_template("pin/CreateRequestPage.html", categories=all_categories)

    # POST
    category_id = request.form.get("category_id", type=int)
    if not category_id:
        flash("Please select a category.", "error")
        return redirect(url_for("createRequestPage"))

    try:
        create_controller = CreateRequestController(session['user_id'])
        result = create_controller.createRequest(category_id)

        if result:
            flash("Request created successfully!", "success")
            return redirect(url_for("viewRequestPage"))
        else:
            flash("Failed to create request.", "error")
            return redirect(url_for("createRequestPage"))

    except Exception as e:
        flash(f"An error occurred while creating the request: {str(e)}", "error")
        return redirect(url_for("createRequestPage"))

@app.route("/UpdateRequestPage/<int:request_id>", methods=["GET", "POST"])
def updateRequestPage(request_id):
    if 'email' not in session:
        return redirect(url_for('login'))
    if session.get('role_id') != 3:
        return redirect(url_for('login'))

    update_controller = UpdateRequestController()

    if request.method == "GET":
        req_obj = update_controller.getRequestById(request_id)
        if not req_obj:
            flash("Request not found", "error")
            return redirect(url_for("viewRequestPage"))

        categories = ViewVolunteerCategoryController().viewVolunteerCategory()
        return render_template(
            "pin/UpdateRequestPage.html",
            request=req_obj,
            categories=categories
        )

    # POST
    category_id = request.form.get("category_id", type=int)
    if not category_id:
        flash("Please select a category.", "error")
        return redirect(url_for("updateRequestPage", request_id=request_id))

    ok = update_controller.updateRequest(category_id, request_id)

    if ok:
        flash("Request updated!", "success")
    else:
        flash("Update failed or no changes made.", "error")

    return redirect(url_for("viewRequestPage"))

@app.route("/ViewCompletedRequestsPage", methods=["GET", "POST"])
def viewCompletedRequestsPage():
    # For now, skip login and hardcode a test user id
    pin_user_id = 1

    view_completed_requests_controller = ViewCompletedRequestsController()
    completed_requests = view_completed_requests_controller.viewCompletedRequests(pin_user_id)

    # If you *just* want to display completed requests for now:
    return render_template(
        "pin/ViewCompletedRequestsPage.html",
        completed_requests=completed_requests
    )


 
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


# CSR Rep Routes

@app.route("/ViewOpportunitiesPage", methods=["GET"])
def viewOpportunitiesPage():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 4:  # Assuming CSR Rep
        return redirect(url_for('login'))

    view_controller = ViewOpportunitiesDetailsController()
    opportunities = view_controller.viewOpportunitiesDetails()

    search_controller = SearchOpportunitiesController()
    keyword = (request.args.get('opportunity_keyword') or "").strip()
    search = search_controller.searchOpportunities(keyword)
    rows = search if keyword else opportunities

    # request_id = (request.args.get('request_id') or "").strip()
    # shortlist_controller = AddToShortlistController()
    # shortlist = shortlist_controller.addToShortlist(request_id)

    return render_template("csr/ViewOpportunitiesPage.html", opportunities=opportunities , rows=rows, keyword=keyword )

@app.route("/ViewOpportunitiesPage", methods=["GET", "POST"])
def addToShortlist():
    if 'email' not in session:
        return redirect(url_for('login'))
    if session['role_id'] != 4:  # Assuming CSR Rep
        return redirect(url_for('login'))
    
    request_id = (request.args.get('request_id') or "").strip()
    shortlist_controller = AddToShortlistController()
    shortlist = shortlist_controller.addToShortlist(request_id)
    print(request_id)
    print(shortlist)
    flash("Added to shortlist!", "success")

    return render_template("csr/ViewOpportunitiesPage.html", opportunity_keyword=shortlist)


@app.route("/other_dashboard")
def other_dashboard():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)


''' 
Example Login Credentials

latisha.brandle@volunteer.com  password123)) # CSR Rep (4)
rhonda.bonnet@volunteer.com    password123)) # PM (2)
kirsteni.demcik@volunteer.com  password123)) # PIN
bambi.berkely@volunteer.com  password123)) # PIN (active) (3)
lawton.korfmann@volunteer.com  password123)) # UserAdmin (1)
'''