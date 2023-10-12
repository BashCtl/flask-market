from flask import Blueprint, render_template

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(403)
def access_error(e):
    return render_template("403.html"), 403


@errors.app_errorhandler(404)
def page_not_found_error(e):
    return render_template("404.html"), 404
