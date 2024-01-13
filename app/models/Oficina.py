from app import db
import datetime

class Oficina(db.Model):
    __tablename__ = "oficina"
    id = db.Column(db.Integer, primary_key=True)
    nombre_oficina = db.Column(db.String(50), nullable=False,unique=True)
    direccion = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    guias = db.relationship('GuiaRemision') 

    def __init__(self, form):
        self.nombre_oficina=form.get("nombre")
        self.direccion=form.get("direccion")
        self.id_distrito=form.get("id_distrito")

    def to_json(self):
        dict={
            'id':self.id,
            'nombre':self.nombre_oficina,
            'direccion':self.direccion,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict

    def save_oficina(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_oficina(self, form):
        try:
            self.nombre_oficina=form.get("nombre")
            self.direccion=form.get("direccion")
            db.session.commit()
            return True
        except:
            return False

    def delete_oficina(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False





