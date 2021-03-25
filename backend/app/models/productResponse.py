class ProductResponse():

  def __init__(self, id, name, image, price, tax, discount=0):
    self.id = id
    self.name = name
    self.image = image
    self.price = price
    self.tax = tax
    self.discount = discount