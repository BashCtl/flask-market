from flask import Blueprint
from flask_login import login_required
from market.services.users_service import UserService

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register_page():
    return UserService.register_user()


@users.route("/login", methods=["GET", "POST"])
def login_page():
    return UserService.user_login()


@users.route("/logout")
def logout_page():
    return UserService.logout()



