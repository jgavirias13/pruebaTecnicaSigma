from marshmallow import fields
from app.ext import ma

class ProductSchema(ma.Schema):
  id = fields.Integer()
  name = fields.String()
  image = fields.String()
  price = fields.Float()
  tax = fields.Float()
  discount = fields.Float(dump_only = True)