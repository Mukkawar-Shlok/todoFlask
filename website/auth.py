# routes of authentication
from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        pass
    data = request.form
    print(data)
    return render_template("login.html",text="Testing")


@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"


@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method =='POST':
        name = request.form.get('userName')
        email = request.form.get('userEmail')
        password = request.form.get('userPass')
        passwordRepeat = request.form.get('userPassConfirm')
        print(name,email,password,passwordRepeat)

        if len(name)<2:
            flash("Name should be greater than 2 letter",category="error")
        elif len(email)<4:
            flash("Please put valid email",category="error")
        elif password != passwordRepeat:
            flash("Password do not match",category="error")
        elif len(password)<7:
            flash("Password should be greater than 7 letters",category="error")
        return render_template("sign_up.html")
    else:
        return render_template("sign_up.html")
        
