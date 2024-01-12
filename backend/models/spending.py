from db import db


class SpendingModel(db.Model):
    __tablename__ = "spendings"

    id = db.Column(db.Integer, primary_key=True)
    is_spending = db.Column(db.String(80), unique=True, nullable=False)

    expenses = db.relationship("ExpenseModel", back_populates="spending", lazy="dynamic")