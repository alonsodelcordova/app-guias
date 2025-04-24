from app import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    id_cargo = db.Column(db.Integer, db.ForeignKey("cargo.id"), nullable=False)
    id_oficina = db.Column(db.Integer, db.ForeignKey("oficina.id"), nullable=False)
    id_persona = db.Column(db.Integer, db.ForeignKey("persona.id"), nullable=False)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)
    estado = db.Column(db.String(1),default='A', nullable=False)

    cargo = db.relationship('Cargo', backref = 'usuarios', foreign_keys=[id_cargo])
    oficina = db.relationship('Oficina', backref = 'usuarios', foreign_keys=[id_oficina])
    persona = db.relationship('Persona', backref = 'usuarios', foreign_keys=[id_persona])


    def __init__(self, form):
        self.usuario = form.get("usuario")
        self.id_cargo = form.get("id_cargo")
        self.id_oficina = form.get("id_oficina")
        self.password = self.__create_password(form.get("password"))

    def to_json(self):
        dict={
            'id':self.id,
            'id_cargo':self.id_cargo,
            'id_oficina':self.id_oficina,
            'id_persona':self.id_persona,
            'usuario':self.usuario,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict

    def __create_password(self, clave):
        return generate_password_hash(clave)

    def verify_password(self, password):
        #return self.password == password
        return check_password_hash(self.password, password)

    def save_usuario(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def change_usuario(self, form):
        self.usuario = form.get("usuario")
        self.id_cargo = form.get("id_cargo")
        self.id_oficina = form.get("id_oficina")
        return self.update_usuario()
        
    def update_usuario(self):
        try:
            db.session.commit()
            return True
        except:
            return False

    def update_password(self,password):
        self.password=self.__create_password(password)
    
    def delete_usuario(self):
        db.session.delete(self)
        db.session.commit()
        return True