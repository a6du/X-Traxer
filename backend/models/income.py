from db import db


class IncomeModel(db.Model):
    __tablename__ = "incomes"

    id = db.Column(db.Integer, primary_key=True)
    is_income = db.Column(db.String(80), unique=True, nullable=False)

    expenses = db.relationship("ExpenseModel", back_populates="income", lazy="dynamic")