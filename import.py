import csv
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from website import db, create_app
from website.models import Products

app=create_app()

def main():
    with app.app_context():
        f = open("products.csv")
        reader = csv.reader(f)
        for name, price, Acategory, Bcategory, description in reader:
            product = Products(name=name,price=price,Acategory=Acategory,Bcategory=Bcategory,description=description)
            db.session.add(product)
            print(f"Added product {name}, {price}, {Acategory}, {Bcategory},  {description}")
        db.session.commit()

if __name__ == "__main__":
    main()