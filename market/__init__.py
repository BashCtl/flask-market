from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor

from market.configs import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
ckeditor = CKEditor()
login_manager = LoginManager()
login_manager.login_view = "users.login_page"
login_manager.login_message_category = "info"


def create_app(app_configs=Config):
    app = Flask(__name__)
    app.config.from_object(app_configs)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)

    migrate = Migrate(app, db)

    from market.routers.market import market
    from market.routers.users import users
    from market.routers.errors import errors

    app.register_blueprint(market)
    app.register_blueprint(users)
    app.register_blueprint(errors)

    return app
