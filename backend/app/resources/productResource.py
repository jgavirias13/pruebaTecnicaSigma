from flask_restful import Resource
from app.schema.productSchema import ProductSchema
from app.models.product import Product
from app.models.productResponse import ProductResponse
from app.common.util import calculateDiscount, calculateTax
import requests

productSchema = ProductSchema()

def validateProductEquals(product1, product2):
  if(product1.name == product2.name and product1.image == product2.image
    and product1.price == product2.price and product1.tax == product2.tax):
    return True
  return False

class ProductResource(Resource):
  def get(self):
    apiResponse = requests.get('http://sigmatest.sigmastorage.online/')
    productDic = productSchema.load(apiResponse.json())
    inquiredProduct = Product(productDic['id'], productDic['name'],
      productDic['image'], productDic['price'], productDic['tax'])
    oldProduct = Product.get_by_id(inquiredProduct.id)
    if(oldProduct):
      if(not validateProductEquals(inquiredProduct, oldProduct)):
        oldProduct.name = inquiredProduct.name
        oldProduct.image = inquiredProduct.image
        oldProduct.price = inquiredProduct.price
        oldProduct.tax = inquiredProduct.tax
        oldProduct.update()
    else:
      inquiredProduct.save()
    
    productResponse = ProductResponse(inquiredProduct.id, inquiredProduct.name,
      inquiredProduct.image, inquiredProduct.price, inquiredProduct.tax)
    productResponse.tax = calculateTax(inquiredProduct)
    productResponse.discount = calculateDiscount(inquiredProduct)
    return productSchema.dump(productResponse)
