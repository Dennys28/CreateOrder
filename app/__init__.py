from flask import Flask
from app.config.database import db
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()  # Cargar variables de entorno
    app = Flask(__name__)

    # Configurar la base de datos
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Registrar blueprints (controladores)
    from app.controllers.order_controller import order_bp
    app.register_blueprint(order_bp, url_prefix="/orders")

    return app
