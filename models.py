from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    risk_score = db.Column(db.Float, nullable=False)

class Physician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    medical_practice_name = db.Column(db.String(256), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(128), nullable=False)

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    physician_id = db.Column(db.Integer, db.ForeignKey('physician.id'), nullable=False)
    procedure_date = db.Column(db.DateTime, nullable=False)
    down_payment = db.Column(db.Float, nullable=False)
    monthly_payment = db.Column(db.Float, nullable=False)
    apr = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(128), nullable=False)
