from flask_app import app
from flask import flash
from flask_app.models.user_model import User
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#DISPLAY LOGIN/REGISTER
# @app.route("/")
# def loginRegisterPage():
#     return render_template('login_register.html')


#REGISTER NEW PARENT-USER PROCESS
@app.route('/registration/process', methods=['POST'])
def registerUser():
# see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)

    if user_in_db:
        flash("Email already used")
        return redirect("/")

    if not User.validate_register(request.form):
        print('I am NOT validated!')
        return redirect('/')
    print('I am validated!')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])# create the hash
    print(pw_hash)
    
    data = {# put the pw_hash into the data dictionary
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_data = User.register_user(data)# Call the save @classmethod on User
    print(f"I have added you to the database, user {user_data}")
    # store user id into session
    session['user_id'] = user_data
    print(f"Your session is {session}")
    return redirect("/home")



#LOGIN PARENT-USER PROCESS
@app.route('/login/process', methods=['POST'])
def loginUser():

    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Email does not exist")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/paintings")


#LOGOUT USER
@app.route("/logout")
def logout():
    session.clear()
    print('Session Cleared')
    return redirect('/')


#CHOOSE PLAYER
@app.route("/home/clear")
def clearHome():
    session.clear()
    print('Session Cleared')
    return redirect('/home')

#DISPLAY HOME PAGE
@app.route("/home")
def homePage():

    # if not 'user_id' in session:
    #     flash("Please login first!")
    #     return render_template('login_register.html')

    # data = {
    #     'id':session['user_id']
    # }
    # userID = User.get_one_user(data) #doing this instead of parsing through data b/c i want the logged in user. not user associated with painting
    # return render_template('home.html', userID = userID)

    return render_template('home.html')