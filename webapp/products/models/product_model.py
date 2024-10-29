from users.models.db import db

class Product(db.Model):
    __tablename__ = 'products'

    ref = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=True)

    def __init__(self, ref, name, price, description):
        self.ref = ref
        self.name = name
        self.price = price
        self.description = description

