from app import db
import datetime

class DescripcionGuia(db.Model):
    __tablename__ = "descripcion_guia"
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(300), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    unidad_medida = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    id_guia_remision = db.Column(db.Integer, db.ForeignKey("guia_remision.id"), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    guia_remision = db.relationship('GuiaRemision', backref = 'descripcion_guias', foreign_keys=[id_guia_remision])

    def __init__(self, form):
        self.descripcion=form.get("descripcion")
        self.cantidad=form.get("cantidad")
        self.unidad_medida=form.get("unidad_medida")
        self.peso= float(form.get("cantidad")) * float(form.get("unidad_medida"))
    
    def to_json(self):
        dict={
            'id':self.id,
            'descripcion':self.descripcion,
            'cantidad':self.cantidad,
            'unidad_medida':self.unidad_medida,
            'id_guia_remision':self.id_guia_remision,
            'peso':self.peso,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict

    def save_descripcion(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_descripcion(self, form):
        try:
            self.descripcion=form.get("descripcion")
            self.cantidad=form.get("cantidad")
            self.unidad_medida=form.get("unidad_medida")
            self.peso= float(form.get("cantidad")) * float(form.get("unidad_medida"))
            db.session.commit()
            return True
        except:
            return False

    def delete_descripcion(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False