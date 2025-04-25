from app import db
import datetime


class Transportista(db.Model):
    __tablename__ = "transportista"
    id = db.Column(db.Integer, primary_key=True)
    ruc = db.Column(db.String(20), nullable=False)
    denominacion = db.Column(db.String(50), nullable=False)
    nombres = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    numero_licencia = db.Column(db.String(20),unique=True, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, form):
        self.ruc=form.get("ruc")
        self.denominacion=form.get("denominacion")
        self.nombres=form.get("nombres")
        self.apellidos=form.get("apellidos")
        self.numero_licencia=form.get("numero_licencia")

    def to_json(self):
        dict={
            'id':self.id,
            'ruc':self.ruc,
            'denominacion':self.denominacion,
            'nombres':self.nombres,
            'apellidos':self.apellidos,
            'numero_licencia':self.numero_licencia,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict

    def save_transportista(self):
        try:
            db.session.add(self)
            db.session.commit()
            print(f"Transportista guardado: {self.denominacion}")
            return True
        except Exception as e:
            print(e)
            return False

    def update_transportista(self, form):
        try:
            self.ruc=form.get("ruc")
            self.denominacion=form.get("denominacion")
            self.nombres=form.get("nombres")
            self.apellidos=form.get("apellidos")
            self.numero_licencia=form.get("numero_licencia")
            db.session.commit()
            print(f"Transportista actualizado: {self.denominacion}")
            return True
        except Exception as e:
            print(e)
            return False

    def delete_transportista(self):
        try:
            db.session.delete(self)
            db.session.commit()
            print(f"Transportista eliminado: {self.denominacion}")
            return True
        except Exception as e:
            print(e)
            return False







