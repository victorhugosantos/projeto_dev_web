from app import db

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    availability = db.Column(db.String(50))

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)

class Distribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient_name = db.Column(db.String(100), nullable=False)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    distribution_date = db.Column(db.Date, nullable=False)
