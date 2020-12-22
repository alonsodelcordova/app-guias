from app import db
import datetime

class DescripcionGuia(db.Model):
    __tablename__ = "descripcion_guia"
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    unidad_medida = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    id_guia_remision = db.Column(db.Integer, db.ForeignKey("guia_remision.id"), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    guia_remision = db.relationship('GuiaRemision', backref='descripcion_guia')

    def __init__(self, form):
        self.descripcion=form.get("descripcion")
        self.cantidad=form.get("cantidad")
        self.unidad_medida=form.get("unidad_medida")
        self.id_guia_remision=form.get("id_guia_remision")
        self.peso= float(form.get("cantidad")) * float(form.get("unidad_medida"))

    def save_descripcion(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_descripcion(self, form):
        self.descripcion=form.get("descripcion")
        self.cantidad=form.get("cantidad")
        self.unidad_medida=form.get("unidad_medida")
        self.id_guia_remision=form.get("id_guia_remision")
        self.peso=self.cantidad * self.unidad_medida
        db.session.commit()
        return True

    def delete_descripcion(self):
        db.session.delete(self)
        db.session.commit()
        return True