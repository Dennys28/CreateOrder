from flask import Blueprint, request, jsonify

order_bp = Blueprint("order", __name__)


# Crear una orden
@order_bp.route("/", methods=["POST"])
def create_order():
    from app.models.order_model import Order  # Import local
    from app.views.order_view import order_response, success_response, error_response  # Import local
    try:
        data = request.get_json()
        new_order = Order(
            customer_id=data["customer_id"],
            restaurant_id=data["restaurant_id"],
            reservation_date=data["reservation_date"],
            reservation_time=data["reservation_time"],
            guests=data["guests"]
        )
        new_order.save()
        return jsonify(success_response("Orden creada exitosamente", order_response(new_order))), 201
    except Exception as e:
        return jsonify(error_response(str(e))), 400
