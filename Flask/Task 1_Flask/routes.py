from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models import User, db

app_routes = Blueprint("app_routes", __name__)

@app_routes.route("/")
def home():
    return redirect(url_for("app_routes.dashboard"))

@app_routes.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == "admin":
        users = User.query.all()
        return render_template("admin_dashboard.html", users=users, user=current_user)
    elif current_user.role == "manager":
        users = User.query.all()
        return render_template("manager_dashboard.html", users=users, user=current_user)
    else:
        return render_template("user_dashboard.html", user=current_user)
@app_routes.route("/admin/users/create", methods=["GET", "POST"])
@login_required
def create_user():
    if current_user.role not in ["admin", "manager"]:
        flash("Unauthorized access!", "danger")
        return redirect(url_for("app_routes.dashboard"))

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        role = request.form["role"]
        password = request.form["password"]

        new_user = User(username=username, email=email, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("User created successfully!", "success")
        return redirect(url_for("app_routes.dashboard"))

    return render_template("create_user.html")

@app_routes.route("/admin/users/update/<int:user_id>", methods=["GET", "POST"])
@login_required
def update_user(user_id):
    if current_user.role not in ["admin", "manager"]:
        flash("Unauthorized access!", "danger")
        return redirect(url_for("app_routes.dashboard"))

    user = User.query.get_or_404(user_id)

    if request.method == "POST":
        user.username = request.form["username"]
        user.email = request.form["email"]
        user.role = request.form["role"]
        if "password" in request.form and request.form["password"]:
            user.set_password(request.form["password"])

        db.session.commit()
        flash("User updated successfully!", "success")
        return redirect(url_for("app_routes.dashboard"))

    return render_template("edit_user.html", user=user)

@app_routes.route("/admin/users/delete/<int:user_id>", methods=["POST"])
@login_required
def delete_user(user_id):
    if current_user.role != "admin":
        flash("Unauthorized access!", "danger")
        return redirect(url_for("app_routes.dashboard"))

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    
    flash("User deleted successfully!", "success")
    return redirect(url_for("app_routes.dashboard"))

@app_routes.route("/user/edit", methods=["GET", "POST"])
@login_required
def edit_profile():
    user = User.query.get(current_user.id)
    
    if request.method == "POST":
        user.username = request.form["username"]
        user.email = request.form["email"]
        db.session.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for("app_routes.dashboard"))
    
    return render_template("edit_profile.html", user=user)
