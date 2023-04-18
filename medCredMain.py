# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://brianmporter:medCredPassword@localhost/medCredDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the borrower model
class Borrower(db.Model):
    __tablename__ = 'borrowers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    risk_score = db.Column(db.Integer, nullable=False)

# Define the physician model
class Physician(db.Model):
    __tablename__ = 'physicians'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    medical_practice_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Define the loan model
class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    borrower_id = db.Column(db.Integer, db.ForeignKey('borrowers.id'), nullable=False)
    physician_id = db.Column(db.Integer, db.ForeignKey('physicians.id'), nullable=False)
    procedure_date = db.Column(db.Date, nullable=False)
    down_payment = db.Column(db.Integer, nullable=False)
    monthly_payment = db.Column(db.Integer, nullable=False)
    apr = db.Column(db.Float, nullable=False)

# Create the database tables
db.create_all()

# Define the loan estimate request API endpoint
@app.route('/loan-estimate', methods=['POST'])
def get_loan_estimate():
    data = request.get_json()
    credit_score = data['credit_score']
    annual_income = data['annual_income']
    max_monthly_payment = data['max_monthly_payment']
    
    # Perform calculations to generate loan estimate
    
    # Return loan estimate
    return jsonify({'loan_estimate': loan_estimate})

# Define the loan application API endpoint
@app.route('/loan-application', methods=['POST'])
def apply_for_loan():
    data = request.get_json()
    borrower_name = data['borrower_name']
    borrower_address = data['borrower_address']
    borrower_risk_score = data['borrower_risk_score']
    physician_id = data['physician_id']
    procedure_date = data['procedure_date']
    down_payment = data['down_payment']
    monthly_payment = data['monthly_payment']
    apr = data['apr']
    
    # Create a new borrower record
    borrower = Borrower(name=borrower_name, address=borrower_address, risk_score=borrower_risk_score)
    db.session.add(borrower)
    db.session.commit()
    
    # Create a new loan record
    loan = Loan(borrower_id=borrower.id, physician_id=physician_id, procedure_date=procedure_date, down_payment=down_payment, monthly_payment=monthly_payment, apr=apr)
    db.session.add(loan)
    db.session.commit()
    
    # Return loan application status
    return jsonify({'status': 'Application submitted successfully'})

