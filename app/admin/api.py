from . import api_admin as api
from app.models.Departamento import Departamento
from app.models.Provincia import Provincia
from app.models.Distrito import Distrito

from app.models.Cargo import Cargo
from app.models.Menu import Menu
from app.models.Link import Link
from app.models.TipoMoneda import TipoMoneda
from app.models.Oficina import Oficina

from app.models.Usuario import Usuario
from app.models.Persona import Persona

from flask import jsonify

#********************* direccion
@api.route("/provincias/<int:id>", methods=["GET"])#id departamento
def provincias(id):
    provincias=Provincia.query.filter_by(id_departamento=id)
    return jsonify([(provincia.to_json()) for provincia in provincias])

@api.route("/distritos/<int:id>", methods=["GET"])# id provincias
def distritos(id=0):
    distritos=Distrito.query.filter_by(id_provincia=id)
    return jsonify([(distrito.to_json()) for distrito in distritos])

#--------   api para los get y delete de las vistas ---------#
#cargos 
@api.route("/cargo/<int:id>", methods=["GET"])#id cargo
def cargo(id):
    cargo=Cargo.query.filter_by(id=id).first()
    if cargo is not None:
        return jsonify(cargo.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar cargo
@api.route("/cargo/<int:id>", methods=["DELETE"])
def cargo_delete(id):
    cargo = Cargo.query.filter_by(id=id).first() 
    if cargo.delete_cargo():
        return jsonify(dict(mesage='Cargo eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#menus
@api.route("/menu/<int:id>", methods=["GET"])#id menu
def menu(id):
    menu=Menu.query.filter_by(id=id).first()
    if menu is not None:
        return jsonify(menu.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar menu
@api.route("/menu/<int:id>", methods=["DELETE"])
def menu_delete(id):
    menu = Menu.query.filter_by(id=id).first() 
    if menu.delete_menu():
        return jsonify(dict(mesage='Menu eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#link
@api.route("/link/<int:id>", methods=["GET"])#id menu
def link(id):
    link=Link.query.filter_by(id=id).first()
    if link is not None:
        return jsonify(link.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar link
@api.route("/link/<int:id>", methods=["DELETE"])
def link_delete(id):
    link = Link.query.filter_by(id=id).first() 
    if link.delete_link():
        return jsonify(dict(mesage='Link eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#tipo de moneda
@api.route("/tipo-moneda/<int:id>", methods=["GET"])#id menu
def moneda(id):
    moneda=TipoMoneda.query.filter_by(id=id).first()
    if moneda is not None:
        return jsonify(moneda.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar moneda
@api.route("/tipo-moneda/<int:id>", methods=["DELETE"])
def moneda_delete(id):
    moneda = TipoMoneda.query.filter_by(id=id).first() 
    if moneda.delete_moneda():
        return jsonify(dict(mesage='Tipo de Moneda eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#departamento
@api.route("/departamento/<int:id>", methods=["GET"])
def departamento(id):
    departamento=Departamento.query.filter_by(id=id).first()
    if departamento is not None:
        return jsonify(departamento.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar departamento
@api.route("/departamento/<int:id>", methods=["DELETE"])
def departamento_delete(id):
    departamento = Departamento.query.filter_by(id=id).first() 
    if departamento.delete_departamento():
        return jsonify(dict(mesage='Tipo de departamento eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#provincia
@api.route("/provincia/<int:id>", methods=["GET"])
def provincia(id):
    provincia=Provincia.query.filter_by(id=id).first()
    if provincia is not None:
        return jsonify(provincia.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar provincia
@api.route("/provincia/<int:id>", methods=["DELETE"])
def provincia_delete(id):
    provincia = Provincia.query.filter_by(id=id).first() 
    if provincia.delete_provincia():
        return jsonify(dict(mesage='Tipo de provincia eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#distrito
@api.route("/distrito/<int:id>", methods=["GET"])
def distrito(id=0):
    distrito=Distrito.query.filter_by(id=id).first()
    if distrito is not None:
        return jsonify(distrito.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar distrito
@api.route("/distrito/<int:id>", methods=["DELETE"])
def distrito_delete(id):
    distrito = Distrito.query.filter_by(id=id).first() 
    if distrito.delete_distrito():
        return jsonify(dict(mesage='Tipo de distrito eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#oficinas 
@api.route("/oficina/<int:id>", methods=["GET"])
def oficina(id):
    oficina=Oficina.query.filter_by(id=id).first()
    if oficina is not None:
        return jsonify(oficina.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar oficina
@api.route("/oficina/<int:id>", methods=["DELETE"])
def oficina_delete(id):
    oficina = Oficina.query.filter_by(id=id).first() 
    if oficina.delete_oficina():
        return jsonify(dict(mesage='oficina eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#personas 
@api.route("/persona/<int:id>", methods=["GET"])
def persona(id):
    persona=Persona.query.filter_by(id=id).first()
    if persona is not None:
        return jsonify(persona.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar persona
@api.route("/persona/<int:id>", methods=["DELETE"])
def persona_delete(id):
    persona = Persona.query.filter_by(id=id).first() 
    if persona.delete_persona():
        return jsonify(dict(mesage='Persona eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#usuarios 
@api.route("/usuario/<int:id>", methods=["GET"])
def usuario(id):
    usuario=Usuario.query.filter_by(id=id).first()
    if usuario is not None:
        return jsonify(usuario.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar usuario
@api.route("/usuario/<int:id>", methods=["DELETE"])
def usuario_delete(id):
    usuario = Usuario.query.filter_by(id=id).first() 
    if usuario.delete_usuario():
        return jsonify(dict(mesage='usuario eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass