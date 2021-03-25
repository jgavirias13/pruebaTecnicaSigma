from marshmallow import fields
from app.ext import ma

class OrderSchema(ma.Schema):
  id = fields.Integer(dump_only=True)
  productName = fields.String()
  totalProduct = fields.Float()
  totalCompra = fields.Float()
  product = fields.Nested('ProductSchema')