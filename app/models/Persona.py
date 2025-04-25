from app import db
import datetime

class Persona(db.Model):
    __tablename__ = "persona"
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(8), nullable=False)
    nombres = db.Column(db.String(50), nullable=False)
    primer_apellido = db.Column(db.String(50), nullable=False)
    segundo_apellido = db.Column(db.String(50), nullable=False)
    estado_civil = db.Column(db.String(1),default='N', nullable=False)
    sexo = db.Column(db.String(1),default='N', nullable=False)
    numero_celular = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)


    def __init__(self, form):
        self.nombres=form.get("nombres")
        self.dni=form.get("dni")
        self.primer_apellido=form.get("primer_apellido")
        self.segundo_apellido=form.get("segundo_apellido")
        self.estado_civil=form.get("estado_civil")
        self.sexo=form.get("sexo")
        self.numero_celular=form.get("numero_celular")
        self.email=form.get("email")
        self.direccion=form.get("direccion")
    
    def to_json(self):
        dict={
            'id':self.id,
            'nombres':self.nombres,
            'dni':self.dni,
            'primer_apellido':self.primer_apellido,
            'segundo_apellido':self.segundo_apellido,
            'estado_civil':self.estado_civil,
            'sexo':self.sexo,
            'numero_celular':self.numero_celular,
            'direccion':self.direccion,
            'email':self.email,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict

    def save_persona(self):
        try:
            db.session.add(self)
            db.session.commit()
            print(f"Persona guardada: {self.nombres}")
            return True
        except Exception as e:
            print(e)
            return False

    def update_persona(self, form):
        try:
            self.dni=form.get("dni")
            self.nombres=form.get("nombres")
            self.primer_apellido=form.get("primer_apellido")
            self.segundo_apellido=form.get("segundo_apellido")
            self.estado_civil=form.get("estado_civil")
            self.sexo=form.get("sexo")
            self.numero_celular=form.get("numero_celular")
            self.email=form.get("email")
            self.direccion=form.get("direccion")
            db.session.commit()
            print(f"Persona actualizada: {self.nombres}")
            return True
        except Exception as e:
            print(e)
            return False

    def delete_persona(self):
        try:
            db.session.delete(self)
            db.session.commit()
            print(f"Persona eliminada: {self.nombres}")
            return True
        except Exception as e:
            print(e)
            return False






    
