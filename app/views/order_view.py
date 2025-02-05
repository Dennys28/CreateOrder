def order_response(order):
    """
    Convierte un objeto Order en un diccionario para la respuesta JSON.
    """
    return {
        "id": order.id,
        "customer_id": order.customer_id,
        "restaurant_id": order.restaurant_id,
        "reservation_date": order.reservation_date.strftime("%Y-%m-%d"),
        "reservation_time": order.reservation_time.strftime("%H:%M:%S"),
        "guests": order.guests
    }


def success_response(message, data=None):
    """
    Retorna una respuesta de éxito con un mensaje y opcionalmente datos.
    """
    response = {"message": message}
    if data:
        response["data"] = data
    return response


def error_response(error_message):
    """
    Retorna una respuesta de error.
    """
    return {"error": error_message}
