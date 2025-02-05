from flask import Blueprint, request, jsonify

# Blueprint para las rutas de órdenes
order_bp = Blueprint("order", __name__)


# Crear una orden
@order_bp.route("/", methods=["POST"])
def create_order():
    # Usamos importaciones relativas para evitar problemas con el sistema de paquetes
    from ..models.order_model import Order
    from ..views.order_view import order_response, success_response, error_response

    try:
        # Obtener datos del JSON enviado en la solicitud
        data = request.get_json()

        # Crear una nueva orden
        new_order = Order(
            customer_id=data["customer_id"],
            restaurant_id=data["restaurant_id"],
            reservation_date=data["reservation_date"],
            reservation_time=data["reservation_time"],
            guests=data["guests"]
        )
        new_order.save()

        # Respuesta de éxito
        return jsonify(success_response("Orden creada exitosamente", order_response(new_order))), 201

    except Exception as e:
        # Respuesta de error
        return jsonify(error_response(str(e))), 400
