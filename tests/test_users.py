from market.models.user_model import User


def test_home_page(client):
    response = client.get("/")
    assert b"Welcome to the Flask Market" in response.data


def test_valid_registration(client, app, user_data):
    response = client.post("/register", data=user_data, follow_redirects=True)
    with app.app_context():
        assert b"Account created successfully!" in response.data
        assert User.query.count() == 1
        assert User.query.first().username == user_data["username"]


def test_valid_login(client, register_user, user_data):
    response = client.post("/login", data={"username": user_data["username"],
                                           "password": user_data["password1"]}, follow_redirects=True)
    assert b"Success! You are logged in as:" in response.data