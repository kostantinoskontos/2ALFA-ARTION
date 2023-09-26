from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime, timedelta


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    orders = db.relationship('Order', backref='Costumer')

order_product = db.Table('order_product',
                         db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
                         db.Column('product_id', db.Integer, db.ForeignKey('poduct.id'), primary_key=True)
                         )

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    shipped_date = db.Column(db.DateTime)
    delivered_date = db.Column(db.DateTime)
    coupon_code = db.Column(db.String(50))
    costumer_id = db.Column(db.Integer, db.ForeignKey('costumer.id'), nullable=False)

    product = db.relationship('Product', secondary=order_product)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     category = db.Column(db.String(50))
#     price = db.Column(db.Float)
#     image = db.Column(db.String(120))
#     about = db.Column(db.String(50))
#     cart = db.relationship('Cart', backref="cart", lazy=True)
  
#     def toDict(self):
#       return{
#         'id':self.id,
#         'name':self.name,
#         'category':self.category,
#         'price':self.price,
#         'image':self.image,
#         'about':self.about,
#         'cart':[ product.toDict() for product in self.products]
#       }

# class Cart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     quantity = db.Column(db.Integer)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

#     def toDict(self):
#       return{
#         'id':self.id,
#         'quantity':self.quantity,
#         'product_id':self.product_id,
#         'product':self.product.toDict()
#       }
