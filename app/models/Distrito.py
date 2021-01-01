from app import db
import datetime

class Distrito(db.Model):
    __tablename__ = "distrito"
    id = db.Column(db.Integer, primary_key=True)
    id_provincia = db.Column(db.Integer, db.ForeignKey("provincia.id"), nullable=False)
    nombre_distrito = db.Column(db.String(50), nullable=False, unique=True)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)
    
    oficinas = db.relationship('Oficina')
    provincia = db.relationship('Provincia', backref='distrito')

    def __init__(self, form):
        self.nombre_distrito=form.get("nombre")

    def to_json(self):
        dict={
            'id':self.id,
            'id_provincia':self.id_provincia,
            'nombre':self.nombre_distrito,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict

    def save_distrito(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_distrito(self, form):
        try:
            self.nombre_distrito=form.get("nombre")
            db.session.commit()
            return True
        except:
            return False

    def delete_distrito(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False



