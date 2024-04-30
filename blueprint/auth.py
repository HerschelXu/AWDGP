import random
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash, session
from exts import mail, db
from flask_mail import Message
import string
from models import EmailVerifyModel
from .forms import RegisForm, LoginForm
from models import UserModel
from werkzeug.security import generate_password_hash, check_password_hash


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("email address not in database!")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                # cookie
                session['user_id'] = user.id
                return redirect("/")
            else:
                print('wrong password')
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))


@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@bp.route("/register", methods=['GET', 'POST'])
# form registration
def register():
    if request.method == 'GET':
        return render_template("regis.html")
    else:
        form = RegisForm(request.form)
        # print('Password:', form.password.data)
        # print('Confirm Password:', form.confirm_password.data)
        if form.validate():
            # return "success"
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            # return reason of fail in registration
            for fieldName, errorMessages in form.errors.items():
                for err in errorMessages:
                    flash(f"{fieldName}:{err}")
            return redirect(url_for("auth.register"))


@bp.route("/verify/email")
def get_email_verify():
    email = request.args.get("email")
    code = string.digits * 6
    captcha = random.sample(code, 6)
    captcha = "".join(captcha)
    message = Message(subject="This is your verification code", recipients=[email],
                      body=f"Your verification code is: {captcha}")
    mail.send(message)
    email_verify = EmailVerifyModel(email=email, captcha=captcha)
    db.session.add(email_verify)
    db.session.commit()
    return jsonify({"code": 200, "message": "", "data": None})

# @bp.route("/mail/test")
# def mail_test():
#     message = Message(subject="test", recipients=["23750564@student.uwa.edu.au"], body="test message")
#     mail.send(message)
#     return "success"
