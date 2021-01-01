from app import db
import datetime

class Factura(db.Model):
    __tablename__ = "factura"
    id = db.Column(db.Integer, primary_key=True)
    numero_factura = db.Column(db.String(10), unique=True, nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    id_tipo_moneda = db.Column(db.Integer, db.ForeignKey("tipo_moneda.id"), nullable=False)
    fecha_emision = db.Column(db.DateTime, default=datetime.datetime.now)
    observacion = db.Column(db.Text(), nullable=False)
    estado = db.Column(db.String(1),default='A', nullable=False)
    total = db.Column(db.Float, nullable=False)
    
    guias = db.relationship('GuiaRemision')
    cliente = db.relationship('Cliente', backref='factura')
    tipo_moneda = db.relationship('TipoMoneda', backref='factura')

    def __init__(self, form):
        self.numero_factura=form.get("numero_factura")
        self.id_cliente=form.get("id_cliente")
        self.id_tipo_moneda=form.get("tipo_moneda")
        self.fecha_emision=form.get("fecha_emision")
        self.observacion=form.get("observacion")
        self.total=form.get("total")
    
    def to_json(self):
        dict={
            'id':self.id,
            'numero_factura':self.numero_factura,
            'id_cliente':self.id_cliente,
            'id_tipo_moneda':self.id_tipo_moneda,
            'observacion':self.observacion,
            'total':self.total,
            'fecha_emision':self.fecha_emision.strftime('%Y-%m-%d')
        }
        return dict

    def save_factura(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_factura(self, form):
        try:
            self.numero_factura=form.get("numero_factura")
            self.id_cliente=form.get("id_cliente")
            self.id_tipo_moneda=form.get("tipo_moneda")
            self.fecha_emision=form.get("fecha_emision")
            self.observacion=form.get("observacion")
            self.total=form.get("total")
            db.session.commit()
            return True
        except:
            return False

    def delete_factura(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False





