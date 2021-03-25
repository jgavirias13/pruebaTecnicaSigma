from marshmallow import fields
from app.ext import ma

class ProductSchema(ma.Schema):
  id = fields.Integer(dump_only=True)
  name = fields.String()
  image = fields.String()
  price = fields.Float()
  tax = fields.Float()