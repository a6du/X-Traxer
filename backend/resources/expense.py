from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import ExpenseModel
from schemas import ExpenseSchema


blp = Blueprint("Expenses", "Expenses", description="Operations on expenses")


@blp.route("/expense/<string:expense_id>")
class Expense(MethodView):
    @blp.response(200, ExpenseSchema)
    def get(self, expense_id):
        expense = ExpenseModel.query.get_or_404(expense_id)
        return expense

    def delete(self, expense_id):
        expense = ExpenseModel.query.get_or_404(expense_id)
        db.session.delete(expense)
        db.session.commit()
        return {"message": "Expense deleted"}, 200


@blp.route("/expense")
class StoreList(MethodView):
    @blp.response(200, ExpenseSchema(many=True))
    def get(self):
        return ExpenseModel.query.all()

    @blp.arguments(ExpenseSchema)
    @blp.response(201, ExpenseSchema)
    def post(self, expense_data):
        expense = ExpenseModel(**expense_data)
        try:
            db.session.add(expense)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while adding the expense.")

        return expense