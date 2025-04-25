from app import db
import datetime

class MotivoTraslado(db.Model):
    __tablename__ = "motivo_traslado"
    id = db.Column(db.Integer, primary_key=True)
    nombre_motivo = db.Column(db.String(50), nullable=False,unique=True)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, form):
        self.nombre_motivo=form.get("nombre")
        
    def to_json(self):
        dict={
            'id':self.id,
            'nombre':self.nombre_motivo,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict

    def save_motivo(self):
        try:
            db.session.add(self)
            db.session.commit()
            print(f"Motivo guardado: {self.nombre_motivo}")
            return True
        except Exception as e:
            print(e)
            return False

    def update_motivo(self, form):
        try:
            self.nombre_motivo=form.get("nombre")
            db.session.commit()
            print(f"Motivo actualizado: {self.nombre_motivo}")
            return True
        except Exception as e:
            print(e)
            return False

    def delete_motivo(self):
        try:
            db.session.delete(self)
            db.session.commit()
            print(f"Motivo eliminado: {self.nombre_motivo}")
            return True
        except Exception as e:
            print(e)
            return False



