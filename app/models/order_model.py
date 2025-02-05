from app.config.database import db

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, nullable=False)
    reservation_date = db.Column(db.Date, nullable=False)
    reservation_time = db.Column(db.Time, nullable=False)
    guests = db.Column(db.Integer, nullable=False)

    def __init__(self, customer_id, restaurant_id, reservation_date, reservation_time, guests):
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.reservation_date = reservation_date
        self.reservation_time = reservation_time
        self.guests = guests

    def save(self):
        db.session.add(self)
        db.session.commit()
