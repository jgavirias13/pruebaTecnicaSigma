from flask_restful import Resource
from app.schema.productSchema import ProductSchema
from app.models.product import Product

productSchema = ProductSchema()

class ProductResource(Resource):
  def get(self):
    product = Product(1, 'Libros', 'https://images-na.ssl-images-amazon.com/images/I/61Uxg-SWExL._SL1500_.jpg', 10, 1)
    response = productSchema.dump(product)
    return response