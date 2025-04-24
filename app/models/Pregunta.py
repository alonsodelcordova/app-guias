from app import db
import datetime

class Pregunta(db.Model):
    __tablename__ = "pregunta"
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    pregunta = db.Column(db.String(100), nullable=False)
    respuesta = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    usuario = db.relationship('Usuario', backref = 'preguntas', foreign_keys=[id_usuario])

    def __init__(self, form):
        self.id_usuario=form.get("id_usuario")
        self.pregunta=form.get("pregunta")
        self.respuesta=form.get("respuesta")
    
    def to_json(self):
        dict={
            'id':self.id,
            'id_usuario':self.id_usuario,
            'pregunta':self.pregunta,
            'respuesta':self.respuesta,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict


    def save_pregunta(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_pregunta(self, form):
        try:
            self.id_usuario=form.get("id_usuario")
            self.pregunta=form.get("pregunta")
            self.respuesta=form.get("respuesta")
            db.session.commit()
            return True
        except:
            return False

    def delete_pregunta(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False



