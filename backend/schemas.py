from marshmallow import Schema, fields


class ExpenseSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.DateTime(required=True, format='%d-%m-%Y %H:%M:%S')
    name = fields.Str(required=True)
    amount = fields.Float(required=True)
    note = fields.Str(required=False)
