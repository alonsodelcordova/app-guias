from . import api_admin as api

from app.models.Cargo import Cargo
from app.models.TipoMoneda import TipoMoneda
from app.models.Oficina import Oficina

from app.models.Usuario import Usuario
from app.models.Persona import Persona

from app.models.Pregunta import Pregunta

from flask import jsonify


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


#preguntas 
@api.route("/pregunta/<int:id>", methods=["GET"])
def pregunta(id):
    pregunta=Pregunta.query.filter_by(id=id).first()
    if pregunta is not None:
        return jsonify(pregunta.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar pregunta
@api.route("/pregunta/<int:id>", methods=["DELETE"])
def pregunta_delete(id):
    pregunta = Pregunta.query.filter_by(id=id).first() 
    if pregunta.delete_pregunta():
        return jsonify(dict(mesage='Pregunta eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass