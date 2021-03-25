from flask_restful import Resource
from flask import request
from app.schema.orderSchema import OrderSchema
from app.models.order import Order
from app.models.product import Product
from app.common.util import calculateTotalCompra

orderSchema = OrderSchema()

class OrderResource(Resource):
  def post(self):
    data = request.get_json()
    orderDict = orderSchema.load(data)
    product = Product.get_by_id((orderDict['product']['id']))
    order = Order(orderDict['productName'], orderDict['totalProduct'],
      orderDict['totalCompra'], product)
    totalCalculado = calculateTotalCompra(product)

    if(totalCalculado != order.totalCompra):
      print(totalCalculado)
      print('error son diferentes')
    else:
      order.save()
    resp = orderSchema.dump(order)
    return resp, 201