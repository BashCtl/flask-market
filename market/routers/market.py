from flask import Blueprint
from flask_login import login_required
from market.services.market_service import MarketService

market = Blueprint("market", __name__)


@market.route("/")
@market.route("/home")
def home_page():
    return MarketService.home()


@market.route("/market", methods=["GET", "POST"])
@login_required
def market_page():
    return MarketService.market_page()


@market.route("/market/admin")
@login_required
def admin_page():
    return MarketService.admin()

@market.route("/market/new_item")
@login_required
def add_product():
    return MarketService.add_product()
