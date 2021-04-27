from flask import Flask, render_template, redirect, session, url_for, flash, request
from data.db_session import db_auth
from Model.accounts_service import create_user, login_user, get_profile
import os, sys

# create an application instance
# all requests it receives from clients to this object for handling
# we are instantiating a Flask object by passing __name__ argument to the Flask constructor.
# The Flask constructor has one required argument which is the name of the application package.
# Most of the time __name__ is the correct value. The name of the application package is used
# by Flask to find static assets, templates and so on
# and the secret key is used to create a user session
app = Flask(__name__)
app.secret_key = os.urandom(24)

graph = db_auth()

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
dir_path = os.path.dirname(os.path.realpath(__file__))

# get current app directory
basedir = os.path.abspath(os.path.dirname(__file__))


app.config['UPLOAD_FOLDER'] = dir_path + '/data/'


@app.route('/')
def index():
    logo_path=url_for('static', filename='img/clik.PNG')
    return render_template("home/index.html", img_clik=logo_path)

@app.route('/home/index', methods=['GET'])
def home_index():
    logo_full_path = dir_path+'/static/img/clik.PNG'
    return render_template("home/index.html", img_clik=logo_full_path)

@app.route('/accounts/register', methods=['GET'])
def register_get():
    return render_template("accounts/register.html")

# if a user registers with a name, email and password not in the system
# then the user is taken to login automatically
@app.route('/accounts/register', methods=['POST'])
def register_post():
    # Get the form data from register.html
    name = request.form.get('name')
    email = request.form.get('email').lower().strip()
    password = request.form.get('password').strip()
    confirm = request.form.get('confirm').strip()

    # Check for blank fields in the registration form
    if not name or not email  or not password or not confirm:
        flash("Please fill in all the registration fields", "error")
        return render_template("accounts/register.html", name=name, email=email, password=password, confirm=confirm)

    # Check if password and confirm match
    if password != confirm:
        flash("Passwords do not match")
        return render_template("accounts/register.html", name=name, email=email)

    # Create the user
    user = create_user(name, email, password)
    # Verify another user with the same email does not exist
    if not user:
        flash("A user with that email already exists.")
        return render_template("accounts/register.html", name=name, email=email)

    return redirect(url_for("profile_get"))


@app.route('/accounts/login', methods=['GET'])
def login_get():
    # Check if the user is already logged in.  if yes, redirect to profile page.
    if "usr" in session:
        return redirect(url_for("profile_get"))
        #return render_template("accounts/mypage.html")
    else:
        return render_template("accounts/login.html")


@app.route('/accounts/login', methods=['POST'])
def login_post():
    # Get the form data from login.html
    email = request.form['email']
    password = request.form['password']
    if not email or not password:
        return render_template("accounts/login.html", email=email, password=password)

    # Validate the user
    user = login_user(email, password)
    if not user:
        flash("No account for that email address or the password is incorrect", "error")
        return render_template("accounts/login.html", email=email, password=password)

    # Log in user and create a user session, redirect to user profile page.
    usr = request.form["email"]
    session["usr"] = usr
    return redirect(url_for("profile_get"))
\


@app.route('/accounts/profile', methods=['GET'])
def profile_get():
    # Make sure the user has an active session.  If not, redirect to the login page.
    if "usr" in session:
        usr = session["usr"]
        session["usr"] = usr
        user_profile = get_profile(usr)
        return render_template("accounts/index.html", user_profile=user_profile)
    else:
        return redirect(url_for("login_get"))


@app.route('/accounts/profile', methods=['POST'])
def profile_post():
    # Make sure the user has an active session.  If not, redirect to the login page.
    if "usr" in session:
        usr = session["usr"]
        session["usr"] = usr
        user_profile = get_profile(usr)
        return render_template("accounts/index.html", user_profile=user_profile)
    else:
        return redirect(url_for("login_get"))

@app.route('/accounts/mypage2', methods=['GET'])
def mypage2():
    # Make sure the user has an active session.  If not, redirect to the login page.
    #if "usr" in session:
     #   usr = session["usr"]
     #   session["usr"] = usr
     #   user_profile = get_profile(usr)
     #   return render_template("accounts/mypage.html", user_profile=user_profile)
   # else:
   #     return redirect(url_for("login_get"))
    return render_template("accounts/mypage2.html")


#@app.route('/accounts/mypage', methods=['POST'])
#def profile_post():
    # Make sure the user has an active session.  If not, redirect to the login page.
#    if "usr" in session:
#        usr = session["usr"]
#        session["usr"] = usr
#        user_profile = get_profile(usr)
#        return render_template("accounts/mypage.html", user_profile=user_profile)
#    else:
#        return redirect(url_for("login_get"))

@app.route('/accounts/logout')
def logout():
    session.pop("usr", None)
    flash("You have successfully been logged out.", "info")
    return redirect(url_for("login_get"))


if __name__ == '__main__':
    app.run(debug=True)
