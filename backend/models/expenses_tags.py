from db import db


class ExpensesTags(db.Model):
    __tablename__ = "expenses_tags"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("expenses.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))