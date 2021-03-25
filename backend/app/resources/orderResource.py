from flask_restful import Resource
from app.schema.orderSchema import OrderSchema
from app.models.order import Order

orderSchema = OrderSchema()

class OrderResource(Resource):
  def post(self):
    data = request.get_json()
    orderDict = orderSchema.load(data)
    order = Order(orderDict['productName'], orderDict['totalProduct'],
      orderDict['totalCompra'], None)
    order.save()
    resp = orderSchema.dump(order)
    return resp, 201