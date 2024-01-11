from db import db
from datetime import datetime


class ExpenseModel(db.Model):
    __tablename__ = "expenses"
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    amount = db.Column(db.Float(precision=2), unique=False, nullable=False)
    note = db.Column(db.String(80), unique=False, nullable=True)

    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.id"), unique=False, nullable=True, default = 1
    )
    transaction_id = db.Column(
        db.Integer, db.ForeignKey("transactions.id"), unique=False, nullable=True, default=1
    )
    
    category = db.relationship("CategoryModel", back_populates="expenses")
    transaction = db.relationship("TransactionModel", back_populates="expenses")

