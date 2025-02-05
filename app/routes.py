from controllers.order_controller import order_bp


def register_blueprints(app):
    app.register_blueprint(order_bp, url_prefix="/orders")