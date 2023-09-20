# routes of authentication
from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email = email).first()
        if(user):
            if check_password_hash(user.password, password):
                flash("logged in successfully!",category="success")
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password please try again",category="error")
        else:
            flash("User does not exists",category="error")
    # data = request.form
    # print(data)
    return render_template("login.html",user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login',user=current_user))


@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method =='POST':
        name = request.form.get('userName')
        email = request.form.get('userEmail')
        password = request.form.get('userPass')
        passwordRepeat = request.form.get('userPassConfirm')
        print(name,email,password,passwordRepeat)

        user = User.query.filter_by(email = email).first()

        if user:
            flash("User already exists",category="error")     
        elif len(name)<2:
            flash("Name should be greater than 2 letter",category="error")
        elif len(email)<4:
            flash("Please put valid email",category="error")
        elif password != passwordRepeat:
            flash("Password do not match",category="error")
        elif len(password)<7:
            flash("Password should be greater than 7 letters",category="error")
        else:
            new_user = User(email=email,name=name,password=generate_password_hash(password,method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("User Created Sucesfully",category="success")
            login_user(user,remember=True)
            return redirect(url_for('views.home'))
    return render_template("sign_up.html",user=current_user)
        
