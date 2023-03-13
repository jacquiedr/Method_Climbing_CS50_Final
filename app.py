import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for, json
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from datetime import date

from helpers import apology, login_required

# Configure application
app = Flask(__name__)
# app.run(port=5000)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///mastery_log.db")

@app.route('/progression', methods =["GET"])
@login_required
def line_chart():
    user_id = session["user_id"]
    vb = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'VB'", user_id)[0]['COUNT(grade)']
    v0 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V0'", user_id)[0]['COUNT(grade)']
    v1 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V1'", user_id)[0]['COUNT(grade)']
    v2 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V2'", user_id)[0]['COUNT(grade)']
    v3 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V3'", user_id)[0]['COUNT(grade)']
    v4 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V4'", user_id)[0]['COUNT(grade)']
    v5 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V5'", user_id)[0]['COUNT(grade)']
    v6 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V6'", user_id)[0]['COUNT(grade)']
    v7 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V7'", user_id)[0]['COUNT(grade)']
    v8 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V8'", user_id)[0]['COUNT(grade)']
    v9 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V9'", user_id)[0]['COUNT(grade)']
    v10 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V10'", user_id)[0]['COUNT(grade)']
    v11 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V11'", user_id)[0]['COUNT(grade)']
    v12 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V12'", user_id)[0]['COUNT(grade)']
    v13 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V13'", user_id)[0]['COUNT(grade)']
    v14 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V14'", user_id)[0]['COUNT(grade)']
    v15 = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = 'V15'", user_id)[0]['COUNT(grade)']

    fiveone = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.1'", user_id)[0]['COUNT(grade)']
    fivetwo = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.2'", user_id)[0]['COUNT(grade)']
    fivethree = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.3'", user_id)[0]['COUNT(grade)']
    fivefour = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.4'", user_id)[0]['COUNT(grade)']
    fivefive = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.5'", user_id)[0]['COUNT(grade)']
    fivesix = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.6'", user_id)[0]['COUNT(grade)']
    fiveseven = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.7'", user_id)[0]['COUNT(grade)']
    fiveeight = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.8'", user_id)[0]['COUNT(grade)']
    fivenine = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.9'", user_id)[0]['COUNT(grade)']
    fivetenA = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.10a'", user_id)[0]['COUNT(grade)']
    fivetenB = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.10b'", user_id)[0]['COUNT(grade)']
    fivetenC = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.10c'", user_id)[0]['COUNT(grade)']
    fivetenD = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.10d'", user_id)[0]['COUNT(grade)']
    fiveelevenA = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.11a'", user_id)[0]['COUNT(grade)']
    fiveelevenB = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.11b'", user_id)[0]['COUNT(grade)']
    fiveelevenC = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.11c'", user_id)[0]['COUNT(grade)']
    fiveelevenD = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.11d'", user_id)[0]['COUNT(grade)']
    fiveTwelveA = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.12a'", user_id)[0]['COUNT(grade)']
    fiveTwelveB = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.12b'", user_id)[0]['COUNT(grade)']
    fiveTwelveC = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.12c'", user_id)[0]['COUNT(grade)']
    fiveTwelveD = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.12d'", user_id)[0]['COUNT(grade)']
    fiveThirteenA = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.13a'", user_id)[0]['COUNT(grade)']
    fiveThirteenB = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.13b'", user_id)[0]['COUNT(grade)']
    fiveThirteenC = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.13c'", user_id)[0]['COUNT(grade)']
    fiveThirteenD = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.13d'", user_id)[0]['COUNT(grade)']
    fiveFourteenA = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.14a'", user_id)[0]['COUNT(grade)']
    fiveFourteenB = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.14b'", user_id)[0]['COUNT(grade)']
    fiveFourteenC = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.14c'", user_id)[0]['COUNT(grade)']
    fiveFourteenD = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.14d'", user_id)[0]['COUNT(grade)']
    fiveFifteenA = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? and grade = '5.15a'", user_id)[0]['COUNT(grade)']

    vert = db.execute("SELECT COUNT(style) FROM session WHERE user_id = ? and style = 'Vert'", user_id)[0]['COUNT(style)']
    slab = db.execute("SELECT COUNT(style) FROM session WHERE user_id = ? and style = 'Slab'", user_id)[0]['COUNT(style)']
    roof = db.execute("SELECT COUNT(style) FROM session WHERE user_id = ? and style = 'Roof'", user_id)[0]['COUNT(style)']
    overhang = db.execute("SELECT COUNT(style) FROM session WHERE user_id = ? and style = 'Overhang'", user_id)[0]['COUNT(style)']

    summed = vert + slab + roof + overhang
    vert = (vert/summed) * 100
    slab = (slab/summed) * 100
    roof = (roof/summed) * 100
    overhang = (overhang/summed) * 100

    data = json.dumps( [vb,v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15] )
    data1 = json.dumps( [fiveone,fivetwo,fivethree,fivefour,fivefive,fivesix,fiveseven,fiveeight,fivenine,fivetenA,fivetenB,fivetenC,fivetenD,fiveelevenA,fiveelevenB,fiveelevenC,fiveelevenD,fiveTwelveA,fiveTwelveB,fiveTwelveC,fiveTwelveD, fiveThirteenA,fiveThirteenB,fiveThirteenC,fiveThirteenD,fiveFourteenA,fiveFourteenB,fiveFourteenC,fiveFourteenD,fiveFifteenA] )
    data2 = json.dumps( [round(vert, 2), round(slab, 2), round(roof, 2), round(overhang, 2)])
    labels = json.dumps( ['VB','V0','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15'] )
    labels1 = json.dumps(['5.1','5.2','5.3','5.4','5.5','5.6','5.7','5.8','5.9','5.10a','5.10b','5.10c','5.10d','5.11a','5.11b','5.11c','5.11d','5.12a','5.12b','5.12c','5.12d','5.13a','5.13b','5.13c','5.13d','5.14a','5.14b','5.14c','5.14d','5.15a'])
    labels2 = json.dumps(['Vert', 'Slab', 'Roof', 'Overhang'])
    return render_template("progression.html", data=data, labels=labels, data1=data1, labels1=labels1, data2=data2, labels2=labels2)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def main():
    return redirect("/account")


@app.route("/index")
@login_required
def index():
    user_id = session["user_id"]
    name = db.execute("SELECT firstName FROM users WHERE id = ?", user_id)[0]['firstName']
    goals = db.execute("SELECT * FROM goals WHERE user_id = ?", user_id)
    return render_template("index.html", goals=goals, name=name)


@app.route("/add", methods=["POST"])
@login_required
def add():
    goal = request.form['goal']
    user_id = session["user_id"]
    today = date.today()
    completion = False
    if goal == None or goal == '':
        return apology("please fill out field", 400)
    db.execute("INSERT INTO goals(user_id, goal, date, complete) VALUES(?, ?, ?, ?)", user_id, goal, today, completion)
    return redirect(url_for("index"))


@app.route("/edit/<int:index>", methods=["GET", "POST"])
@login_required
def edit(index):
    user_id = session["user_id"]
    goals = db.execute("SELECT * FROM goals WHERE user_id = ?", user_id)
    old_goal = goals[index]['goal']
    if request.method == 'POST':
        user_id = session["user_id"]
        goals = db.execute("SELECT * FROM goals WHERE user_id = ?", user_id)
        new_goal = request.form['goal']
        db.execute("UPDATE goals SET goal = ? WHERE user_id = ? AND goal = ?", new_goal, user_id, old_goal)
        return redirect(url_for("index"))
    else:
        goal = goals[index]['goal']
        return render_template("edit.html", old_goal=old_goal, goal=goal, index=index)


@app.route("/check/<int:index>")
@login_required
def check(index):
    user_id = session["user_id"]
    goals = db.execute("SELECT * FROM goals WHERE user_id = ?", user_id)
    goal = goals[index]['goal']
    completion = True
    db.execute("UPDATE goals SET complete = ? WHERE user_id = ? AND goal = ?", completion, user_id, goal)
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
@login_required
def delete(index):
    user_id = session["user_id"]
    goals = db.execute("SELECT * FROM goals WHERE user_id = ?", user_id)
    goal = goals[index]['goal']
    db.execute("DELETE FROM goals WHERE user_id = ? AND goal = ?", user_id, goal)
    return redirect(url_for("index"))


@app.route("/about", methods=["GET", "POST"])
def about():
    """About page, users can see w/o logging in"""

    if request.method == "POST":
        return apology("TODO", 400)
    else:
        return render_template("about.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get username field from HTML form
        username = request.form.get("username")

        # Get password field from HTML form
        password = request.form.get("password")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?;", (username, ))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], (password)):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User submitted register form
    if request.method == "POST" and "username" in request.form and "password" in request.form:

        # Retrieve user's first name
        firstName = request.form.get("firstName")

        # Retrieve user's last name from form
        lastName = request.form.get("lastName")

        # Retrieve user's country of origin from from
        country = request.form.get("country")

        # retrieve user's birthday
        birthday = request.form.get("birthday")

         # Get username field from HTML form
        username = request.form.get("username")

        # Get password field from HTML form
        password = request.form.get("password")

        if not username:
            return apology("must provide username and/or password", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide username and/or password", 400)

        # Search database for username that matches the username inputed
        accounts = db.execute("SELECT username FROM users WHERE username = ?;", (username, ))

        # If account already exists, return apology
        if accounts:
            return apology("username already taken", 400)

        # Make sure password contains at least one uppercase letter, one number, and a special character
        u, p, d = 0, 0, 0
        specialchar = "!@#$%^&*()-+?_=,<>/"
        digits = "0123456789"
        capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pw_len = len(password)
        if pw_len < 8:
            return apology("password must be at least 8 characters long, contain one uppercase letter, one number, and a special character", 400)

        for i in password:

            # counting uppercase alphabets
            if (i in capitalalphabets):
                u += 1

            # counting digits
            if (i in digits):
                d += 1

            # counting special chars
            if (i in specialchar):
                p += 1

        # checking if password meets requirements
        if (u < 1 or p < 1 or d < 1):
            return apology("password must be at least 8 characters long, contain one uppercase letter, one number, and a special character", 400)

        # Check if password and confirmation of password matches
        if password != request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        # Generate hash of password and input it in users table
        else:
            hash = generate_password_hash(password)
            db.execute("INSERT INTO users(username, hash, firstName, lastName, country, birthday) VALUES (?);", (username, hash, firstName, lastName, country, birthday))

            # Redirect user to home page
            return redirect("/")

    # Redirect user to register form
    return render_template("register.html")


@app.route("/logbook", methods=["GET", "POST"])
@login_required
def logbook():
    """ User can plan their training cycles here, add exercises... """

    if request.method == "POST":
        session_date = request.form.get("date")
        user_id = session["user_id"]
        sessions = db.execute("SELECT * FROM session WHERE user_id = ? AND date = ?", user_id, session_date)
        return render_template("session-overview.html", session_date=session_date, sessions=sessions)

    else:
        user_id = session["user_id"]
        firstName = db.execute("SELECT firstName FROM users WHERE id = ?", user_id)[0]['firstName']
        sessions = db.execute("SELECT * FROM session WHERE user_id = ?", user_id)
        climbs_sent = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ?", user_id)[0]['COUNT(grade)']
        total_sessions = db.execute("SELECT COUNT(DISTINCT date) FROM session WHERE user_id = ?;", user_id)[0]['COUNT(DISTINCT date)']
        session_day = db.execute("SELECT DISTINCT date FROM session WHERE user_id = ? ORDER BY date ASC", user_id)
        return render_template("logbook.html", firstName=firstName, climbs_sent=climbs_sent, session_day=session_day,total_sessions=total_sessions)


@app.route("/add-climb", methods=["GET", "POST"])
@login_required
def add_climb():
    """ User can add climbs to logbook"""
    if request.method == "POST":
        # Get user id
        user_id = session["user_id"]

        # Get inputed climb data from user
        date = request.form.get("session-date")
        if not date:
            return apology("must fill out all fields", 400)
        climb_type = request.form.get("type")
        if not climb_type:
            return apology("must fill out all fields", 400)
        grade = request.form.get("grade")
        if not grade:
            return apology("must fill out all fields", 400)
        ascent_type = request.form.get("type-ascent")
        if not ascent_type:
            return apology("must fill out all fields", 400)
        attempts = request.form.get("attempts")
        if not attempts:
            return apology("must fill out all fields", 400)
        style = request.form.get("style")
        if not style:
            return apology("must fill out all fields", 400)
        notes = request.form.get("notes")
        if not notes or notes == "":
            notes = ""

        db.execute("INSERT INTO session (user_id, date, type, grade, type, style, attempts, climb, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", user_id, date, climb_type, grade, ascent_type, style, attempts, ascent_type, notes)

        session_overview = db.execute("SELECT * FROM session WHERE user_id = ? AND date LIKE ?", user_id, date)
        return render_template("session-overview.html", session_date=date, sessions=session_overview)
    else:
        return render_template("add-climb.html")


@app.route("/session-overview", methods=["GET", "POST"])
@login_required
def session_overview():
    """ User can add climbs to logbook"""
    if request.method == "POST":
        return render_template("remove-climb.html")

    else:
        user_id = session["user_id"]
        date = db.execute("SELECT date FROM session WHERE user_id = ?", user_id)[0]['date']
        session_overview = db.execute("SELECT * FROM session WHERE user_id = ?", user_id)
        return render_template("session-overview.html", date=date, sessions=session_overview)


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    """ User can edit their account, view their goals... """
    if request.method == "GET":
        user_id = session["user_id"]
        username = db.execute("SELECT username FROM users WHERE id = ?", user_id)[0]['username']
        firstName = db.execute("SELECT firstName FROM users WHERE id = ?", user_id)[0]['firstName']
        lastName = db.execute("SELECT lastName FROM users WHERE id = ?", user_id)[0]['lastName']
        country = db.execute("SELECT country FROM users WHERE id = ?", user_id)[0]['country']
        birthday = db.execute("SELECT birthday FROM users WHERE id = ?", user_id)[0]['birthday']
        if birthday is None:
            birthday = ' '
        climbingstart = db.execute("SELECT climbingstart FROM users WHERE id = ?", user_id)[0]['climbingstart']
        if climbingstart is None:
            climbingstart = ' '
        occupation = db.execute("SELECT occupation FROM users WHERE id = ?", user_id)[0]['occupation']
        if occupation is None:
            occupation = ' '
        hobbies = db.execute("SELECT hobbies FROM users WHERE id = ?", user_id)[0]['hobbies']
        if hobbies is None:
            hobbies = ' '
        favorite = db.execute("SELECT favorite FROM users WHERE id = ?", user_id)[0]['favorite']
        if favorite is None:
            favorite = ' '
        goals = db.execute("SELECT goals FROM users WHERE id = ?", user_id)[0]['goals']
        if goals is None:
            goals = ' '

        return render_template("account.html", username=username, firstName=firstName, lastName=lastName, country=country, birthday=birthday, climbing_start=climbingstart, occupation=occupation, hobbies=hobbies, favorite=favorite,goals=goals)
    else:
        return render_template("edit-details.html")

@app.route("/edit-details", methods=["GET", "POST"])
@login_required
def edit_account():
    """ User can edit and update their account details from profile view page """
    # if user got to edit page from profile
    if request.method == "GET":

        # get all data from form based on user's id number
        user_id = session["user_id"]
        username = db.execute("SELECT username FROM users WHERE id = ?", user_id)[0]['username']
        firstName = db.execute("SELECT firstName FROM users WHERE id = ?", user_id)[0]['firstName']
        lastName = db.execute("SELECT lastName FROM users WHERE id = ?", user_id)[0]['lastName']
        country = db.execute("SELECT country FROM users WHERE id = ?", user_id)[0]['country']
        birthday = db.execute("SELECT birthday FROM users WHERE id = ?", user_id)[0]['birthday']
        climbing_start = db.execute("SELECT climbingstart FROM users WHERE id = ?", user_id)[0]['climbingstart']
        occupation = db.execute("SELECT occupation FROM users WHERE id = ?", user_id)[0]['occupation']
        interests = db.execute("SELECT hobbies FROM users WHERE id = ?", user_id)[0]['hobbies']
        favorite = db.execute("SELECT favorite FROM users WHERE id = ?", user_id)[0]['favorite']
        goals = db.execute("SELECT goals FROM users WHERE id = ?", user_id)[0]['goals']

        return render_template("edit-details.html",username=username, firstName=firstName, lastName=lastName, country=country, birthday=birthday, goals=goals, occupation=occupation, climbing_start=climbing_start, interests=interests,favorite=favorite)

    # if user is submitting information
    else:
        # get all data again
        user_id = session["user_id"]
        username = db.execute("SELECT username FROM users WHERE id = ?", user_id)[0]['username']
        firstName = db.execute("SELECT firstName FROM users WHERE id = ?", user_id)[0]['firstName']
        lastName = db.execute("SELECT lastName FROM users WHERE id = ?", user_id)[0]['lastName']
        country = db.execute("SELECT country FROM users WHERE id = ?", user_id)[0]['country']
        birthday = db.execute("SELECT birthday FROM users WHERE id = ?", user_id)[0]['birthday']
        climbing_start = db.execute("SELECT climbingstart FROM users WHERE id = ?", user_id)[0]['climbingstart']
        occupation = db.execute("SELECT occupation FROM users WHERE id = ?", user_id)[0]['occupation']
        interests = db.execute("SELECT hobbies FROM users WHERE id = ?", user_id)[0]['hobbies']
        favorite = db.execute("SELECT favorite FROM users WHERE id = ?", user_id)[0]['favorite']
        goals = db.execute("SELECT goals FROM users WHERE id = ?", user_id)[0]['goals']

        # check input and update if field is filled in

        firstNameNew = request.form.get("firstName")
        if firstNameNew == '' or (firstNameNew == firstName and firstNameNew != ''):
            firstNameNew = firstName
        elif firstNameNew != '':
            db.execute("UPDATE users SET firstName = ? WHERE id = ?", firstNameNew, user_id)

        lastNameNew = request.form.get("lastName")
        if lastNameNew == '' or (lastNameNew == lastName and lastNameNew != ''):
            lastNameNew = lastName
        elif lastNameNew != '':
            db.execute("UPDATE users SET lastName = ? WHERE id = ?", lastNameNew, user_id)

        country_new = request.form.get("country")
        if country_new == '' or (country_new == country and country_new != ''):
            country_new = country
        elif country_new != '':
            db.execute("UPDATE users SET country = ? WHERE id = ?", country_new, user_id)

        climbing_start_new = request.form.get("climbing_start")
        if climbing_start_new == '' or (climbing_start_new == climbing_start and climbing_start_new != ''):
            climbing_start_new = climbing_start
        elif climbing_start_new:
            db.execute("UPDATE users SET climbingstart = ? WHERE id = ?", climbing_start_new, user_id)

        occupation_new = request.form.get("occupation")
        if occupation_new == '' or (occupation_new == occupation and occupation_new != ''):
            occupation_new = occupation
        elif occupation_new != '':
            db.execute("UPDATE users SET occupation = ? WHERE id = ?", occupation_new, user_id)

        interests_new = request.form.get("interests")
        if interests_new == '' or (interests_new == interests and interests_new != ''):
            interests_new = interests
        elif interests_new != '':
            db.execute("UPDATE users SET hobbies = ? WHERE id = ?", interests_new, user_id)

        favorite_new = request.form.get("favorite")
        if favorite_new == '' or (favorite_new == favorite and favorite_new != ''):
            favorite_new = favorite
        elif favorite_new != '':
            db.execute("UPDATE users SET favorite = ? WHERE id = ?", favorite_new, user_id)

        goals_new = request.form.get("goals")
        if goals_new == '' or (goals_new == goals and goals_new != ''):
            goals_new = goals
        elif goals_new != '':
            db.execute("UPDATE users SET goals = ? WHERE id = ?", goals_new, user_id)

        flash("account info updated successfully")
        return redirect("/account")


@app.route("/edit-pass", methods=["GET", "POST"])
@login_required
def edit_pass():
    if request.method == "GET":
        return render_template("edit-pass.html")
    else:

        # get user ID
        user_id = session.get("user_id")

        # get user's new password and confirmation of pass
        password_new = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # ensure all fields have been filled out, or else return apology
        if not password_new or not confirmation:
            return apology("must fill out all fields", 400)

        # update password
        if password_new != '':

            # Make sure password contains at least one uppercase letter, one number, and a special character
            u, p, d = 0, 0, 0
            specialchar = "!@#$%^&*()-+?_=,<>/"
            digits = "0123456789"
            capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            pw_len = len(password_new)
            if pw_len < 8:
                return apology("password must be at least 8 characters long, contain one uppercase letter, one number, and a special character", 400)

            for i in password_new:

                # counting uppercase alphabets
                if (i in capitalalphabets):
                    u += 1

                # counting digits
                if (i in digits):
                    d += 1

                # counting special chars
                if (i in specialchar):
                    p += 1

            # checking if password meets requirements
            if (u < 1 or p < 1 or d < 1):
                return apology("password must be at least 8 characters long, contain one uppercase letter, one number, and a special character", 400)

            # Check if password and confirmation of password matches
            if password_new != request.form.get("confirmation"):
                return apology("passwords do not match", 400)

            # Generate hash of password and input it in users table
            else:
                hash = generate_password_hash(password_new)
                db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, user_id)
                flash("you have successfully changed your password")

            return redirect("/account")


@app.route("/delete-climb/<int:index>")
@login_required
def delete_climb(index):
    """ User can add climbs to logbook"""
    user_id = session["user_id"]
    sessions = db.execute("SELECT * FROM session WHERE user_id = ?", user_id)
    climb = sessions[index]['id']
    db.execute("DELETE FROM session WHERE user_id = ? AND id = ? LIMIT 1", user_id, climb)
    return redirect(url_for("logbook"))


@app.route("/progression")
def progression_graphs():
    sport_grades = [
        ("5.1"),
        ("5.2"),
        ("5.3"),
        ("5.4"),
        ("5.5"),
        ("5.6"),
        ("5.7"),
        ("5.8"),
        ("5.9"),
        ("5.10a"),
        ("5.10b"),
        ("5.10c"),
        ("5.10d"),
        ("5.11a"),
        ("5.11b"),
        ("5.11c"),
        ("5.11d"),
        ("5.12a"),
        ("5.12b"),
        ("5.12c"),
        ("5.12d"),
        ("5.13a"),
        ("5.13b"),
        ("5.13c"),
        ("5.13d"),
        ("5.14a"),
        ("5.14b"),
        ("5.14c"),
        ("5.14d"),
        ("5.15a"),
    ]
    # user_id = session["user_id"]
    # grades_sport = db.execute("SELECT COUNT(grade) FROM session WHERE user_id = ? AND type = 'Sport Climbing' AND grade = ?", user_id, values)
    # style_sport = db.execute("SELECT style FROM session WHERE user_id = ? and type = 'Sport Climbing", user_id)
    # grades_boulder = db.execute("SELECT grade FROM session WHERE user_id = ? type = 'Boulder", user_id)
    # style_boulder = db.execute("SELECT style FROM session WHERE user_id = ? and type = 'Boulder", user_id)
    return render_template("progression.html")