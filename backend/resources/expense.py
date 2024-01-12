from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import ExpenseModel, CategoryModel, TransactionModel
from schemas import ExpenseSchema, ExpenseUpdateSchema


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
    
    @blp.arguments(ExpenseUpdateSchema)
    @blp.response(200, ExpenseSchema)
    def put(self, expense_data, expense_id):
        expense = ExpenseModel.query.get(expense_id)

        if expense:
            expense.amount = expense_data["amount"]
            expense.name = expense_data["name"]
            expense.date = expense_data["date"]
            expense.note= expense_data["note"]

        else:
            expense = ExpenseModel(id=expense_id, **expense_data)

        db.session.add(expense)
        db.session.commit()

        return expense


@blp.route("/expense")
class ExpenseList(MethodView):
    @blp.response(200, ExpenseSchema(many=True))
    def get(self):
        return ExpenseModel.query.all()

    @blp.arguments(ExpenseSchema)
    @blp.response(201, ExpenseSchema)
    def post(self, expense_data):
        
        try:
            category_id = expense_data["category_id"]
            transaction_id = expense_data["transaction_id"]
            expense = CategoryModel.query.get_or_404(category_id)
            expense = TransactionModel.query.get_or_404(transaction_id)
            expense = ExpenseModel(**expense_data)
        except:
            expense = ExpenseModel(**expense_data)

        try:
            db.session.add(expense)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while adding the expense.")

        return expense
    