from . import api_secretaria as api

from app.models.MotivoTraslado import MotivoTraslado
from app.models.GuiaRemision import GuiaRemision
from app.models.Factura import Factura
from app.models.Vehiculo import Vehiculo
from app.models.Transportista import Transportista
from app.models.Cliente import Cliente
from app.models.DescripcionGuia import DescripcionGuia

from flask import jsonify

#motivo 
@api.route("/motivo/<int:id>", methods=["GET"])
def motivo(id):
    motivo=MotivoTraslado.query.filter_by(id=id).first()
    if motivo is not None:
        return jsonify(motivo.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar motivo
@api.route("/motivo/<int:id>", methods=["DELETE"])
def motivo_delete(id):
    motivo = MotivoTraslado.query.filter_by(id=id).first() 
    if motivo.delete_motivo():
        return jsonify(dict(mesage='Motivo eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#guia 
@api.route("/guia/<int:id>", methods=["GET"])
def guia(id):
    guia=GuiaRemision.query.filter_by(id=id).first()
    if guia is not None:
        return jsonify(guia.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

"""#eliminar guia
@api.route("/guia/<int:id>", methods=["DELETE"])
def guia_delete(id):
    guia = GuiaRemision.query.filter_by(id=id).first() 
    if guia.delete_guia():
        return jsonify(dict(mesage='Guia eliminada'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass"""

#descripcion 
@api.route("/descripcion-guia/<int:id>", methods=["GET"])
def descripcion(id):
    descripcion=DescripcionGuia.query.filter_by(id=id).first()
    if descripcion is not None:
        return jsonify(descripcion.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar descripcion
@api.route("/descripcion-guia/<int:id>", methods=["DELETE"])
def descripcion_delete(id):
    descripcion = DescripcionGuia.query.filter_by(id=id).first() 
    if descripcion.delete_descripcion():
        return jsonify(dict(mesage='Descripcion eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#factura 
@api.route("/factura/<int:id>", methods=["GET"])
def factura(id):
    factura=Factura.query.filter_by(id=id).first()
    if factura is not None:
        return jsonify(factura.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar factura
@api.route("/factura/<int:id>", methods=["DELETE"])
def factura_delete(id):
    factura = Factura.query.filter_by(id=id).first() 
    if factura.delete_factura():
        return jsonify(dict(mesage='Factura eliminada'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#vehiculo 
@api.route("/vehiculo/<int:id>", methods=["GET"])
def vehiculo(id):
    vehiculo=Vehiculo.query.filter_by(id=id).first()
    if vehiculo is not None:
        return jsonify(vehiculo.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar vehiculo
@api.route("/vehiculo/<int:id>", methods=["DELETE"])
def vehiculo_delete(id):
    vehiculo = Vehiculo.query.filter_by(id=id).first() 
    if vehiculo.delete_vehiculo():
        return jsonify(dict(mesage='vehiculo eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#transportista 
@api.route("/transportista/<int:id>", methods=["GET"])
def transportista(id):
    transportista=Transportista.query.filter_by(id=id).first()
    if transportista is not None:
        return jsonify(transportista.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar transportista
@api.route("/transportista/<int:id>", methods=["DELETE"])
def transportista_delete(id):
    transportista = Transportista.query.filter_by(id=id).first() 
    if transportista.delete_transportista():
        return jsonify(dict(mesage='Transportista eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass

#cliente 
@api.route("/cliente/<int:id>", methods=["GET"])
def cliente(id):
    cliente=Cliente.query.filter_by(id=id).first()
    if cliente is not None:
        return jsonify(cliente.to_json())
    else:
        return jsonify(dict(mesage='Recurso no encontrado')),404
    pass

#eliminar cliente
@api.route("/cliente/<int:id>", methods=["DELETE"])
def cliente_delete(id):
    cliente = Cliente.query.filter_by(id=id).first() 
    if cliente.delete_cliente():
        return jsonify(dict(mesage='Cliente eliminado'))
    else:
        return jsonify(dict(mesage='No se puede Eliminar')),404
    pass