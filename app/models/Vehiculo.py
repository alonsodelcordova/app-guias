from app import db
import datetime

class Vehiculo(db.Model):
    __tablename__ = "vehiculo"
    id = db.Column(db.Integer, primary_key=True)
    marca_vehiculo = db.Column(db.String(30), nullable=False)
    modelo_vehiculo = db.Column(db.String(15), nullable=False)
    placa_vehiculo = db.Column(db.String(15), nullable=False, unique=True)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, form):
        self.marca_vehiculo=form.get("marca_vehiculo")
        self.modelo_vehiculo=form.get("modelo_vehiculo")
        self.placa_vehiculo=form.get("placa_vehiculo")

    def to_json(self):
        dict={
            'id':self.id,
            'marca_vehiculo':self.marca_vehiculo,
            'modelo_vehiculo':self.modelo_vehiculo,
            'placa_vehiculo':self.placa_vehiculo,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict

    def save_vehiculo(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_vehiculo(self, form):
        try:
            self.marca_vehiculo=form.get("marca_vehiculo")
            self.modelo_vehiculo=form.get("modelo_vehiculo")
            self.placa_vehiculo=form.get("placa_vehiculo")
            db.session.commit()
            return True
        except:
            return False

    def delete_vehiculo(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False




