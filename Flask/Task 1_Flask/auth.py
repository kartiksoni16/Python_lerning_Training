from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models import User, db

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        role = request.form.get("role", "user")
        password = request.form["password"]

        print(f"Form Input Role: {request.form.get('role')}")
        print(f"Final Stored Role: {role}")

        if role not in ["admin", "manager", "user"]:
            role = "user"

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already taken!", "danger")
            return redirect(url_for("auth.register"))

        new_user = User(username=username, email=email, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash(f"User {username} registered successfully as {role}!", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")
    
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("app_routes.dashboard"))
        else:
            flash("Incorrect username or password!", "danger")

    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "info")
    return redirect(url_for("auth.login"))
