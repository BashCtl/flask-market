from flask import flash, redirect, render_template, url_for
from flask_login import login_user

from market import db
from market.models.user_model import User
from market.webforms.webforms import RegisterForm


class UserService:

    @staticmethod
    def register_user():
        form = RegisterForm()
        if form.validate_on_submit():
            user_to_create = User(username=form.username.data,
                                  email_address=form.email_address.data,
                                  password=form.password1.data)
            db.session.add(user_to_create)
            db.session.commit()
            login_user(user_to_create)
            flash(f"Account created successfully! You are now logged in as {user_to_create.username}.",
                  category="success")
            return redirect(url_for("market_page"))
        if form.errors != {}:
            for err_msg in form.errors.values():
                flash(f"There was an error with creating a user: {err_msg}", category="danger")
        return render_template("register.html", form=form)
