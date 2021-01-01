from app import db
import datetime

class Departamento(db.Model):
    __tablename__ = "departamento"
    id = db.Column(db.Integer, primary_key=True)
    nombre_departamento = db.Column(db.String(50), nullable=False, unique=True)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)
    
    provincias = db.relationship('Provincia')
    
    def __init__(self, form):
        self.nombre_departamento=form.get("nombre")

    def to_json(self):
        dict={
            'id': self.id,
            'nombre': self.nombre_departamento,
            'fecha':self.fecha.strftime('%Y-%m-%d'),
            #'provincias': [(row.to_json()) for row in self.provincias]
        }
        return dict

    def save_departamento(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_departamento(self, form):
        self.nombre_departamento=form.get("nombre")
        db.session.commit()
        return True

    def delete_departamento(self):
        db.session.delete(self)
        db.session.commit()
        return True