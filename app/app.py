from flask import Flask
from config.database import init_db
from controllers.order_controller import order_bp

app = Flask(__name__)

# Configurar base de datos
init_db(app)

# Registrar Blueprint (rutas)
app.register_blueprint(order_bp, url_prefix="/orders")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
