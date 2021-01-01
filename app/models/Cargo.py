from app import db
import datetime

class Cargo(db.Model):
    __tablename__ = "cargo"
    id = db.Column(db.Integer, primary_key=True)
    nombre_cargo = db.Column(db.String(50), nullable=False, unique=True)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)
    usuarios = db.relationship('Usuario',cascade="all, delete") 
    menus = db.relationship('Menu',cascade="all, delete") 

    def __init__(self, form):
        self.nombre_cargo=form.get("nombre_cargo")
    
    def to_json(self):
        dict={
            'id':self.id,
            'nombre':self.nombre_cargo,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict

    def save_cargo(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_cargo(self, form):
        try:
            self.nombre_cargo=form.get("nombre_cargo")
            db.session.commit()
            return True
        except:
            return False

    def delete_cargo(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False
        


