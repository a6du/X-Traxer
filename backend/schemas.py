from marshmallow import Schema, fields

class PlainExpenseSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.DateTime(required=True, format='%d-%m-%Y %H:%M:%S')
    name = fields.Str(required=True)
    amount = fields.Float(required=True)
    note = fields.Str(required=False)

class PlainCategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainTransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)    


class ExpenseSchema(PlainExpenseSchema):
    category_id = fields.Int(required=False, load_only=True)
    category = fields.Nested(PlainCategorySchema(), dump_only=True)
    transaction_id = fields.Int(required=False, load_only=True)
    transaction = fields.Nested(PlainTransactionSchema(), dump_only=True)

class ExpenseUpdateSchema(Schema):
    date = fields.DateTime(format='%d-%m-%Y %H:%M:%S')
    name = fields.Str()
    amount = fields.Float()
    note = fields.Str()

class CategorySchema(PlainCategorySchema):
    expenses = fields.List(fields.Nested(PlainExpenseSchema()), dump_only=True)

class TransactionSchema(PlainTransactionSchema):
    expenses = fields.List(fields.Nested(PlainExpenseSchema()), dump_only=True)