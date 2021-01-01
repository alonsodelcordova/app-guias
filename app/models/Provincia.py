from app import db
import datetime

class Provincia(db.Model):
    __tablename__ = "provincia"
    id = db.Column(db.Integer, primary_key=True)
    id_departamento=db.Column(db.Integer, db.ForeignKey("departamento.id"), nullable=False)
    nombre_provincia = db.Column(db.String(50),unique=True, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    distritos = db.relationship('Distrito')
    departamento = db.relationship('Departamento', backref='provincia')

    def __init__(self, form):
        self.nombre_provincia=form.get("nombre")

    def to_json(self):
        dict={
            'id':self.id,
            'id_departamento':self.id_departamento,
            'nombre':self.nombre_provincia,
            'fecha':self.fecha.strftime('%Y-%m-%d'),
            #'distritos':[(row.to_json()) for row in self.distritos]
        }
        return dict

    def save_provincia(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_provincia(self, form):
        try:
            self.nombre_provincia=form.get("nombre")
            db.session.commit()
            return True
        except:
            return False

    def delete_provincia(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False



