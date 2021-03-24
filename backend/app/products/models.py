from app.db import db, BaseModelMixin

class Product(db.Model, BaseModelMixin):
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
    return f'Product({self.name})'

  def __str__(self):
    return f'{self.name}'

class Order(db.Model, BaseModelMixin):
  id = db.Column(db.Integer, primary_key=True)
  productName = db.Column(db.String)
  totalProduct = db.Column(db.Float)
  totalCompra = db.Column(db.Float)
  productId = db.Column(db.Integer, db.ForeignKey('product.id'), nullable = False)

  def __init__(self, productName, totalProduct, totalCompra):
    self.productName = productName
    self.totalProduct = totalProduct
    self.totalCompra = totalCompra

  def __repr__(self):
    return f'Order({self.id})'

  def __str__(self):
    return f'{self.id}: {self.productName}'
