from market.models import db, User, Item
from market import app

# u1 = User(username="jsc", password_hash="123456", email_address="jsc@jsc.com")
# i1 = Item(name="Iphone 12", barcode="234987645912", price=840, description="Iphone 12 description")
# i2 = Item(name="Laptop Lenovo Yoga", barcode="764987645912", price=750, description="Lenovo Yoga description")
# i3 = Item(name="Keyboard", barcode="894081645912", price=85, description="Keyboard description")

with app.app_context():
    db.create_all()
    # db.session.add(i1)
    # db.session.add(i2)
    # db.session.add(i3)
    # db.session.commit()
    item1 = Item.query.filter_by(name='Iphone 12').first()
    print(item1)
    item1.owner = User.query.filter_by(username='jsc').first().id
    db.session.add(item1)
    db.session.commit()
