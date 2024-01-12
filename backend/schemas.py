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

class PlainSpendingSchema(Schema):
    id = fields.Int(dump_only=True)
    is_spending = fields.Str(required=True)    

class PlainIncomeSchema(Schema):
    id = fields.Int(dump_only=True)
    is_income = fields.Str(required=True)   

class PlainAccountSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)  

class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()        

class ExpenseSchema(PlainExpenseSchema):
    category_id = fields.Int(required=False, load_only=True)
    category = fields.Nested(PlainCategorySchema(), dump_only=True)

    transaction_id = fields.Int(required=False, load_only=True)
    transaction = fields.Nested(PlainTransactionSchema(), dump_only=True)

    spending_id = fields.Int(required=False, load_only=True)
    spending = fields.Nested(PlainSpendingSchema(), dump_only=True)

    income_id = fields.Int(required=False, load_only=True)
    income = fields.Nested(PlainIncomeSchema(), dump_only=True)  

    account_id = fields.Int(required=False, load_only=True)
    account = fields.Nested(PlainAccountSchema(), dump_only=True)  

    tag_list = fields.List(fields.Int,required=False,load_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class ExpenseUpdateSchema(Schema):
    date = fields.DateTime(format='%d-%m-%Y %H:%M:%S')
    name = fields.Str()
    amount = fields.Float()
    note = fields.Str()

class CategorySchema(PlainCategorySchema):
    expenses = fields.List(fields.Nested(PlainExpenseSchema()), dump_only=True)

class TransactionSchema(PlainTransactionSchema):
    expenses = fields.List(fields.Nested(PlainExpenseSchema()), dump_only=True)

class SpendingSchema(PlainSpendingSchema):
    expenses = fields.List(fields.Nested(PlainExpenseSchema()), dump_only=True)    

class IncomeSchema(PlainIncomeSchema):
    expenses = fields.List(fields.Nested(PlainExpenseSchema()), dump_only=True)   

class AccountSchema(PlainAccountSchema):
    expenses = fields.List(fields.Nested(PlainExpenseSchema()), dump_only=True)

# class TagSchema(PlainTagSchema):
#     expenses = fields.List(fields.Nested(PlainExpenseSchema()), dump_only=True)

# class TagAndExpenseSchema(Schema):
#     message = fields.Str()
#     expense = fields.Nested(ExpenseSchema)
#     tag = fields.Nested(TagSchema)