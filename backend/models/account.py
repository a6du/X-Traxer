from db import db


class AccountModel(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    expenses = db.relationship("ExpenseModel", back_populates="account", lazy="dynamic")