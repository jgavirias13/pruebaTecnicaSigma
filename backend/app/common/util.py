from app.models.product import Product
from datetime import datetime

def calculateTotalCompra(product: Product):
  totalCompra = product.price
  totalCompra += calculateTax(product)
  totalCompra *= (1 - calculateDiscount(product))
  return totalCompra

def calculateDiscount(product: Product):
  horaActual = datetime.now().hour
  if(product.id == 1 and horaActual % 2 == 0):
    return 0.2
  return 0

def calculateTax(product: Product):
  if(product.id == 1):
    return product.tax
  return 0