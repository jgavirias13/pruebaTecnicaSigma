from app.ext import db
from .baseModel import BaseModel

class Product(db.Model, BaseModel):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  image = db.Column(db.String)
  price = db.Column(db.Float)
  tax = db.Column(db.Float)

  def __init__(self, id, name, image, price, tax):
    self.id = id
    self.name = name
    self.image = image
    self.price = price
    self.tax = tax

  def __repr__(self):
    return f'Product({self.id})'

  def __str__(self):
    return f'{self.name}'