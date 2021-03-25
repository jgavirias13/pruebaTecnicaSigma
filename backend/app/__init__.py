from flask import Flask, jsonify
from flask_restful import Api
from app.resources.orderResource import OrderResource
from app.resources.productResource import ProductResource
from .ext import ma, migrate, db

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    api = Api(app, catch_all_404s=True)

    app.url_map.strict_slashes = False
    
    api.add_resource(OrderResource, '/orders')
    api.add_resource(ProductResource, '/products')
    
    return app