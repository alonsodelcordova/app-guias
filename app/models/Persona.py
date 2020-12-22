from app import db
import datetime

class Persona(db.Model):
    __tablename__ = "persona"
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(8), nullable=False)
    id_distrito = db.Column(db.Integer, db.ForeignKey("distrito.id"), nullable=False)
    nombres = db.Column(db.String(50), nullable=False)
    primer_apellido = db.Column(db.String(50), nullable=False)
    segundo_apellido = db.Column(db.String(50), nullable=False)
    estado_civil = db.Column(db.String(1),default='N', nullable=False)
    sexo = db.Column(db.String(1),default='N', nullable=False)
    numero_celular = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    usuarios = db.relationship('Usuario') 
    distrito = db.relationship('Distrito', backref='persona')

    def __init__(self, form):
        self.nombres=form.get("nombres")
        self.dni=form.get("dni")
        self.id_distrito=form.get("id_distrito")
        self.primer_apellido=form.get("primer_apellido")
        self.segundo_apellido=form.get("segundo_apellido")
        self.estado_civil=form.get("estado_civil")
        self.sexo=form.get("sexo")
        self.numero_celular=form.get("numero_celular")
        self.email=form.get("email")
        self.direccion=form.get("direccion")

    def save_persona(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_persona(self, form):
        self.dni=form.get("dni")
        self.nombres=form.get("nombres")
        self.id_distrito=form.get("id_distrito")
        self.primer_apellido=form.get("primer_apellido")
        self.segundo_apellido=form.get("segundo_apellido")
        self.estado_civil=form.get("estado_civil")
        self.sexo=form.get("sexo")
        self.numero_celular=form.get("numero_celular")
        self.email=form.get("email")
        self.direccion=form.get("direccion")
        db.session.commit()
        return True

    def delete_persona(self):
        db.session.delete(self)
        db.session.commit()
        return True






    
