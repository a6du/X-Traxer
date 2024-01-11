from db import db


class TransactionModel(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    expenses = db.relationship("ExpenseModel", back_populates="transaction", lazy="dynamic")