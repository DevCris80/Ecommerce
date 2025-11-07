from app.db.models import Order

class OrderService:
    def __init__(self, db):
        self.db = db

    def list_orders(self):
        return self.db.query(Order)
    
    def get_order_by_id(self, order_id: int):
        return self.db.query(Order).filter(Order.id == order_id).first()
    
    def create_order(self, order_data):
        new_order = Order(**order_data.model_dump())
        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)
        return new_order