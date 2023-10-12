from flask import Blueprint
from flask_login import login_required
from market.services.market_service import MarketService
from market.decorators import admin_required

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
@admin_required
def admin_page():
    return MarketService.admin()


@market.route("/market/admin/new_item", methods=["GET", "POST"])
@login_required
@admin_required
def new_item():
    return MarketService.new_item()


@market.route("/market/admin/edit_item/<int:item_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_item(item_id):
    return MarketService.edit_item(item_id)


@market.route("/market/admin/delete_item/<int:item_id>", methods=["GET"])
@login_required
@admin_required
def delete_item(item_id):
    return MarketService.delete_item(item_id)
