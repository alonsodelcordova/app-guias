from app import db
import datetime

class Oficina(db.Model):
    __tablename__ = "oficina"
    id = db.Column(db.Integer, primary_key=True)
    id_distrito = db.Column(db.Integer, db.ForeignKey("distrito.id"), nullable=False)
    nombre_oficina = db.Column(db.String(50), nullable=False,unique=True)
    direccion = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    guias = db.relationship('GuiaRemision') 
    distrito = db.relationship('Distrito', backref='oficina')

    def __init__(self, form):
        self.nombre_oficina=form.get("nombre")
        self.direccion=form.get("direccion")
        self.id_distrito=form.get("id_distrito")

    def save_oficina(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_oficina(self, form):
        self.nombre_oficina=form.get("nombre")
        self.direccion=form.get("direccion")
        self.id_distrito=form.get("id_distrito")
        db.session.commit()
        return True

    def delete_oficina(self):
        db.session.delete(self)
        db.session.commit()
        return True





