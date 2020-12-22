from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

# para el token
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

db = SQLAlchemy()

def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
    db.init_app(app)
    csrf.init_app(app)
    
    #modelos
    from app.models.Cargo import Cargo
    from app.models.Menu import Menu
    from app.models.Link import Link
    from app.models.Departamento import Departamento
    from app.models.Provincia import Provincia
    from app.models.Distrito import Distrito
    from app.models.Persona import Persona
    from app.models.Oficina import Oficina
    from app.models.Usuario import Usuario
    from app.models.Cliente import Cliente
    from app.models.TipoMoneda import TipoMoneda
    from app.models.Factura import Factura
    from app.models.MotivoTraslado import MotivoTraslado
    from app.models.Vehiculo import Vehiculo
    from app.models.Transportista import Transportista
    from app.models.GuiaRemision import GuiaRemision
    from app.models.DescripcionGuia import DescripcionGuia

    #views
    from app.login import login as viewlogin
    app.register_blueprint(viewlogin)
    
    from app.gerente import gerente as viewGerente
    app.register_blueprint(viewGerente)

    from app.secretaria import secretaria as viewsecretaria
    app.register_blueprint(viewsecretaria)

    

    from app.admin import admin as viewadmin
    app.register_blueprint(viewadmin)
    
    #apis
    from app.gerente import api_gerente 
    app.register_blueprint(api_gerente)

    from app.admin import api_admin 
    app.register_blueprint(api_admin)

    with app.app_context():
        db.create_all()
    return app
    
