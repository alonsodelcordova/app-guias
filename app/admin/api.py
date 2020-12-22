from . import api_admin as api
from app.models.Departamento import Departamento
from app.models.Provincia import Provincia
from app.models.Distrito import Distrito

from flask import jsonify

@api.route("/departamentos", methods=["GET"])
def departamentos():
    departamentos = Departamento.query.all()
    return jsonify([(departamento.to_json()) for departamento in departamentos])

@api.route("/provincias", methods=["GET"])
@api.route("/provincias/<int:id>", methods=["GET"])#id departamento
def provincias(id=0):
    provincias = ''
    if id == 0:
        provincias = Provincia.query.all()
    else:
        provincias=Provincia.query.filter_by(id_departamento=id)
    return jsonify([(provincia.to_json()) for provincia in provincias])

@api.route("/distritos", methods=["GET"])
@api.route("/distritos/<int:id>", methods=["GET"])# id provincias
def distritos(id=0):
    distritos=''
    if id == 0 :
        distritos = Distrito.query.all()
    else:
        distritos=Distrito.query.filter_by(id_provincia=id)
    return jsonify([(distrito.to_json()) for distrito in distritos])
