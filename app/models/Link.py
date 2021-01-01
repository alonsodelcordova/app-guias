from app import db
import datetime

class Link(db.Model):
    __tablename__ = "link"
    id = db.Column(db.Integer, primary_key=True)
    id_menu = db.Column(db.Integer, db.ForeignKey("menu.id"), nullable=False)
    nombre_link = db.Column(db.String(50), nullable=False)
    link = db.Column(db.String(50), nullable=False, unique=True)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    menu = db.relationship('Menu', backref='link')

    def __init__(self, form):
        self.nombre_link=form.get("nombre")
        self.link=form.get("link")
        self.id_menu=form.get("id_menu")
    
    def to_json(self):
        dict={
            'id':self.id,
            'nombre':self.nombre_link,
            'link':self.link,
            'id_menu':self.id_menu,
            'fecha':self.fecha.strftime('%Y-%m-%d')
        }
        return dict

    def save_link(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def update_link(self, form):
        try:
            self.nombre_link=form.get("nombre")
            self.link=form.get("link")
            self.id_menu=form.get("id_menu")
            db.session.commit()
            return True
        except:
            return False

    def delete_link(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False



