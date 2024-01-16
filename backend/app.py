from flask import Flask
from flask_smorest import Api

# import models

from db import db
from resources.expense import blp as ExpenseBlueprint
from resources.category import blp as CategoryBlueprint
from resources.tag import blp as TagBlueprint

from models import TransactionModel, CategoryModel, SpendingModel, IncomeModel, AccountModel, TagModel

def create_app(db_url="postgresql://admin:your_password@postgres-db-1:5432/x_traxer"):
    app = Flask(__name__)
    app.config["API_TITLE"] = "X-Traxer REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        # db.drop_all()
        db.create_all()

        if not TransactionModel.query.all():
            transactions = [
                TransactionModel(name="DR"),
                TransactionModel(name="CR")
            ]
            db.session.add_all(transactions)

        if not CategoryModel.query.all():
            categories=[CategoryModel(name="Unknown"),
            CategoryModel(name="Food & Drinks"),
            CategoryModel(name="Tea & Snacks")
            ]
            db.session.add_all(categories)

        if not SpendingModel.query.all():
            spendings = [
                SpendingModel(is_spending="Yes"),
                SpendingModel(is_spending="-"),
                SpendingModel(is_spending="No")
            ]
            db.session.add_all(spendings)

        if not IncomeModel.query.all():
            incomes = [
                IncomeModel(is_income="Yes"),
                IncomeModel(is_income="-"),
                IncomeModel(is_income="No")
            ]
            db.session.add_all(incomes)

        if not AccountModel.query.all():        

            accounts=[AccountModel(name="SBI 9955"),
            AccountModel(name="ICICI 735"),
            AccountModel(name="ICICI credit 4009"),
            AccountModel(name="ICICI credit 1001")
            ]
            db.session.add_all(accounts)

        if not TagModel.query.all():
            tags=[TagModel(name="#Liked_It"),
            TagModel(name="#Hated_It")
            ]
            db.session.add_all(tags)


        db.session.commit()

    api.register_blueprint(ExpenseBlueprint)
    api.register_blueprint(CategoryBlueprint)
    api.register_blueprint(TagBlueprint)

    print("Hi")

    return app