
from app import db
import datetime

class GuiaRemision(db.Model):
    __tablename__ = "guia_remision"
    id = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.DateTime, default=datetime.datetime.now)
    id_oficina = db.Column(db.Integer, db.ForeignKey("oficina.id"), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    id_factura = db.Column(db.Integer, db.ForeignKey("factura.id"), nullable=False)
    id_transportista = db.Column(db.Integer, db.ForeignKey("transportista.id"), nullable=False)
    id_vehiculo = db.Column(db.Integer, db.ForeignKey("vehiculo.id"), nullable=False)
    id_motivo_traslado = db.Column(db.Integer, db.ForeignKey("motivo_traslado.id"), nullable=False)
    punto_destino = db.Column(db.String(50), nullable=False)

    descripcion_guias = db.relationship('DescripcionGuia') 
    oficina = db.relationship('Oficina', backref='guia_remision')
    usuario = db.relationship('Usuario', backref='guia_remision')
    factura = db.relationship('Factura', backref='guia_remision')
    transportista = db.relationship('Transportista', backref='guia_remision')
    vehiculo = db.relationship('Vehiculo', backref='guia_remision')
    motivo_traslado = db.relationship('MotivoTraslado', backref='guia_remision')


    def __init__(self, form):
        self.fecha_inicio=form.get("fecha_inicio")
        self.id_oficina=form.get("id_oficina")
        self.id_factura=form.get("id_factura")
        self.id_transportista=form.get("id_transportista")
        self.id_vehiculo=form.get("id_vehiculo")
        self.id_motivo_traslado=form.get("id_motivo_traslado")
        self.direccion=form.get("direccion")
        self.punto_destino=form.get("punto_destino") 

    def to_json(self):
        dict={
            'id':self.id,
            'id_oficina':self.id_oficina,
            'id_usuario':self.id_usuario,
            'id_factura':self.id_factura,
            'id_transportista':self.id_transportista,
            'id_vehiculo':self.id_vehiculo,
            'id_motivo_traslado':self.id_motivo_traslado,
            'direccion':self.direccion,
            'punto_destino':self.punto_destino,
            'fecha_inicio':self.fecha_inicio.strftime('%Y-%m-%d')
        }
        return dict

    def save_guia(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_guia(self, form):
        try:
            self.fecha_inicio=form.get("fecha_inicio")
            self.id_oficina=form.get("id_oficina")
            self.id_factura=form.get("id_factura")
            self.id_transportista=form.get("id_transportista")
            self.id_vehiculo=form.get("id_vehiculo")
            self.id_motivo_traslado=form.get("id_motivo_traslado")
            self.direccion=form.get("direccion")
            self.punto_destino=form.get("punto_destino")
            db.session.commit()
            return True
        except:
            return False

    def delete_guia(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False




