from app import db
import datetime

class Cargo(db.Model):
    __tablename__ = "cargo"
    id = db.Column(db.Integer, primary_key=True)
    nombre_cargo = db.Column(db.String(50), nullable=False, unique=True)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)
    usuarios = db.relationship('Usuario') 
    menus = db.relationship('Menu') 

    def __init__(self, form):
        self.nombre_cargo=form.get("nombre_cargo")

    def save_cargo(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_cargo(self, form):
        self.nombre_cargo=form.get("nombre_cargo")
        db.session.commit()
        return True

    def delete_cargo(self):
        db.session.delete(self)
        db.session.commit()
        return True


