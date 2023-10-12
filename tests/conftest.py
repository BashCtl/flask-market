import pytest
from dotenv import load_dotenv
from os import getenv, getcwd
from market import create_app, db
from market.models.user_model import User


class TestConfig:
    load_dotenv()
    SECRET_KEY = getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    WTF_CSRF_ENABLED = False


@pytest.fixture()
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def user_data():
    return dict(username="JohnDoe",
                email_address="john@test.com",
                password1="qwerty1234",
                password2="qwerty1234")


@pytest.fixture()
def register_user(app, user_data):
    with app.app_context():
        user = User(username=user_data["username"],
                    email_address=user_data["email_address"],
                    password=user_data["password1"])
        db.session.add(user)
        db.session.commit()
        return user
