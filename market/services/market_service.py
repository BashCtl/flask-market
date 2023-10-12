from flask import flash, redirect, render_template, url_for, request
from flask_login import login_user, logout_user, current_user

from market import db
from market.models.item_model import Item
from market.webforms.webforms import PurchaseItemForm, SellItemForm, ItemForm


class MarketService:

    @staticmethod
    def home():
        return render_template("home.html")

    @staticmethod
    def market_page():
        purchase_form = PurchaseItemForm()
        selling_form = SellItemForm()
        if request.method == "POST":
            # Purchase Item Logic
            purchased_item = request.form.get("purchased_item")
            p_item_object = Item.query.filter_by(name=purchased_item).first()
            if p_item_object:
                if current_user.can_purchase(p_item_object):
                    p_item_object.buy(current_user)
                    flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$",
                          category="success")
                else:
                    flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}",
                          category="danger")
            # Sell Item Logic
            sold_item = request.form.get("sold_item")
            s_item_object = Item.query.filter_by(name=sold_item).first()
            if s_item_object:
                if current_user.can_sell(s_item_object):
                    s_item_object.sell(current_user)
                    flash(f"Congratulations! You sold {s_item_object.name}  back to market.",
                          category="success")
                else:
                    flash(f"Something went wrong with selling {s_item_object.name}", category="danger")

            return redirect(url_for("market.market_page"))

        if request.method == "GET":
            items = Item.query.filter_by(owner=None)
            owned_items = Item.query.filter_by(owner=current_user.id)
            return render_template("market.html", items=items, purchase_form=purchase_form, owned_items=owned_items,
                                   selling_form=selling_form)

    @staticmethod
    def admin():
        items = Item.query.all()
        return render_template("admin.html", items=items)

    @staticmethod
    def new_item():
        form = ItemForm()
        if request.method == "POST":
            item = Item(name=form.item_name.data, barcode=form.barcode.data,
                        price=form.price.data, description=form.description.data)
            db.session.add(item)
            db.session.commit()
            flash("Item successfully added.", category="success")
            return redirect(url_for("market.admin_page"))
        return render_template("new_item.html", form=form)

    @staticmethod
    def edit_item(item_id):
        form = ItemForm()
        item = Item.query.get_or_404(item_id)
        if form.validate_on_submit():
            item.name = form.item_name.data
            item.barcode = form.barcode.data
            item.price = form.price.data
            item.description = form.description.data
            db.session.commit()
            flash("Item successfully updated.", category="success")
            return redirect(url_for("market.admin_page"))
        form.item_name.data = item.name
        form.barcode.data = item.barcode
        form.price.data = item.price
        form.description.data = item.description
        return render_template("edit_item.html", form=form, item=item)

    @staticmethod
    def delete_item(item_id):
        item = Item.query.get_or_404(item_id)
        if current_user.is_admin:
            db.session.delete(item)
            db.session.commit()
            flash("Item Was Deleted!", category="success")
            return redirect(url_for("market.admin_page"))
