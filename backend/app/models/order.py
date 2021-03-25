from app.ext import db
from .baseModel import BaseModel

class Order(db.Model, BaseModel):
  id = db.Column(db.Integer, primary_key=True)
  productName = db.Column(db.String)
  totalProduct = db.Column(db.Float)
  totalCompra = db.Column(db.Float)
  productId = db.Column(db.Integer, db.ForeignKey('product.id'))
  product = db.relationship('Product')

  def __init__(self, productName, totalProduct, totalCompra, product):
    self.productName = productName
    self.totalProduct = totalProduct
    self.totalCompra = totalCompra
    self.product = product

  def __repr__(self):
    return f'Order({self.id})'

  def __str__(self):
    return f'{self.id}: {self.productName}'
