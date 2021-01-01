from app import db
import datetime

class TipoMoneda(db.Model):
    __tablename__ = "tipo_moneda"
    id = db.Column(db.Integer, primary_key=True)
    nombre_moneda = db.Column(db.String(20),unique=True, nullable=False)
    prefijo = db.Column(db.String(3),unique=True, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)
    facturas = db.relationship('Factura')

    def __init__(self, form):
        self.nombre_moneda=form.get("nombre")
        self.prefijo=form.get("prefijo")
    
    def to_json(self):
        dict={
            'id':self.id,
            'nombre':self.nombre_moneda,
            'prefijo':self.prefijo,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict

    def save_moneda(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_moneda(self, form):
        try:
            self.nombre_moneda=form.get("nombre")
            self.prefijo=form.get("prefijo")
            db.session.commit()
            return True
        except:
            return False

    def delete_moneda(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False



