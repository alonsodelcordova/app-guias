from app import db
import datetime

class Menu(db.Model):
    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key=True)
    id_cargo = db.Column(db.Integer, db.ForeignKey("cargo.id"), nullable=False)
    nombre_menu = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)
    estado = db.Column(db.String(1),default='A', nullable=False)
    links = db.relationship('Link',cascade="all, delete") 
    cargo = db.relationship('Cargo', backref='menu')

    def __init__(self, form):
        self.nombre_menu=form.get("nombre_menu")
        self.id_cargo=form.get("id_cargo")
    
    def to_json(self):
        dict={
            'id':self.id,
            'nombre':self.nombre_menu,
            'id_cargo':self.id_cargo,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict

    def save_menu(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_menu(self, form):
        try:
            self.nombre_menu=form.get("nombre_menu")
            self.id_cargo=form.get("id_cargo")
            db.session.commit()
            return True
        except:
            return False

    def delete_menu(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False



