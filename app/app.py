from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuración de la base de datos con valores por defecto
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '3306')  # Puerto por defecto de MySQL
DB_NAME = os.getenv('DB_NAME', 'testdb')

# Verificar si el puerto es un entero válido
try:
    DB_PORT = int(DB_PORT)
except ValueError:
    raise ValueError("La variable DB_PORT debe ser un número entero válido.")

# Construir la URI de conexión
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Modelo de la orden
class Orden(db.Model):
    __tablename__ = "Ordenes"

    ID_Orden = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ID_Cliente = db.Column(db.Integer, nullable=False)
    ID_Restaurante = db.Column(db.Integer, nullable=False)
    Fecha = db.Column(db.Date, nullable=False)
    Hora = db.Column(db.Time, nullable=False)
    Numero_Personas = db.Column(db.Integer, nullable=False)
    Estado = db.Column(db.Enum("Pendiente", "Confirmada", "Cancelada"), default="Pendiente")


@app.route("/orders", methods=["POST"])
def create_order():
    try:
        data = request.get_json()

        # Validar que todos los campos obligatorios estén presentes
        required_fields = ["ID_Cliente", "ID_Restaurante", "Fecha", "Hora", "Numero_Personas"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"El campo '{field}' es obligatorio"}), 400

        # Crear nueva orden
        new_order = Orden(
            ID_Cliente=data["ID_Cliente"],
            ID_Restaurante=data["ID_Restaurante"],
            Fecha=data["Fecha"],
            Hora=data["Hora"],
            Numero_Personas=data["Numero_Personas"],
            Estado=data.get("Estado", "Pendiente")  # Si no envían Estado, se pone 'Pendiente'
        )

        db.session.add(new_order)
        db.session.commit()

        return jsonify({"message": "Orden creada exitosamente", "order_id": new_order.ID_Orden}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
