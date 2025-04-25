from app import db
import datetime

class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True)
    razon_social = db.Column(db.String(50), nullable=False)
    tipo_documento = db.Column(db.String(3), nullable=False)
    numero_documento = db.Column(db.String(20), nullable=False,unique=True)
    direccion = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, form):
        self.razon_social=form.get("razon_social")
        self.tipo_documento=form.get("tipo_documento")
        self.numero_documento=form.get("numero_documento")
        self.direccion=form.get("direccion")
    
    def to_json(self):
        dict={
            'id':self.id,
            'razon_social':self.razon_social,
            'tipo_documento':self.tipo_documento,
            'numero_documento':self.numero_documento,
            'direccion':self.direccion,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict


    def save_cliente(self):
        try:
            db.session.add(self)
            db.session.commit()
            print(f"Cliente guardado: {self.razon_social}")
            return True
        except Exception as e:
            print(e)
            return False

    def change_cliente(self, form):
        self.razon_social=form.get("razon_social")
        self.tipo_documento=form.get("tipo_documento")
        self.numero_documento=form.get("numero_documento")
        self.direccion=form.get("direccion")
        return self.update_cliente()
        
    def update_cliente(self):
        try:
            db.session.commit()
            print(f"Cliente actualizado: {self.razon_social}")
            return True
        except Exception as e:
            print(e)
            return False

    def delete_cliente(self):
        try:
            db.session.delete(self)
            db.session.commit()
            print(f"Cliente eliminado: {self.razon_social}")
            return True
        except Exception as e:
            print(e)
            return False


