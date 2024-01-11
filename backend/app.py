from flask import Flask
from flask_smorest import Api

# import models

from db import db
from resources.expense import blp as ExpenseBlueprint
from resources.category import blp as CategoryBlueprint
from models import TransactionModel, CategoryModel


def create_app(db_url=None):
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
        db.drop_all()
        db.create_all()

        transaction = TransactionModel(name="DR")
        db.session.add(transaction)
        transaction = TransactionModel(name="CR")
        db.session.add(transaction)

        category = CategoryModel(name="Unknown")
        db.session.add(category)        
        category = CategoryModel(name="Food & Drinks")
        db.session.add(category)
        category = CategoryModel(name="Tea & Snacks")
        db.session.add(category)

        db.session.commit()

    api.register_blueprint(ExpenseBlueprint)
    api.register_blueprint(CategoryBlueprint)

    return app