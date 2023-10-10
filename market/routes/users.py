from flask import Blueprint
from market.services.users_service import UserService

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register_page():
    return UserService.register_user()
